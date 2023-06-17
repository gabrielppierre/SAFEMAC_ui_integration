import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def undistort_image(img, mtx, dist):
    h, w = img.shape[:2]
    new_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

    dst = cv2.undistort(img, mtx, dist, None, new_mtx)

    x, y, w, h = roi
    dst = dst[y:y + h, x:x + w]
    return dst

def load_calibration_results():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return None, None

    with open(file_path, "r") as file:
        content = file.readlines()

    mtx = np.array(eval(content[1]), dtype=np.float32)
    dist = np.array(eval(content[4]), dtype=np.float32)

    return mtx, dist

def view_undistorted_camera():
    mtx, dist = load_calibration_results()
    if mtx is None or dist is None:
        messagebox.showerror("Erro", "Não foi possível carregar os resultados da calibração.")
        return

    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if not img_path:
        return

    img = cv2.imread(img_path)
    undistorted_img = undistort_image(img, mtx, dist)

    window_name = "Imagem corrigida"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def view_undistorted_live():
    mtx, dist = load_calibration_results()
    if mtx is None or dist is None:
        messagebox.showerror("Erro", "Não foi possível carregar os resultados da calibração.")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Erro", "Não foi possível acessar a câmera.")
        return

    window_name = "Câmera corrigida em tempo real"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Erro", "Não foi possível obter um frame da câmera.")
            break

        undistorted_frame = undistort_image(frame, mtx, dist)
        cv2.imshow(window_name, undistorted_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()