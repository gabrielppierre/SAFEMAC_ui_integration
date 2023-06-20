from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from datetime import datetime
import cv2
import numpy as np
import os
from . single6dofPose.darknet import Darknet
from . single6dofPose.utils import get_region_boxes
import torch
from PIL import Image
from torch.autograd import Variable
from . detectt import Darknet_dummy

class CameraWindow(QMainWindow):
    def __init__(self, cap):
        super(CameraWindow, self).__init__()
        self.camera_label = QLabel()
        self.setCentralWidget(self.camera_label)
        self.showMaximized()
        self.cap = cap
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_frame)
        self.update_timer.start(1)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            pixmap = pixmap.scaled(self.camera_label.width(), self.camera_label.height(), Qt.IgnoreAspectRatio)
            self.camera_label.setPixmap(pixmap)

class CameraManager:
    def __init__(self, cameras, frame):
        self.cameras = cameras
        self.timers = [QTimer() for _ in self.cameras]
        for timer in self.timers:
            timer.timeout.connect(self.update_frame)
        self.caps = [None for _ in self.cameras]
        self.video_paths = []
        self.camera_indices = []
        self.recorders = [None for _ in self.cameras]
        self.recording = False
        self.maximized_camera = None
        self.frame = frame
        self.camera_windows = [None for _ in self.cameras]
        self.modelcfg = "yolo-pose.cfg"
        self.weightfile = "PATH_TO_MODEL_WEIGHTS"#nao consegui encontrar o arquivo de pesos
        self.target_shape = (680, 680)  #tamanho teste pra redimensionar as imagens
        self.current_camera_index = 0
    
    #implementacao do metodo 'detect' de Kelvin para funcionar quadro a quadro
    def detect(self, frame):
        
        #inicializacao do modelo Darknet
        #model = Darknet(self.modelcfg)
        model = Darknet_dummy('labels\\scene_gt.json', 'C:\\Users\\gabsp\\Downloads\\lm_train (1)\\train\\000001\\scene_camera.json', 'C:\\Users\\gabsp\\Downloads\\lm_models (2)\\models_eval\\obj_000001.ply')
        #model.load_weights(self.weightfile)
        #model.cuda()
        #model.eval()

        #conversao do quadro em uma imagem do tipo RGB
        #image = Image.fromarray(frame).convert('RGB')

        #redimensionamento da imagem para o tamanho de destino
        #image = image.resize(self.target_shape)

        #conversao da imagem em um tensor e reformatando-o para se adequar ao modelo
        #image = torch.ByteTensor(torch.ByteStorage.from_buffer(image.tobytes()))
        #image = image.view(self.target_shape[1], self.target_shape[0], 3).transpose(0, 1).transpose(0, 2).contiguous()
        #image = image.view(1, 3, self.target_shape[1], self.target_shape[0])
        #image = image.float().div(255.)

        #movendo o tensor da imagem para a GPU e encapsulando-o em uma variavel
        #image = image.cuda()
        #image = Variable(image, volatile=True)

        #obtendo a saida do modelo para a imagem
        #output = model(image).data

        #extracao das caixas delimitadoras das regioes de interesse
        #box = get_region_boxes(output, 1, 9)

        #processamento das coordenadas dos cantos 2D
        #corners2D = np.array(np.reshape(box[:18], [-1, 2]), dtype='float32')
        #corners2D[:, 0] = corners2D[:, 0] * self.target_shape[0]
        #corners2D[:, 1] = corners2D[:, 1] * self.target_shape[1]

        corners2D = model.detect(0)
        print(corners2D.shape)

        #retorno das coordenadas dos cantos 2D como resultado da deteccao
        return corners2D
    
    def print_points(self, img, points):
        for (x, y) in points:
            cv2.circle(img, (int(x), int(y)), 3, (0, 255, 0), -1)
        return img  

    #@staticmethod
    #def detect(img):
        #este metodo atualmente retorna um ponto no centro da imagem
        #futuramente, implementar o detector do single6dofpose aqui
        #height, width, _ = img.shape
        #return [(width // 2, height // 2)]

    #@staticmethod
    #def print_points(img, points):
        #desenha um pequeno circulo para cada ponto
        #for point in points:
        #    img = cv2.circle(img, point, radius=3, color=(0, 255, 0), thickness=-1)
        #return img 

    def add_camera_clicked(self):
        # Atualiza camera_index para usar a câmera atual.
        camera_index = self.current_camera_index
        if camera_index in self.camera_indices:
            return
        for i in range(len(self.caps)):
            if self.caps[i] is None:
                self.caps[i] = cv2.VideoCapture(camera_index)
                self.camera_indices.append(camera_index)
                self.timers[i].start(1)
                break
        self.current_camera_index += 1 # Incrementa o índice da câmera após adicionar uma.

    def add_recordings(self):
        #abre uma caixa de dialogo para selecionar arquivos de video
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        video_paths, _ = file_dialog.getOpenFileNames(None, "Select Videos", ".", "Video Files (*.mp4 *.flv *.ts *.3gp *.mov *.avi *.wmv *.png)")
        self.video_paths.extend(video_paths)

    def start_recording(self):
        if self.recording:
            return

        self.recording = True
        recordings_dir = "recordings"
        if not os.path.exists(recordings_dir):
            os.makedirs(recordings_dir)
        current_datetime = datetime.now()
        folder_name = current_datetime.strftime("%d-%m-%Y[%H-%M-%S]")
        folder_path = os.path.join(recordings_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        for i in range(len(self.recorders)):
            if self.recorders[i] is None and self.caps[i] is not None:
                #cria o caminho do video
                video_path = os.path.join(folder_path, f'output{i}.mp4')
                #cria o gravador de video
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                fps = self.caps[i].get(cv2.CAP_PROP_FPS)
                frame_width = int(self.caps[i].get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(self.caps[i].get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.recorders[i] = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

    def stop_recording(self):
        self.recording = False
        for i in range(len(self.recorders)):
            if self.recorders[i] is not None:
                #libera o gravador de video
                self.recorders[i].release()
                self.recorders[i] = None

    def view_recordings(self):
        for video_path in self.video_paths:
            for i in range(len(self.caps)):
                if self.caps[i] is None:
                    self.caps[i] = cv2.VideoCapture(video_path)
                    self.timers[i].start(1) #atualiza o frame a cada 1ms
                    break
        self.video_paths.clear() #limpa a lista de caminhos de video

    def update_frame(self):
        for i in range(len(self.caps)):
            if self.caps[i] is not None:
                ret, frame = self.caps[i].read()
                if ret:
                    frame = cv2.flip(frame, 1) #espelha o frame horizontalmente
                    #detecta pontos no frame
                    points = self.detect(frame)
                    #desenha circulos em torno dos pontos
                    frame = self.print_points(frame, points)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    if self.recording and self.recorders[i] is not None:
                        #converte o frame de volta para BGR, pois OpenCV espera que o frame esteja em BGR
                        self.recorders[i].write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                    #converteo frame para QImage
                    img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(img)
                    #redimensione a QPixmap para caber na QLabel
                    pixmap = pixmap.scaled(self.cameras[i].width(), self.cameras[i].height(), Qt.IgnoreAspectRatio)
                    self.cameras[i].setPixmap(pixmap)
                else:
                    self.timers[i].stop()
                    if self.recording and self.recorders[i] is not None:
                        #libera o gravador de video se estiver gravando
                        self.recorders[i].release()
                        self.recorders[i] = None
                    #libera a captura de video
                    self.caps[i].release()
                    self.caps[i] = None
    
    def maximize_camera(self, index):
        if self.maximized_camera == index:
            self.maximized_camera = None
            self.camera_windows[index].close()
            self.camera_windows[index] = None
        else:
            for i, window in enumerate(self.camera_windows):
                if window is not None:
                    window.close()
                    self.camera_windows[i] = None
            self.camera_windows[index] = CameraWindow(self.caps[index])  #passa a instancia do VideoCapture para a CameraWindow
            self.maximized_camera = index

    def update_frame(self):
        for i in range(len(self.caps)):
            if self.caps[i] is not None:
                ret, frame = self.caps[i].read()
                if ret:
                    frame = cv2.flip(frame, 1) #espelha o frame horizontalmente
                    #detecta pontos no frame
                    points = self.detect(frame)
                    #desenha circulos em torno dos pontos
                    frame = self.print_points(frame, points)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    if self.recording and self.recorders[i] is not None:
                        #converte o frame de volta para BGR, pois OpenCV espera que o frame esteja em BGR
                        self.recorders[i].write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                    #converteo frame para QImage
                    img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(img)
                    #redimensione a QPixmap para caber na QLabel
                    pixmap = pixmap.scaled(self.cameras[i].width(), self.cameras[i].height(), Qt.IgnoreAspectRatio)
                    self.cameras[i].setPixmap(pixmap)
                else:
                    self.timers[i].stop()
                    if self.recording and self.recorders[i] is not None:
                        #libera o gravador de video se estiver gravando
                        self.recorders[i].release()
                        self.recorders[i] = None
                    #libera a captura de video
                    self.caps[i].release()
                    self.caps[i] = None
    
    def maximize_camera(self, index):
        if self.maximized_camera == index:
            self.maximized_camera = None
            self.camera_windows[index].close()
            self.camera_windows[index] = None
        else:
            for i, window in enumerate(self.camera_windows):
                if window is not None:
                    window.close()
                    self.camera_windows[i] = None
            self.camera_windows[index] = CameraWindow(self.caps[index])  #passa a instancia do VideoCapture para a CameraWindow
            self.maximized_camera = index
