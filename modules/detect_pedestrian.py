import cv2
import numpy as np

class Pedestrian:
    def __init__(self, gt_file):
        self.cont = 0
        self.labels = self.read_txt(gt_file)
        self.trajectoria = []

    def detect(self, frame):
        image_id = self.cont
        if image_id in self.labels:
            for x, y in self.labels[image_id]:
                # Vamos normalizar as coordenadas x, y para que elas se encaixem na imagem
                height, width, _ = frame.shape  # Pega as dimensões da imagem
                x = int((x + 1) / 2 * width)  # Normaliza x para [0, width]
                y = int((y + 1) / 2 * height)  # Normaliza y para [0, height]

                # Verifica se x e y estão dentro das dimensões da imagem
                if x > width or y > height:
                    print(f"Os valores de x ({x}) e y ({y}) estão fora das dimensões da imagem ({width}x{height})")

                # Imprime a posição x, y
                print(f"Posição: ({x}, {y})")
                self.trajectoria.append((x, y))  # Adiciona a nova posição à trajectória

        # Desenha um círculo em cada posição da trajectória
        for pos in self.trajectoria:
            cv2.circle(frame, (pos[0], pos[1]), 30, (0, 255, 0), -1)
        
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
