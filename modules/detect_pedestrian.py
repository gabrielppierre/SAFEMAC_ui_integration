import cv2
import numpy as np
import xml.etree.ElementTree as ET

class Pedestrian:
    def __init__(self, gt_file, extrinsics_file, intrinsics_file):
        self.cont = 0
        self.labels = self.read_txt(gt_file)
        self.cameraMatrix, self.distCoeffs = self.read_intrinsics(intrinsics_file)
        self.rvec, self.tvec = self.read_extrinsics(extrinsics_file)
        self.trajectoria = []

    def read_intrinsics(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        camera_matrix = np.array(root.find('camera_matrix/data').text.split(), dtype='float32').reshape((3, 3))
        dist_coeffs = np.array(root.find('distortion_coefficients/data').text.split(), dtype='float32').reshape(-1, 1)

        return camera_matrix, dist_coeffs

    def read_extrinsics(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        rvec = np.array(root.find('rvec').text.split(), dtype='float32')
        tvec = np.array(root.find('tvec').text.split(), dtype='float32')

        return rvec, tvec

    def detect(self, frame):
        image_id = self.cont
        if image_id in self.labels:
            points_3d = []
            for x, y in self.labels[image_id]:
                #adiciona a terceira coordenada
                points_3d.append((x, y, 0))

            #projetar os pontos 3D na imagem da camera
            points_2d, _ = cv2.projectPoints(np.array(points_3d, dtype='float32'), self.rvec, self.tvec, self.cameraMatrix, self.distCoeffs)
            
            #desenha um circulo em cada posição projetada
            for point in points_2d:
                x, y = map(int, point.ravel())
                self.trajectoria.append((x, y))  #adiciona a nova posição na trajetoria
                cv2.circle(frame, (x, y), 15, (0, 255, 0), -1)

        print(self.trajectoria)
        self.cont += 1
        return frame

    def read_txt(self, filename):
        labels = {}
        with open(filename) as f:
            for line in f:
                frame_number, x, y = map(float, line.strip().split())
                if int(frame_number) in labels:
                    labels[int(frame_number)].append((x, y))
                else:
                    labels[int(frame_number)] = [(x, y)]
        return labels

    def reset_parameters(self):
        self.cont = 0
        self.trajectoria = []