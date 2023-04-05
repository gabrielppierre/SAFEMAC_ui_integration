import tkinter as tk
from tkinter import filedialog, messagebox

def view_calibrated_cameras():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    with open(file_path, "r") as file:
        calibration_results = file.read()

    messagebox.showinfo("Resultados da Calibração", calibration_results)
