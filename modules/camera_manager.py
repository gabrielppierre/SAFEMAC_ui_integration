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
from .darknet_dummy import Darknet_dummy

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

class CameraManager:
    def __init__(self, cameras):
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
        self.camera_windows = [None for _ in self.cameras]
        self.modelcfg = "yolo-pose.cfg"
        self.weightfile = "PATH_TO_MODEL_WEIGHTS"
        self.target_shape = (680, 680)
        self.current_camera_index = 0
        self.model = Darknet_dummy('labels\\scene_gt.json', 'C:\\Users\\gabsp\\Downloads\\lm_train (1)\\train\\000001\\scene_camera.json', 'C:\\Users\\gabsp\\Downloads\\lm_models (2)\\models_eval\\obj_000001.ply')
    
    def detect(self, frame):
        corners2D = self.model.detect(0)
        print(corners2D.shape)
        return corners2D
    
    def print_points(self, img, points):
        for (x, y) in points:
            cv2.circle(img, (int(x), int(y)), 3, (0, 255, 0), -1)
        return img

    def add_camera_clicked(self):
        camera_index = self.current_camera_index
        if camera_index in self.camera_indices:
            return
        for i in range(len(self.caps)):
            if self.caps[i] is None:
                self.caps[i] = cv2.VideoCapture(camera_index)
                self.camera_indices.append(camera_index)
                self.timers[i].start(1)
                break
        self.current_camera_index += 1

    def add_recordings(self):
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
                video_path = os.path.join(folder_path, f'output{i}.mp4')
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                fps = self.caps[i].get(cv2.CAP_PROP_FPS)
                frame_width = int(self.caps[i].get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(self.caps[i].get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.recorders[i] = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

    def stop_recording(self):
        self.recording = False
        for i in range(len(self.recorders)):
            if self.recorders[i] is not None:
                self.recorders[i].release()
                self.recorders[i] = None

    def view_recordings(self):
        for video_path in self.video_paths:
            for i in range(len(self.caps)):
                if self.caps[i] is None:
                    self.caps[i] = cv2.VideoCapture(video_path)
                    self.timers[i].start(1)
                    break
        self.video_paths.clear()

    def update_frame(self):
        for i in range(len(self.caps)):
            if self.caps[i] is not None:
                ret, frame = self.caps[i].read()
                if ret:
                    frame = cv2.flip(frame, 0) #espelha o frame horizontalmente
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
            self.camera_windows[index] = CameraWindow(self.caps[index])
            self.maximized_camera = index
