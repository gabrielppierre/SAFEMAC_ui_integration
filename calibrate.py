import cv2
import numpy as np
import glob
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def calibrate_camera(images):
    largura_tabuleiro = 9
    altura_tabuleiro = 6

    objp = np.zeros((altura_tabuleiro * largura_tabuleiro, 3), np.float32)
    objp[:, :2] = np.mgrid[0:largura_tabuleiro, 0:altura_tabuleiro].T.reshape(-1, 2)

    objpoints = []  #pontos 3D no espaço do mundo real
    imgpoints = []  #pontos 2D no plano da imagem

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, (largura_tabuleiro, altura_tabuleiro), None)
        if ret:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    return {
        "Matriz da câmera": mtx,
        "Coeficientes de distorção": dist,
        "Vetores de rotação": rvecs,
        "Vetores de translação": tvecs
    }

def select_images():
    file_path = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    return list(file_path)

def start_calibration():
    images = select_images()

    if not images:
        messagebox.showerror("Erro", "Nenhuma imagem selecionada.")
        return

    calibration_results = calibrate_camera(images)
    
    result_text.delete(1.0, tk.END)
    for key, value in calibration_results.items():
        result_text.insert(tk.END, f"{key}:\n{value}\n\n")

root = tk.Tk()
root.title("Calibração de Câmera")

select_button = tk.Button(root, text="Selecionar Imagens", command=start_calibration)
select_button.pack(padx=10, pady=10)

#area de texto para exibir resultados
result_text = tk.Text(root, wrap=tk.WORD, width=40, height=20)
result_text.pack(padx=10, pady=10)

root.mainloop()
