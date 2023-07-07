import sys
import os
import platform
import time
import cv2
from PyQt5.QtCore import QTimer
from modules.camera_manager import CameraManager
from modules.ui_main import Ui_MainWindow
from make_video import make_video
from modules.system_infos import get_cpu_usage, get_ram_usage, get_fps 

bh = 50
from modules import *
from widgets import *

#Configuracoes de ambiente para corrigir problemas com DPI e escalonamento
os.environ["QT_FONT_DPI"] = "96" 

#Declaracao de widget global
widgets = None

class MainWindow(QMainWindow, Ui_MainWindow):
    import sys
import os
import platform
import time

#Importacoes de bibliotecas externas
import cv2
from PyQt5.QtCore import QTimer

#Importacoes de modulos locais
from modules import *
from modules.camera_manager import CameraManager
from modules.ui_main import Ui_MainWindow
from modules.system_infos import get_cpu_usage, get_ram_usage, get_fps 
from make_video import make_video
from widgets import *

#Configuracao de ambiente para corrigir problemas com DPI e escalonamento
os.environ["QT_FONT_DPI"] = "96" 

#Configuracao inicial
widgets = None  #Declaracao de widget global

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setup_ui()
        self.setup_camera_manager()
        self.connect_buttons()
        self.setup_ui_appearance()
        self.setup_theme()
        self.setup_images()
        self.camera_counter = 1  # Inicia o contador de câmeras
        self.box_cameras_top = QFrame(self)  # Cria um frame para as câmeras
        self.grid_cameras_top = QGridLayout(self.box_cameras_top) # Cria um grid para as câmeras

    def setup_ui(self):
        #Definicoes iniciais de interface e widgets
        self.setMinimumSize(1400, 800)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        #Criacao do QTimer para atualizar as informacoes do sistema
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_system_info)
        self.timer.start(1000)  #Iniciando o timer

    def setup_camera_manager(self):
        #Configuracao do gerenciador de camera
        self.camera_manager = CameraManager([widgets.lb_camera_1], widgets.frame_26)

        #Associa os eventos de clique do mouse as cameras no gerenciador de camera
        for i in range(len(self.camera_manager.cameras)):
            self.camera_manager.cameras[i].mousePressEvent = lambda event, i=i: self.camera_manager.maximize_camera(i)

    def connect_buttons(self):
        #Conectando botoes aos metodos correspondentes
        widgets.btn_visualize.clicked.connect(self.show_cameras_page)
        widgets.hide_configs_camera.clicked.connect(self.toggle_bottom_configs)
        widgets.btn_visu.clicked.connect(self.camera_manager.view_recordings)
        widgets.btn_add_camera.clicked.connect(self.camera_manager.add_camera_clicked)
        widgets.btn_add_camera.clicked.connect(self.add_camera)
        widgets.btn_recordings.clicked.connect(self.camera_manager.add_recordings)
        widgets.btn_init_rec.clicked.connect(self.camera_manager.start_recording)
        widgets.btn_stop_rec.clicked.connect(self.camera_manager.stop_recording)
        widgets.btn_stop_visu.clicked.connect(self.camera_manager.stop_visu)
        widgets.btn_new_video.clicked.connect(self.open_image_selection_dialog)

    def add_camera(self):
        # cria um novo frame
        new_frame = QFrame(self.box_cameras_top)
        new_frame.setObjectName(f"tela_{len(self.camera_manager.cameras)+1}")
        new_frame.setMinimumSize(QSize(640, 480))
        new_frame.setStyleSheet(u"background-color: rgb(8, 8, 8);")
        new_frame.setFrameShape(QFrame.StyledPanel)
        new_frame.setFrameShadow(QFrame.Raised)
        
        # cria um novo label
        new_label = QLabel(new_frame)
        new_label.setGeometry(QRect(0, 0, 640, 480))
        new_label.setObjectName(f"lb_camera_{len(self.camera_manager.cameras)+1}")
        new_label.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        new_label.setAlignment(Qt.AlignCenter)
        
        # adiciona o frame ao grid
        row = len(self.camera_manager.cameras) // self.grid_cameras_top.columnCount()
        column = len(self.camera_manager.cameras) % self.grid_cameras_top.columnCount()
        self.grid_cameras_top.addWidget(new_frame, row, column)
        
        # adiciona o label ao gerenciador de cameras
        self.camera_manager.cameras.append(new_label)
        self.camera_manager.add_camera_clicked()




    def setup_ui_appearance(self):
        #Configuracoes de aparencia da UI
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        title = "SafeMac"
        description = "SafeMac - Construindo seguranca, Protecao inteligente"
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        UIFunctions.uiDefinitions(self)
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_cameras.clicked.connect(self.buttonClick)
        widgets.btn_videos.clicked.connect(self.buttonClick)

        #Funcoes para abrir e fechar as caixas de dialogo
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

    def setup_theme(self):
        #Configuracao do tema
        useCustomTheme = False
        themeFile = "themes\py_safemac_dark.qss"

        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)  #Aplica o tema personalizado
            AppFunctions.setThemeHack(self)  #Aplica correcoes para o tema

        #Define a pagina inicial e seleciona o menu
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def setup_images(self):
        bh = 60  #Tamanho das imagens dos botoes
        #Adiciona imagens (logo e botoes)
        self.add_image_to_label("icon.png", self.ui.label_logo, 55, 55)
        self.add_image_to_label("images/images/camera.png", self.ui.img_calibrate, bh, bh)
        self.add_image_to_label("images/images/live.png", self.ui.img_visualize, bh, bh)
        self.add_image_to_label("images/images/instructions.png", self.ui.img_instructions, bh, bh)

    def add_image_to_label(self, image_path, label, width, height):
        #Adiciona uma imagem a um QLabel, redimensionando-a para o tamanho especificado
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)


    def show_cameras_page(self):
        widgets.stackedWidget.setCurrentWidget(widgets.cameras)  #Muda para a pagina das cameras
        UIFunctions.resetStyle(self, "btn_cameras")
        widgets.btn_cameras.setStyleSheet(UIFunctions.selectMenu(widgets.btn_cameras.styleSheet()))

    def toggle_bottom_configs(self):
        #Mostra/esconde as configuracoes de camera
        if widgets.bottom_configs.isVisible():
            widgets.bottom_configs.hide()
            widgets.hide_configs_camera.setText("Mostrar")
        else:
            widgets.bottom_configs.show()
            widgets.hide_configs_camera.setText("Esconder")

    def open_image_selection_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")

        if file_dialog.exec_():
            image_files = file_dialog.selectedFiles()
            output_file, _ = QFileDialog.getSaveFileName(self, "Save Video", "", "Videos (*.mp4)")

            if image_files and output_file:
                image_folder = os.path.dirname(image_files[0])
                fps, _ = QInputDialog.getInt(self, "Frames per Second", "Enter the FPS for the video:", 30)

                make_video(image_folder, output_file, fps)

    def update_system_info(self):
        #Atualiza as informacoes de sistema mostradas na UI
        start_time = time.time()
        cpu = get_cpu_usage()
        ram = get_ram_usage()
        fps = get_fps(100, start_time)
        self.ui.Qlabel_cpu.setText(f"{cpu:.2f}%")  
        self.ui.Qlabel_ram.setText(f"{ram:.2f}%") 
        self.ui.Qlabel_fps.setText(f"{fps:.2f}")
        self.ui.Qlabel_fps.setText(f"{fps:.2f}")

    def buttonClick(self):
        #Controla a acao a ser executada quando cada botao eh clicado
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)  #Redefine o estilo do botao para o estado padrao
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  #Aplica o estilo de um botao selecionado

        if btnName == "btn_cameras":
            widgets.stackedWidget.setCurrentWidget(widgets.cameras)  #Muda a pagina atual para a pagina de cameras
            UIFunctions.resetStyle(self, btnName)  #Redefine o estilo do botao para o estado padrao
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  #Aplica o estilo de um botao selecionado

        if btnName == "btn_videos":
            widgets.stackedWidget.setCurrentWidget(widgets.tabs)  #Muda a pagina atual para a pagina de videos
            UIFunctions.resetStyle(self, btnName)  #Redefine o estilo do botao para o estado padrao
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  #Aplica o estilo de um botao selecionado

        print(f'Botao "{btnName}" pressionado!')

    #Tratamento do evento de redimensionamento
    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)  #Redimensiona os controles da janela conforme o evento de redimensionamento

    #Tratamento dos eventos de clique do mouse
    def mousePressEvent(self, event):
        #Define a posicao de arrasto da janela
        self.dragPos = event.globalPos()

        if event.buttons() == Qt.LeftButton:
            print('Clique do mouse: botao esquerdo')
        if event.buttons() == Qt.RightButton:
            print('Clique do mouse: botao direito')

if __name__ == "__main__":
    app = QApplication(sys.argv)  #Cria uma instancia de QApplication
    app.setWindowIcon(QIcon("icon.ico"))  #Define o icone da janela
    window = MainWindow()  #Cria uma instancia da janela principal
    sys.exit(app.exec_())  #Executa o loop de eventos da aplicacao e finaliza o programa quando a janela principal eh fechada
