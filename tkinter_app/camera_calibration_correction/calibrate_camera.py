import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def calibrate_camera(images):
    width_tab = 7
    height_tab = 7
    square_size = 1.3

    objp = np.zeros((height_tab * width_tab, 3), np.float32)
    objp[:, :2] = np.mgrid[0:width_tab, 0:height_tab].T.reshape(-1, 2) * square_size

    objpoints = []
    imgpoints = []

    flags_to_try = [
        None,
        cv2.CALIB_CB_ADAPTIVE_THRESH,
        cv2.CALIB_CB_FAST_CHECK,
        cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_FAST_CHECK,
    ]

    for fname in images:
        img = cv2.imread(fname)
        
        if img is None:
            print(f"Erro ao ler a imagem: {fname}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for flags in flags_to_try:
            ret, corners = cv2.findChessboardCorners(gray, (width_tab, height_tab), flags)
            if ret:
                break

        if not ret:
            print(f"Erro ao encontrar cantos do tabuleiro de xadrez na imagem: {fname}")
            continue

        objpoints.append(objp)
        imgpoints.append(corners)

    if not objpoints or not imgpoints:
        print("Erro: Não foi possível encontrar cantos do tabuleiro de xadrez em nenhuma das imagens fornecidas.")
        return None

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    calibration_results = {
        "Matriz da camera": mtx,
        "Coeficientes de distorçao": dist,
        "Vetores de rotaçao": rvecs,
        "Vetores de translaçao": tvecs,
    }

    return calibration_results

def select_images():
    filetypes = [("image files", "*.jpg;*.png;*.jpeg")]
    filenames = filedialog.askopenfilenames(title="Selecione as imagens", filetypes=filetypes)
    return filenames

def save_calibration_results(calibration_results):
    if not calibration_results:
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    
    with open(file_path, "w") as file:
        for key, value in calibration_results.items():
            file.write(f"{key}:\n{value}\n\n")

def calibrate_and_save_camera():
    images = select_images()

    if not images:
        messagebox.showerror("Erro", "Nenhuma imagem selecionada.")
        return

    calibration_results = calibrate_camera(images)

    if not calibration_results:
        messagebox.showerror("Erro", "Erro: Não foi possível encontrar cantos do tabuleiro de xadrez em nenhuma das imagens fornecidas.")
        return

    save_calibration_results(calibration_results)
    messagebox.showinfo("Sucesso", "A calibração foi concluída com sucesso e os resultados foram salvos.")

if __name__ == "__main__":
    calibrate_and_save_camera()
