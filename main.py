import sys
import os
import platform
from modules.camera_manager import CameraManager
from modules.ui_main import Ui_MainWindow
import time
import cv2
from PyQt5.QtCore import QTimer

from modules.system_infos import get_cpu_usage, get_ram_usage, get_temperature, get_fps

bh = 50

#importar a interface do usuário e os módulos e widgets
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" #corrigir problema para alta DPI e escala acima de 100%
widgets = None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

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

        self.camera_manager = CameraManager([widgets.lb_camera_7, widgets.lb_camera_8, widgets.lb_camera_9, 
                                             widgets.lb_camera_10, widgets.lb_camera_11, widgets.lb_camera_12], widgets.frame_14)
        
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
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        #caixa extra direita
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

        #definir tema personalizado
        useCustomTheme = False
        themeFile = "themes\py_safemac_dark.qss"

        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)

        #definir página inicial e selecionar menu
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        #adicionando imgs (logo e botoes)
        pixmap_logo = QPixmap("icon.png")
        pixmap_logo = pixmap_logo.scaled(55, 55, Qt.KeepAspectRatio)  #define o tamanho máximo da imagem como 55x55 pixels
        self.ui.label_logo.setPixmap(pixmap_logo)
        self.ui.label_logo.setAlignment(Qt.AlignCenter) 

        pixmap_select_imgs = QPixmap("images/images/camera.png")
        pixmap_select_imgs = pixmap_select_imgs.scaled(bh, bh, Qt.KeepAspectRatio)
        self.ui.label_select_images.setPixmap(pixmap_select_imgs)
        self.ui.label_select_images.setAlignment(Qt.AlignCenter)

        
        pixmap_view_cameras = QPixmap("images/images/live.png")
        pixmap_view_cameras = pixmap_view_cameras.scaled(bh, bh, Qt.KeepAspectRatio)
        self.ui.label_visu_cameras.setPixmap(pixmap_view_cameras)
        self.ui.label_visu_cameras.setAlignment(Qt.AlignCenter)

    def update_system_info(self):
        start_time = time.time()

        cpu = get_cpu_usage()
        ram = get_ram_usage()
        temp = get_temperature() or 0
        fps = get_fps(100, start_time)

        self.ui.Qlabel_cpu_2.setText(f"{cpu:.2f}%")  
        self.ui.Qlabel_ram_2.setText(f"{ram:.2f}%") 
        self.ui.Qlabel_temp_2.setText(f"{temp:.2f} C")
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

        #mostrar nova página
        if btnName == "btn_cameras":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) #definir página
            UIFunctions.resetStyle(self, btnName) #redefinir outros botões selecionados
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) #selecionar menu

        if btnName == "btn_save":
            print("Botão salvar clicado!")

        print(f'Botão "{btnName}" pressionado!')


    #eventos de redimensionamento
    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    #eventos de clique do mouse
    def mousePressEvent(self, event):
        #definir posição de arrasto da janela
        self.dragPos = event.globalPos()

        if event.buttons() == Qt.LeftButton:
            print('Clique do mouse: botão esquerdo')
        if event.buttons() == Qt.RightButton:
            print('Clique do mouse: botão direito')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())