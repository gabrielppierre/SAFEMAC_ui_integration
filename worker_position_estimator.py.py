import cv2
import numpy as np
from utils import get_region_boxes, pnp

import cv2

def estimate_3d_position_from_detection(detection, points_3D, camera_matrix, dist_coeffs):
    """
    Estima a posição 3D de um trabalhador a partir de uma detecção.

    Args:
        detection: Detecção de um trabalhador na imagem.
        points_3D: Coordenadas 3D conhecidas no espaço do mundo real.
        camera_matrix: Matriz da câmera.
        dist_coeffs: Coeficientes de distorção.

    Return:
        A posição 3D estimada do trabalhador.
    """

    #pontos 2D detectados na imagem
    points_2D = detection.keypoints

    #certificar de ter pelo menos 6 pontos correspondentes para usar o algoritmo PnP
    if len(points_2D) < 6 or len(points_3D) < 6:
        raise ValueError("Número insuficiente de pontos correspondentes para usar o algoritmo PnP.")

    # Resolver o problema de perspectiva-n-pontos (PnP)
    _, rvec, tvec = cv2.solvePnP(points_3D, points_2D, camera_matrix, dist_coeffs)

    #a posição 3D estimada do trabalhador eh dada pelo vetor de translação (tvec)
    worker_position_3d = tvec.flatten()

    return worker_position_3d