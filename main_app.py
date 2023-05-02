import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from  import calibrate_and_save_camera
from view_calibrated import view_calibrated_cameras
from view_undistorted import view_undistorted_camera, view_undistorted_live

width = 800
height = 500

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

def create_button_with_icon(parent, text, icon_path, command):
    button = ttk.Button(parent, text=text, command=command, padding=(5, 5, 5, 5), width=30)
    icon = Image.open(icon_path)
    icon = icon.resize((32, 32), Image.ANTIALIAS)
    button_icon = ImageTk.PhotoImage(icon)
    button.config(image=button_icon, compound=tk.TOP)
    button.image = button_icon
    return button

main_app = tk.Tk()
main_app.title("SAFEMAC")

center_window(main_app, width, height)

style = ttk.Style()
style.configure("Blue.TFrame", background="#0077be")
style.configure("TButton", font=("Arial", 12))

safemac_label = ttk.Label(main_app, text="SAFEMAC", font=("Arial", 24, "bold"))
safemac_label.pack(anchor=tk.NW, padx=(600,0), pady=(50,0))

frame = ttk.Frame(main_app, style="Blue.TFrame", height=height//2)
frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=5, pady=(45,5))

principal_label = ttk.Label(frame, text="PRINCIPAL", font=("Arial", 24, "bold"), background="#0077be", foreground="white")
principal_label.grid(row=0, column=0, pady=(20, 0))

#distribuir o espaco disponivel uniformemente entre as colunas e linhas
for col in range(2):
    frame.columnconfigure(col, weight=1)

for row in range(3):
    frame.rowconfigure(row, weight=1)

calibrate_button = create_button_with_icon(frame, "Calibrar Câmera", "icon_path/camera.png", calibrate_and_save_camera)
calibrate_button.grid(row=1, column=0, padx=15, pady=(25,10))

view_button = create_button_with_icon(frame, "Visualizar Câmeras Calibradas", "./icon_path/files.png", view_calibrated_cameras)
view_button.grid(row=1, column=1, padx=15, pady=(25,10))

view_undistorted_button = create_button_with_icon(frame, "Visualizar Imagem Corrigida", "./icon_path/image.png", view_undistorted_camera)
view_undistorted_button.grid(row=2, column=0, padx=15, pady=10)

view_undistorted_live_button = create_button_with_icon(frame, "Visualizar Câmeras em Tempo Real", "./icon_path/live.png", view_undistorted_live)
view_undistorted_live_button.grid(row=2, column=1, padx=15, pady=10)

exit_button = create_button_with_icon(frame, "Sair", "./icon_path/logout.png", main_app.quit)
exit_button.grid(row=3, column=0, columnspan=2, pady=10)

main_app.mainloop()