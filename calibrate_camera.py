import cv2
import numpy as np
import glob
import tkinter as tk
from tkinter import filedialog, messagebox

def calibrate_camera(images):
    largura_tabuleiro = 9
    altura_tabuleiro = 6

    objp = np.zeros((altura_tabuleiro * largura_tabuleiro, 3), np.float32)
    objp[:, :2] = np.mgrid[0:largura_tabuleiro, 0:altura_tabuleiro].T.reshape(-1, 2)

    objpoints = []
    imgpoints = []

    for fname in images:
        img = cv2.imread(fname)
        
        if img is None:
            print(f"Erro ao ler a imagem: {fname}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (largura_tabuleiro, altura_tabuleiro), None)

        if ret:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    calibration_results = {
        "Matriz da camera": mtx,
        "Coeficientes de distorçao": dist,
        "Vetores de rotaçao": rvecs,
        "Vetores de translaçao": tvecs,
    }

    return calibration_results

def select_images():
    filetypes = [("Image files", "*.jpg;*.png;*.jpeg")]
    filenames = filedialog.askopenfilenames(title="Selecione as imagens", filetypes=filetypes)
    return filenames

def save_calibration_results(calibration_results):
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
    save_calibration_results(calibration_results)
