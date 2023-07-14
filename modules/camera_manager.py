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
from . detect_darknet import Darknet_dummy
from . detect_pedestrian import Pedestrian
import time

class CameraWindow(QMainWindow):
    def __init__(self, cap, detect_func, print_points_func):
        super(CameraWindow, self).__init__()
        self.camera_label = QLabel()
        self.setCentralWidget(self.camera_label)
        self.showMaximized()
        self.cap = cap
        self.detect_func = detect_func
        self.print_points_func = print_points_func
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_frame)
        self.update_timer.start(1)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            points = self.detect_func(frame)
            frame = self.print_points_func(frame, points)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            pixmap = pixmap.scaled(self.camera_label.width(), self.camera_label.height(), Qt.IgnoreAspectRatio)
            self.camera_label.setPixmap(pixmap)

class DetectorFactory:
    def __init__(self):
        self.detectors = {"Darknet Dummy": Darknet_dummy, "Pedestrian": Pedestrian}

    def create_detector(self, detector_type, files):
        if len(files) != 3: 
            print(f"Número incorreto de arquivos selecionados para {detector_type}. Por favor, selecione novamente.")
            return None

        detector_class = self.detectors.get(detector_type)
        if detector_class is None:
            raise ValueError(f"Invalid detector type: {detector_type}")

        return detector_class(*files)


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
        #self.modelcfg = "yolo-pose.cfg"
        #self.weightfile = "PATH_TO_MODEL_WEIGHTS"
        #self.target_shape = (680, 680)  #tamanho teste pra redimensionar as imagens
        self.current_camera_index = 0
        self.model = None
        self.detector_factory = DetectorFactory()
        self.mesh_enabled = False
        self.points_history = [[] for _ in self.cameras]
    
    def toggle_mesh(self):
        self.mesh_enabled = not self.mesh_enabled

    def print_points(self, img, points):
        if points is not None:
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
        #   img = cv2.circle(img, point, radius=3, color=(0, 255, 0), thickness=-1)
        #return img 

    def select_files(self):
        #pergunta ao usuario para qual funçao os arquivos devem ser selecionados
        file_type, _ = QInputDialog.getItem(None, "Selecione o tipo de arquivo", "Para qual funçao você deseja adicionar os arquivos?", ["Darknet Dummy", "Pedestrian"], 0, False)
        
        #abre dialogos de seleçao de arquivo de acordo com a funçao escolhida
        files = []
        if file_type == "Darknet Dummy":
            files.append(QFileDialog.getOpenFileName(None, "Selecione o arquivo scene_gt.json", "", "JSON Files (*.json)")[0])
            files.append(QFileDialog.getOpenFileName(None, "Selecione o arquivo scene_camera.json", "", "JSON Files (*.json)")[0])
            files.append(QFileDialog.getOpenFileName(None, "Selecione o arquivo obj.ply", "", "PLY Files (*.ply)")[0])
        else:  #file_type == "Pedestrian"
            files.append(QFileDialog.getOpenFileName(None, "Selecione a lista de pontos 3d a serem projetados", "", "TXT Files (*.txt)")[0])
            files.append(QFileDialog.getOpenFileName(None, "Selecione o ext", "", "XML Files (*.xml)")[0])
            files.append(QFileDialog.getOpenFileName(None, "Selecione o intr", "", "XML Files (*.xml)")[0])


        #verifica se todos os arquivos foram selecionados
        if all(files):
            self.model = self.detector_factory.create_detector(file_type, files)
            return True

        #pergunta ao usuario se deseja cancelar
        reply = QMessageBox.warning(None, "Aviso", "Arquivos necessarios nao selecionados. Cancelar?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return False
        else:
            return self.select_files()

    def add_camera_clicked(self):
        user_wants_to_select_files = QMessageBox.question(None, "Aviso", "Deseja selecionar arquivos especificos para a camera?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes
        if user_wants_to_select_files and not self.select_files():
            return

        while True:
            cap = cv2.VideoCapture(self.current_camera_index)
            time.sleep(1)  #adiciona um atraso para dar tempo pra camera inicializar
            if cap.isOpened():
                break
            cap.release()
            self.current_camera_index += 1
            if self.current_camera_index > 10:  #limitando a busca até o indice 10 para evitar um loop infinito
                print("Nenhuma camera disponivel encontrada.")
                return

        for i in range(len(self.caps)):
            if self.caps[i] is None:
                self.caps[i] = cap
                self.camera_indices.append(self.current_camera_index)
                self.timers[i].start(1)
                break

        self.current_camera_index += 1 #incrementa o indice da camera apos adicionar uma.


    def add_recordings(self):
        user_wants_to_select_files = QMessageBox.question(None, "Aviso", "Deseja selecionar arquivos adicionais para o video?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes
        if user_wants_to_select_files and not self.select_files():
            return

        #Abre uma caixa de dialogo para selecionar arquivos de video
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
                    frame = cv2.flip(frame, 1)  #espelha

                    #Realiza a detecçao se self.model nao for None
                    if self.model is not None:
                        frame = self.model.detect(frame)
                    else:
                        print("Modelo nao inicializado.")
                        return None

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    
                    if self.recording and self.recorders[i] is not None:
                        #Converte o frame de volta para BGR, pois o OpenCV espera que o frame esteja em BGR
                        self.recorders[i].write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                    
                    #Converte o frame para QImage
                    img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(img)
                    #Redimensiona a QPixmap para caber na QLabel
                    pixmap = pixmap.scaled(self.cameras[i].width(), self.cameras[i].height(), Qt.IgnoreAspectRatio)
                    self.cameras[i].setPixmap(pixmap)
                else:
                    self.timers[i].stop()
                    if self.recording and self.recorders[i] is not None:
                        #Libera o gravador de video se estiver gravando
                        self.recorders[i].release()
                        self.recorders[i] = None
                    #Libera a captura de video
                    self.caps[i].release()
                    self.caps[i] = None



    def stop_visu(self):
        #Parar todas as cameras
        for i in range(len(self.caps)):
            if self.caps[i] is not None:
                self.timers[i].stop()
                self.caps[i].release()
                self.caps[i] = None

        #Parar todas as gravaçoes
        for recorder in self.recorders:
            if recorder is not None:
                recorder.release()

        #Limpar as janelas de visualizaçao de camera
        for window in self.camera_windows:
            if window is not None:
                window.close()
        self.camera_windows = [None for _ in self.cameras]

        #Limpar a lista de capturas de video e gravadores
        self.caps = [None for _ in self.cameras]
        self.recorders = [None for _ in self.cameras]

        #Reiniciar a lista de indices de camera
        self.camera_indices = []

        #Reiniciar o indice da camera atual
        self.current_camera_index = 0
        if self.model is not None: #Adiciona uma verificaçao para self.model
            self.model.reset_parameters()

        for camera in self.cameras:
            camera.clear()

    
    def maximize_camera(self, index):
        if self.caps[index] is None:
            print(f"Nenhuma camera ativa ou video no indice {index}")
            return

        if self.maximized_camera == index:
            self.maximized_camera = None
            self.camera_windows[index].close()
            self.camera_windows[index] = None
        else:
            for i, window in enumerate(self.camera_windows):
                if window is not None:
                    window.close()
                    self.camera_windows[i] = None
            self.camera_windows[index] = CameraWindow(self.caps[index], self.detect, self.print_points)
            self.maximized_camera = index

    