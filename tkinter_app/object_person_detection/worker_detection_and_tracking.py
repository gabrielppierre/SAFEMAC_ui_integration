import cv2
import numpy as np
import time
import camera_utils

#carrega a rede neural YOLO pre-treinada
net = cv2.dnn.readNetFromDarknet('yolo.cfg', 'yolo.weights')

#define as classes de objetos a serem detectadas
classes = ['worker']

#configuracoes da rede neural
conf_threshold = 0.5
nms_threshold = 0.4

#carrega os dados de calibracao da camera
calibration_file_path = 'calibration_data.npz'
camera_matrix, dist_coeffs = camera_utils.load_calibration_data(calibration_file_path)

#captura a imagem da camera
camera_indices = {0: 'frontal'}
images = camera_utils.image_capture(camera_indices)
img = images['frontal']

#obtem as dimensoes da imagem
(h, w) = img.shape[:2]

#cria um blob de entrada de imagem para a rede neural
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

#configura a entrada para a rede neural
net.setInput(blob)

#obtem as camadas de saida da rede neural
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

#executa a deteccao de objetos na imagem
outputs = net.forward(output_layers)

#inicializa as listas de caixas delimitadoras, confiança e IDs de classe
boxes = []
confidences = []
class_ids = []

#inicializa a variavel de contagem de trabalhadores
worker_count = 0

#itera pelas saidas da rede neural
for output in outputs:
    #itera pelas deteccoes
    for detection in output:
        #obtem as probabilidades de classe e as coordenadas da caixa delimitadora
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > conf_threshold and classes[class_id] == 'worker':
            #incrementa a contagem de trabalhadores
            worker_count += 1

            #calcula as coordenadas da caixa delimitadora na imagem original
            box = detection[0:4] * np.array([w, h, w, h])
            (center_x, center_y, width, height) = box.astype('int')
            x = int(center_x - (width / 2))
            y = int(center_y - (height / 2))
            #adiciona as informacoes da detecaao as listas
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

for i in indices:
    i = i[0]
    box = boxes[i]
    x, y, w, h = box[0], box[1], box[2], box[3]
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    points_2D, points_3D = camera_utils.get_2D_and_3D_points(detection)
    mean_3D = np.mean(points_3D, axis=1)
    print(f"Coordenadas 3D da detecção {i}: ({mean_3D[0]:.2f}, {mean_3D[1]:.2f}, {mean_3D[2]:.2f})")

#exibe a imagem com as deteccoes
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#salva a imagem de saida
cv2.imwrite('output.jpg', img)