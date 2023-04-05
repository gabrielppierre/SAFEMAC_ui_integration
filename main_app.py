import tkinter as tk
from calibrate_camera import calibrate_and_save_camera
from view_calibrated import view_calibrated_cameras

width = 400
height = 200

main_app = tk.Tk()
main_app.title("SAFEMAC")

main_app.geometry(f"{width}x{height}")

calibrate_button = tk.Button(main_app, text="Calibrar Câmera", command=calibrate_and_save_camera)
calibrate_button.pack(padx=10, pady=10)

view_button = tk.Button(main_app, text="Visualizar Câmeras Calibradas", command=view_calibrated_cameras)
view_button.pack(padx=10, pady=10)

main_app.mainloop()
