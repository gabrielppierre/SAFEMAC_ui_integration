import cv2
import numpy as np
from utils import get_region_boxes

def estimate_worker_3d_position(image, model, num_classes, num_keypoints, cameraMatrix, distCoeffs):
    """
    Estima a posição tridimensional dos trabalhadores em uma imagem.

    Args:
        image: Imagem na qual os trabalhadores devem ser detectados e suas posições estimadas.
        model: Modelo de detecção de pessoas treinado.
        num_classes: Número de classes no modelo de detecção.
        num_keypoints: Número de keypoints usados na detecção.
        cameraMatrix: Matriz da câmera.
        distCoeffs: Coeficientes de distorção da câmera.

    Return:
        Uma lista de posições 3D estimadas para os trabalhadores na imagem.
    """
    #obtenha as detecções dos trabalhadores na imagem usando a função get_region_boxes()
    detections = get_region_boxes(image, num_classes, num_keypoints)

    #implementar um algoritmo para estimar a posição 3D dos trabalhadores
    #a partir das detecções obtidas acima.
    worker_positions_3d = []

    for detection in detections:
        #estima a posição 3D do trabalhador a partir da detecção
        worker_position_3d = estimate_3d_position_from_detection(detection, cameraMatrix, distCoeffs)

        worker_positions_3d.append(worker_position_3d)

    return worker_positions_3d

def estimate_3d_position_from_detection(detection, cameraMatrix, distCoeffs):
    """
    Estima a posição 3D de um trabalhador a partir de uma detecção.

    Args:
        detection: Detecção de um trabalhador na imagem.
        cameraMatrix: Matriz da câmera.
        distCoeffs: Coeficientes de distorção da câmera.

    Return:
        A posição 3D estimada do trabalhador.
    """
    #implementar aqui o algoritmo para estimar a posição 3D do trabalhador a partir da detecçao
    #usar a função pnp() para obter a posição 3D a partir dos pontos 2D e 3D
    points_2D, points_3D = get_2D_and_3D_points(detection)
    _, rvec, tvec = cv2.solvePnP(points_3D, points_2D, cameraMatrix, distCoeffs)

    return np.squeeze(tvec)