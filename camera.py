#este modulo lidara com as funcoes relacionadas a camera e a calibracao da camera.
import cv2
import numpy as np
import glob

def image_capture(camera_indices):
    '''
    recebe um dicionario chamado camera_indices, onde as chaves sao os indices das cameras e os valores sao os
    nomes das cameras (por exemplo, 'frontal', 'lateral_direita', etc.). A funcao captura imagens de todas as
    cameras listadas no dicionario e retorna um novo dicionario chamado captured_images, onde as chaves sao os
    nomes das cameras e os valores sao as imagens capturadas.
    '''
    captured_images = {}

    for cam_id, cam_name in camera_indices.items():
        #acessando a camera
        cap = cv2.VideoCapture(cam_id)

        #verificando se a camera esta aberta
        if not cap.isOpened():
            print(f"Não foi possível abrir a câmera {cam_name}.")
            continue

        #capturando a imagem
        ret, frame = cap.read()

        #verificando se a captura foi bem-sucedida
        if not ret:
            print(f"Não foi possível capturar a imagem da câmera {cam_name}.")
        else:
            captured_images[cam_name] = frame

        #liberando o objeto cap e fechando a janela
        cap.release()

    return captured_images

#na main:
""" from image_capture import image_capture
import cv2

camera_indices = {
    0: 'frontal',
    1: 'lateral_direita',
    2: 'lateral_esquerda',
    3: 'traseira'
}

captured_images = image_capture(camera_indices)

# Exemplo de uso das imagens capturadas
for camera_name, image in captured_images.items():
    cv2.imshow(camera_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows() """


def calibrate_camera(images_path, chessboard_size=(6, 9)):
    """
    Calibra a camera usando varias imagens do padrao de tabuleiro de xadrez.

    Args:
        images_path: Caminho das imagens do tabuleiro de xadrez.
        chessboard_size: Tamanho do tabuleiro de xadrez (linhas, colunas).

    Returns:
        mtx: Matriz da camera.
        dist: Coeficientes de distorcao.
    """

    #preparar pontos de objeto, como (0,0,0), (1,0,0), (2,0,0) ..., (6,9,0)
    objp = np.zeros((chessboard_size[0]*chessboard_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:chessboard_size[1], 0:chessboard_size[0]].T.reshape(-1, 2)

    #arrays para armazenar pontos de objeto e pontos de imagem de todas as imagens
    objpoints = []  #Pontos 3D no espaco do mundo real
    imgpoints = []  #Pontos 2D no plano da imagem

    #lista de imagens
    images = glob.glob(images_path)

    #iterar atraves das imagens e encontrar os cantos do tabuleiro de xadrez
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #encontrar os cantos do tabuleiro de xadrez
        ret, corners = cv2.findChessboardCorners(gray, (chessboard_size[1], chessboard_size[0]), None)

        #se os cantos forem encontrados, adicione pontos de objeto e pontos de imagem
        if ret:
            objpoints.append(objp)
            imgpoints.append(corners)

    #calibrar a camera
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    return mtx, dist

images_path = 'path/to/your/chessboard/images/*.jpg'  #modificar este caminho de acordo com suas imagens
chessboard_size = (6, 9)  #modificar este tamanho de acordo com o padrao de tabuleiro de xadrez utilizado

mtx, dist = calibrate_camera(images_path, chessboard_size)
print("Matriz da camera:", mtx)
print("Coeficientes de distorcao:", dist)


def load_calibration_data(calibration_file):
    """
    Carrega os dados de calibração da câmera a partir de um arquivo.

    Args:
        calibration_file (str): O caminho para o arquivo de calibração.

    Returns:
        camera_matrix (numpy array): A matriz da câmera (matriz intrínseca).
        dist_coeffs (numpy array): Os coeficientes de distorção.
    """
    with np.load(calibration_file) as data:
        camera_matrix = data["camera_matrix"]
        dist_coeffs = data["dist_coeffs"]

    return camera_matrix, dist_coeffs


def get_region_boxes(output, num_classes, num_keypoints, only_objectness=1, validation=True):
    
    # Parameters
    anchor_dim = 1 
    if output.dim() == 3:
        output = output.unsqueeze(0)
    batch = output.size(0)
    assert(output.size(1) == (2*num_keypoints+1+num_classes)*anchor_dim)
    h = output.size(2)
    w = output.size(3)

    # Activation
    t0 = time.time()
    max_conf = -sys.maxsize
    output    = output.view(batch*anchor_dim, 2*num_keypoints+1+num_classes, h*w).transpose(0,1).contiguous().view(2*num_keypoints+1+num_classes, batch*anchor_dim*h*w)
    grid_x    = torch.linspace(0, w-1, w).repeat(h,1).repeat(batch*anchor_dim, 1, 1).view(batch*anchor_dim*h*w).cuda()
    grid_y    = torch.linspace(0, h-1, h).repeat(w,1).t().repeat(batch*anchor_dim, 1, 1).view(batch*anchor_dim*h*w).cuda()
    
    xs = list()
    ys = list()
    xs.append(torch.sigmoid(output[0]) + grid_x)
    ys.append(torch.sigmoid(output[1]) + grid_y)
    for j in range(1,num_keypoints):
        xs.append(output[2*j + 0] + grid_x)
        ys.append(output[2*j + 1] + grid_y)
    det_confs = torch.sigmoid(output[2*num_keypoints])
    cls_confs = torch.nn.Softmax()(Variable(output[2*num_keypoints+1:2*num_keypoints+1+num_classes].transpose(0,1))).data
    cls_max_confs, cls_max_ids = torch.max(cls_confs, 1)
    cls_max_confs = cls_max_confs.view(-1)
    cls_max_ids   = cls_max_ids.view(-1)
    t1 = time.time()
    
    # GPU to CPU
    sz_hw = h*w
    sz_hwa = sz_hw*anchor_dim
    det_confs = convert2cpu(det_confs)
    cls_max_confs = convert2cpu(cls_max_confs)
    cls_max_ids = convert2cpu_long(cls_max_ids)
    for j in range(num_keypoints):
        xs[j] = convert2cpu(xs[j])
        ys[j] = convert2cpu(ys[j])
    if validation:
        cls_confs = convert2cpu(cls_confs.view(-1, num_classes))
    t2 = time.time()

    # Boxes filter
    for b in range(batch):
        for cy in range(h):
            for cx in range(w):
                for i in range(anchor_dim):
                    ind = b*sz_hwa + i*sz_hw + cy*w + cx
                    det_conf =  det_confs[ind]
                    if only_objectness:
                        conf = det_confs[ind]
                    else:
                        conf = det_confs[ind] * cls_max_confs[ind]
                    
                    if conf > max_conf:
                        max_conf = conf
                        bcx = list()
                        bcy = list()
                        for j in range(num_keypoints):
                            bcx.append(xs[j][ind])
                            bcy.append(ys[j][ind])
                        cls_max_conf = cls_max_confs[ind]
                        cls_max_id = cls_max_ids[ind]
                        box = list()
                        for j in range(num_keypoints):
                            box.append(bcx[j]/w)
                            box.append(bcy[j]/h)
                        box.append(det_conf)
                        box.append(cls_max_conf)
                        box.append(cls_max_id)                        
    t3 = time.time()
    if False:
        print('---------------------------------')
        print('matrix computation : %f' % (t1-t0))
        print('        gpu to cpu : %f' % (t2-t1))
        print('      boxes filter : %f' % (t3-t2))
        print('---------------------------------')
    return box

