import numpy as np

def get_camera_intrinsic(u0, v0, fx, fy):
    """
    Retorna a matriz de calibração intrínseca da câmera.
    Args:
        u0 (float): Coordenada x do ponto principal.
        v0 (float): Coordenada y do ponto principal.
        fx (float): Distância focal em pixels no eixo x.
        fy (float): Distância focal em pixels no eixo y.
    Returns:
        np.ndarray: Matriz de calibração intrínseca.
    """
    return np.array([[fx, 0.0, u0], [0.0, fy, v0], [0.0, 0.0, 1.0]])

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
