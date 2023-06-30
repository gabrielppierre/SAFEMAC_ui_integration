import sys
import os
import platform
from modules.camera_manager import CameraManager
import time
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from modules.system_infos import get_cpu_usage, get_ram_usage, get_fps #,get_temperature 

bh = 50
#importar a interface do usuário e os módulos e widgets
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "100" #corrigir problema para alta DPI e escala acima de 100%
widgets = None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setMinimumSize(1400, 800)
        
        #definir os widgets como globais
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        #cria um QTimer
        self.timer = QTimer()
        #conecta o sinal timeout do timer ao método update_system_info
        self.timer.timeout.connect(self.update_system_info)
        #inicia o timer
        self.timer.start(1000)

        self.camera_manager = CameraManager([widgets.lb_camera_1, widgets.lb_camera_2, widgets.lb_camera_3, 
                                             widgets.lb_camera_4, widgets.lb_camera_5, widgets.lb_camera_6])
        
        for i in range(len(self.camera_manager.cameras)):
            self.camera_manager.cameras[i].mousePressEvent = lambda event, i=i: self.camera_manager.maximize_camera(i)

        #conectar botões aos métodos do camera_manager
        widgets.btn_visu_2.clicked.connect(self.camera_manager.view_recordings)
        widgets.btn_add_camera_2.clicked.connect(self.camera_manager.add_camera_clicked)
        widgets.btn_recordings_2.clicked.connect(self.camera_manager.add_recordings)
        widgets.btn_init_rec_2.clicked.connect(self.camera_manager.start_recording)
        widgets.btn_stop_rec_2.clicked.connect(self.camera_manager.stop_recording)

        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        title = "SafeMac"
        description = "SafeMac - Construindo segurança, Proteção inteligente"
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        UIFunctions.uiDefinitions(self)

        #cliques nos botões
        #menus esquerdos
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_cameras.clicked.connect(self.buttonClick)
        widgets.btn_videos.clicked.connect(self.buttonClick)

        #caixa extra esquerda
        #def openCloseLeftBox():
           # UIFunctions.toggleLeftBox(self, False)
        #widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        #widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        #caixa extra direita
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

        #definir tema personalizado
        useCustomTheme = False
        themeFile = "themes\py_safemac_dark.qss"

        #if useCustomTheme:
            #UIFunctions.theme(self, themeFile, False)
            #AppFunctions.setThemeHack(self)

        #definir página inicial e selecionar menu
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        #adicionando imgs (logo e botoes)
        pixmap_logo = QPixmap("icon.png")
        pixmap_logo = pixmap_logo.scaled(50, 50, Qt.KeepAspectRatio)  #define o tamanho máximo da imagem como 55x55 pixels
        self.ui.label_logo.setPixmap(pixmap_logo)
        self.ui.label_logo.setAlignment(Qt.AlignCenter) 

        pixmap_select_imgs = QPixmap("images/images/img_cameras.jpg")
        pixmap_select_imgs = pixmap_select_imgs.scaled(bh, bh, Qt.KeepAspectRatio)
        self.ui.img_calibrate.setPixmap(pixmap_select_imgs)
        self.ui.img_calibrate.setAlignment(Qt.AlignCenter)

        pixmap_view_cameras = QPixmap("images/images/img_operario.jpg")
        pixmap_view_cameras = pixmap_view_cameras.scaled(bh, bh, Qt.KeepAspectRatio)
        self.ui.img_visualize.setPixmap(pixmap_view_cameras)
        self.ui.img_visualize.setAlignment(Qt.AlignCenter)

        # Conectar o sinal clicked do QPushButton "hide_confs_camera" ao método hide_confs_camera_clicked
        widgets.hide_configs_camera.clicked.connect(self.hide_confs_camera_clicked)

        grid_layout = self.ui.box_bottom.layout()

        # ajustar proporção
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnStretch(2, 1)
        

    def update_system_info(self):
        start_time = time.time()

        cpu = get_cpu_usage()
        ram = get_ram_usage()
        #temp = get_temperature() or 0
        fps = get_fps(100, start_time)

        self.ui.Qlabel_cpu_2.setText(f"{cpu:.2f}%")  
        self.ui.Qlabel_ram_2.setText(f"{ram:.2f}%") 
        #self.ui.Qlabel_temp_2.setText(f"{temp:.2f} C")
        self.ui.Qlabel_fps_2.setText(f"{fps:.2f}")
        self.ui.Qlabel_fps_2.setText(f"{fps:.2f}")

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        #mostrar página inicial
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #mostrar página de widgets

        #mostrar pagina de cameras
        if btnName == "btn_cameras":
            widgets.stackedWidget.setCurrentWidget(widgets.cameras) #definir página
            UIFunctions.resetStyle(self, btnName) #redefinir outros botões selecionados
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) #selecionar menu

        #mostrar pagina com planilhas de videos e calibracoes
        if btnName == "btn_videos":
            widgets.stackedWidget.setCurrentWidget(widgets.tabs) #definir página
            UIFunctions.resetStyle(self, btnName) #redefinir outros botões selecionados
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) #selecionar menu

        #mostrar as configurações de camera
        if btnName == "hide_configs_camera":
            self.hide_confs_camera_clicked()

        #abrir a pasta com os videos salvos
        if btnName == "btn_videos_2":
            UIFunctions.resetStyle(self, btnName) #redefinir outros botões selecionados
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) #selecionar menu
            os.startfile(os.getcwd())

    def hide_confs_camera_clicked(self):
        if self.ui.bottom_configs.isHidden():
            self.ui.bottom_configs.show()
            self.ui.hide_configs_camera.setText("Ocultar configurações da câmera")
        else:
            self.ui.bottom_configs.hide()
            self.ui.hide_configs_camera.setText("Mostrar configurações da câmera")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
