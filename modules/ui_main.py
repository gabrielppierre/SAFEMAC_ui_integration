# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainlErahC.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 698)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: yellow;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #ffff00;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #000033;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #000080;\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:"
                        "/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #0935B0; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #000099;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #0000FF;\n"
"	color: #C0C0C0;\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #000099;\n"
"}\n"
""
                        "#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #0935B0;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid #262680;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #000080;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #000099;\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: #0000FF;\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #000080;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: #0935B0\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
""
                        "	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	backgr"
                        "ound-color: #0935B0;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #000080;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #262680;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #0000FF ; }\n"
"#themeSettingsTopDetail { background-color: #0935B0; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #00004D; }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; "
                        "}\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: #0935B0;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
""
                        "	background-color: #0935B0;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-backgroun"
                        "d-color: #ffff00;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #ffff00;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    mar"
                        "gin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0935B0;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    widt"
                        "h: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #0935B0;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////"
                        "//////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #000099;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
""
                        "\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #ffff00;	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////"
                        "////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #ffff00;\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #0935B0;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #ffff00;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10"
                        "px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #0935B0;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #ffff00;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: #ffff00;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	bo"
                        "rder: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_5 = QLabel(self.topLogoInfo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 20, 441, 331))
        self.label_logo = QLabel(self.topLogoInfo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(0, 0, 61, 51))
        self.label_logo.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_cameras = QPushButton(self.topMenu)
        self.btn_cameras.setObjectName(u"btn_cameras")
        sizePolicy.setHeightForWidth(self.btn_cameras.sizePolicy().hasHeightForWidth())
        self.btn_cameras.setSizePolicy(sizePolicy)
        self.btn_cameras.setMinimumSize(QSize(0, 45))
        self.btn_cameras.setFont(font)
        self.btn_cameras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cameras.setLayoutDirection(Qt.LeftToRight)
        self.btn_cameras.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-camera.png);")

        self.verticalLayout_8.addWidget(self.btn_cameras)

        self.btn_videos = QPushButton(self.topMenu)
        self.btn_videos.setObjectName(u"btn_videos")
        sizePolicy.setHeightForWidth(self.btn_videos.sizePolicy().hasHeightForWidth())
        self.btn_videos.setSizePolicy(sizePolicy)
        self.btn_videos.setMinimumSize(QSize(0, 45))
        self.btn_videos.setFont(font)
        self.btn_videos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_videos.setLayoutDirection(Qt.LeftToRight)
        self.btn_videos.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-movie.png);")

        self.verticalLayout_8.addWidget(self.btn_videos)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-exit-to-app.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"")
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"background-color: ")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.verticalLayout_33 = QVBoxLayout(self.home)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.box_top = QFrame(self.frame)
        self.box_top.setObjectName(u"box_top")
        self.box_top.setMaximumSize(QSize(16777215, 120))
        self.box_top.setStyleSheet(u"")
        self.box_top.setFrameShape(QFrame.NoFrame)
        self.box_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.box_top)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.welcome_box = QFrame(self.box_top)
        self.welcome_box.setObjectName(u"welcome_box")
        self.welcome_box.setStyleSheet(u"background-color: none;")
        self.welcome_box.setFrameShape(QFrame.NoFrame)
        self.welcome_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.welcome_box)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label = QLabel(self.welcome_box)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(162, 162, 162);\n"
"font: 36pt \"Segoe UI Variable Small\";\n"
"background-color: none;\n"
"")

        self.verticalLayout_23.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.welcome_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(162, 162, 162);\n"
"font: 8pt \"Segoe UI Variable Small\";\n"
"background-color: none;")

        self.verticalLayout_23.addWidget(self.label_2)


        self.verticalLayout_22.addWidget(self.welcome_box)


        self.verticalLayout_21.addWidget(self.box_top)

        self.box_bottom = QFrame(self.frame)
        self.box_bottom.setObjectName(u"box_bottom")
        self.box_bottom.setStyleSheet(u"")
        self.box_bottom.setFrameShape(QFrame.StyledPanel)
        self.box_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.box_bottom)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.box_bottom)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bottom = QFrame(self.frame_2)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMaximumSize(QSize(16777215, 16777215))
        self.bottom.setStyleSheet(u"background-color: none;")
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cards_box = QFrame(self.bottom)
        self.cards_box.setObjectName(u"cards_box")
        self.cards_box.setMinimumSize(QSize(750, 350))
        self.cards_box.setMaximumSize(QSize(1000, 400))
        self.cards_box.setFrameShape(QFrame.StyledPanel)
        self.cards_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.cards_box)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.cards = QFrame(self.cards_box)
        self.cards.setObjectName(u"cards")
        self.cards.setMaximumSize(QSize(16777215, 800))
        self.cards.setStyleSheet(u"background-color: none;")
        self.cards.setFrameShape(QFrame.NoFrame)
        self.cards.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.cards)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.card_calibrate = QFrame(self.cards)
        self.card_calibrate.setObjectName(u"card_calibrate")
        self.card_calibrate.setMinimumSize(QSize(400, 300))
        self.card_calibrate.setMaximumSize(QSize(400, 350))
        self.card_calibrate.setStyleSheet(u"QFrame#card_calibrate{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.517, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 0, 102, 255), stop:1 rgba(0, 0, 255, 242));\n"
"	border-radius:7px;\n"
"	margin: 0px 50px 0 50px;\n"
"}")
        self.card_calibrate.setFrameShape(QFrame.NoFrame)
        self.card_calibrate.setFrameShadow(QFrame.Plain)
        self.card_calibrate.setLineWidth(1)
        self.card_calibrate.setMidLineWidth(0)
        self.verticalLayout_25 = QVBoxLayout(self.card_calibrate)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.image_box_calibrate = QFrame(self.card_calibrate)
        self.image_box_calibrate.setObjectName(u"image_box_calibrate")
        self.image_box_calibrate.setStyleSheet(u"")
        self.image_box_calibrate.setFrameShape(QFrame.StyledPanel)
        self.image_box_calibrate.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.image_box_calibrate)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_select_images = QLabel(self.image_box_calibrate)
        self.label_select_images.setObjectName(u"label_select_images")
        self.label_select_images.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.label_select_images)


        self.verticalLayout_25.addWidget(self.image_box_calibrate)

        self.frame_6 = QFrame(self.card_calibrate)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 160))
        self.frame_6.setStyleSheet(u"background-color: none;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 9pt \"Segoe UI Variable Small\";\n"
"")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.label_3)


        self.verticalLayout_25.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.card_calibrate)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.select_imgs = QPushButton(self.frame_7)
        self.select_imgs.setObjectName(u"select_imgs")
        self.select_imgs.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_imgs.setStyleSheet(u"QPushButton{\n"
"	font: 700 9pt \"Segoe UI Variable Small\";\n"
"	padding: 40px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 	stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	border: none;\n"
"	color: rgb(192, 192, 192);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}")

        self.verticalLayout_28.addWidget(self.select_imgs)


        self.verticalLayout_25.addWidget(self.frame_7)


        self.horizontalLayout_10.addWidget(self.card_calibrate)

        self.card_view = QFrame(self.cards)
        self.card_view.setObjectName(u"card_view")
        self.card_view.setMinimumSize(QSize(400, 300))
        self.card_view.setMaximumSize(QSize(400, 350))
        self.card_view.setStyleSheet(u"QFrame#card_view{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.517, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 0, 102, 255), stop:1 rgba(0, 0, 255, 242));\n"
"	border-radius:7px;\n"
"	margin: 0px 50px 0 50px;\n"
"}")
        self.card_view.setFrameShape(QFrame.StyledPanel)
        self.card_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.card_view)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.image_view_cameras = QFrame(self.card_view)
        self.image_view_cameras.setObjectName(u"image_view_cameras")
        self.image_view_cameras.setStyleSheet(u"")
        self.image_view_cameras.setFrameShape(QFrame.StyledPanel)
        self.image_view_cameras.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.image_view_cameras)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_visu_cameras = QLabel(self.image_view_cameras)
        self.label_visu_cameras.setObjectName(u"label_visu_cameras")

        self.verticalLayout_30.addWidget(self.label_visu_cameras)


        self.verticalLayout_29.addWidget(self.image_view_cameras)

        self.frame_9 = QFrame(self.card_view)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 160))
        self.frame_9.setStyleSheet(u"background-color: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_9)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 9pt \"Segoe UI Variable Small\";\n"
"")
        self.label_4.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.label_4)


        self.verticalLayout_29.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.card_view)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_10)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.view_cameras = QPushButton(self.frame_10)
        self.view_cameras.setObjectName(u"view_cameras")
        self.view_cameras.setCursor(QCursor(Qt.PointingHandCursor))
        self.view_cameras.setStyleSheet(u"QPushButton{\n"
"	font: 700 9pt \"Segoe UI Variable Small\";\n"
"	padding: 40px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 	stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	border: none;\n"
"	color: rgb(192, 192, 192);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}")

        self.verticalLayout_32.addWidget(self.view_cameras, 0, Qt.AlignVCenter)


        self.verticalLayout_29.addWidget(self.frame_10)


        self.horizontalLayout_10.addWidget(self.card_view)


        self.horizontalLayout_8.addWidget(self.cards)


        self.horizontalLayout_7.addWidget(self.cards_box, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.bottom)


        self.verticalLayout_24.addWidget(self.frame_2)


        self.verticalLayout_21.addWidget(self.box_bottom)


        self.verticalLayout_33.addWidget(self.frame)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_12 = QFrame(self.new_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_12)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_14)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.box_cameras_geral_2 = QFrame(self.frame_14)
        self.box_cameras_geral_2.setObjectName(u"box_cameras_geral_2")
        self.box_cameras_geral_2.setMinimumSize(QSize(0, 400))
        self.box_cameras_geral_2.setStyleSheet(u"color: rgb(192, 192, 192);")
        self.box_cameras_geral_2.setFrameShape(QFrame.NoFrame)
        self.box_cameras_geral_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.box_cameras_geral_2)
        self.verticalLayout_45.setSpacing(2)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.box_cameras_top_2 = QFrame(self.box_cameras_geral_2)
        self.box_cameras_top_2.setObjectName(u"box_cameras_top_2")
        self.box_cameras_top_2.setFrameShape(QFrame.StyledPanel)
        self.box_cameras_top_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.box_cameras_top_2)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tela_7 = QFrame(self.box_cameras_top_2)
        self.tela_7.setObjectName(u"tela_7")
        self.tela_7.setMinimumSize(QSize(0, 0))
        self.tela_7.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tela_7.setFrameShape(QFrame.NoFrame)
        self.tela_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.tela_7)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lb_camera_7 = QLabel(self.tela_7)
        self.lb_camera_7.setObjectName(u"lb_camera_7")

        self.verticalLayout_46.addWidget(self.lb_camera_7)


        self.gridLayout_4.addWidget(self.tela_7, 0, 0, 1, 1)

        self.tela_8 = QFrame(self.box_cameras_top_2)
        self.tela_8.setObjectName(u"tela_8")
        self.tela_8.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tela_8.setFrameShape(QFrame.NoFrame)
        self.tela_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.tela_8)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.lb_camera_8 = QLabel(self.tela_8)
        self.lb_camera_8.setObjectName(u"lb_camera_8")

        self.verticalLayout_47.addWidget(self.lb_camera_8)


        self.gridLayout_4.addWidget(self.tela_8, 0, 1, 1, 1)

        self.tela_9 = QFrame(self.box_cameras_top_2)
        self.tela_9.setObjectName(u"tela_9")
        self.tela_9.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tela_9.setFrameShape(QFrame.NoFrame)
        self.tela_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.tela_9)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.lb_camera_9 = QLabel(self.tela_9)
        self.lb_camera_9.setObjectName(u"lb_camera_9")

        self.verticalLayout_48.addWidget(self.lb_camera_9)


        self.gridLayout_4.addWidget(self.tela_9, 0, 2, 1, 1)

        self.tela_10 = QFrame(self.box_cameras_top_2)
        self.tela_10.setObjectName(u"tela_10")
        self.tela_10.setMinimumSize(QSize(0, 0))
        self.tela_10.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tela_10.setFrameShape(QFrame.NoFrame)
        self.tela_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.tela_10)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.lb_camera_10 = QLabel(self.tela_10)
        self.lb_camera_10.setObjectName(u"lb_camera_10")

        self.verticalLayout_49.addWidget(self.lb_camera_10)


        self.gridLayout_4.addWidget(self.tela_10, 1, 0, 1, 1)

        self.tela_11 = QFrame(self.box_cameras_top_2)
        self.tela_11.setObjectName(u"tela_11")
        self.tela_11.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tela_11.setFrameShape(QFrame.NoFrame)
        self.tela_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.tela_11)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.lb_camera_11 = QLabel(self.tela_11)
        self.lb_camera_11.setObjectName(u"lb_camera_11")

        self.verticalLayout_50.addWidget(self.lb_camera_11)


        self.gridLayout_4.addWidget(self.tela_11, 1, 1, 1, 1)

        self.tela_12 = QFrame(self.box_cameras_top_2)
        self.tela_12.setObjectName(u"tela_12")
        self.tela_12.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tela_12.setFrameShape(QFrame.NoFrame)
        self.tela_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.tela_12)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.lb_camera_12 = QLabel(self.tela_12)
        self.lb_camera_12.setObjectName(u"lb_camera_12")

        self.verticalLayout_51.addWidget(self.lb_camera_12)


        self.gridLayout_4.addWidget(self.tela_12, 1, 2, 1, 1)


        self.verticalLayout_45.addWidget(self.box_cameras_top_2)

        self.reconstruction_tela_2 = QFrame(self.box_cameras_geral_2)
        self.reconstruction_tela_2.setObjectName(u"reconstruction_tela_2")
        self.reconstruction_tela_2.setMinimumSize(QSize(350, 120))
        self.reconstruction_tela_2.setMaximumSize(QSize(16777215, 200))
        self.reconstruction_tela_2.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.reconstruction_tela_2.setFrameShape(QFrame.NoFrame)
        self.reconstruction_tela_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.reconstruction_tela_2)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.virtualized_image_2 = QLabel(self.reconstruction_tela_2)
        self.virtualized_image_2.setObjectName(u"virtualized_image_2")

        self.verticalLayout_52.addWidget(self.virtualized_image_2)


        self.verticalLayout_45.addWidget(self.reconstruction_tela_2)


        self.verticalLayout_44.addWidget(self.box_cameras_geral_2)

        self.painel_bottom_2 = QFrame(self.frame_14)
        self.painel_bottom_2.setObjectName(u"painel_bottom_2")
        self.painel_bottom_2.setMinimumSize(QSize(0, 160))
        self.painel_bottom_2.setMaximumSize(QSize(16777215, 200))
        self.painel_bottom_2.setStyleSheet(u"")
        self.painel_bottom_2.setFrameShape(QFrame.NoFrame)
        self.painel_bottom_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.painel_bottom_2)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.box_config_cameras_2 = QFrame(self.painel_bottom_2)
        self.box_config_cameras_2.setObjectName(u"box_config_cameras_2")
        self.box_config_cameras_2.setMaximumSize(QSize(400, 16777215))
        self.box_config_cameras_2.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";")
        self.box_config_cameras_2.setFrameShape(QFrame.NoFrame)
        self.box_config_cameras_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.box_config_cameras_2)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(3, 0, 3, 1)
        self.frame_15 = QFrame(self.box_config_cameras_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_25.setSpacing(3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_39 = QLabel(self.frame_16)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: rgb(192, 192, 192);")

        self.horizontalLayout_25.addWidget(self.label_39)


        self.horizontalLayout_24.addWidget(self.frame_16)

        self.btn_add_camera_2 = QPushButton(self.frame_15)
        self.btn_add_camera_2.setObjectName(u"btn_add_camera_2")
        self.btn_add_camera_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_camera_2.setStyleSheet(u"QPushButton{\n"
"	padding: 4px;\n"
"	border: none;\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.horizontalLayout_24.addWidget(self.btn_add_camera_2)

        self.btn_recordings_2 = QPushButton(self.frame_15)
        self.btn_recordings_2.setObjectName(u"btn_recordings_2")
        self.btn_recordings_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recordings_2.setStyleSheet(u"QPushButton{\n"
"	padding: 4px;\n"
"	border: none;\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.horizontalLayout_24.addWidget(self.btn_recordings_2)


        self.verticalLayout_53.addWidget(self.frame_15)

        self.gb_roi_2 = QGroupBox(self.box_config_cameras_2)
        self.gb_roi_2.setObjectName(u"gb_roi_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gb_roi_2.sizePolicy().hasHeightForWidth())
        self.gb_roi_2.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Small"])
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.gb_roi_2.setFont(font3)
        self.gb_roi_2.setMouseTracking(False)
        self.gb_roi_2.setTabletTracking(False)
        self.gb_roi_2.setFocusPolicy(Qt.NoFocus)
        self.gb_roi_2.setLayoutDirection(Qt.LeftToRight)
        self.gb_roi_2.setStyleSheet(u"color: rgb(192, 192, 192);")
        self.gb_roi_2.setFlat(False)
        self.gridLayout_15 = QGridLayout(self.gb_roi_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, 5, -1, 8)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_40 = QLabel(self.gb_roi_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 20))
        self.label_40.setStyleSheet(u"margin: 0px 0px 2px 0px;")

        self.gridLayout_10.addWidget(self.label_40, 4, 1, 1, 1)

        self.label_41 = QLabel(self.gb_roi_2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_10.addWidget(self.label_41, 3, 0, 1, 1)

        self.label_42 = QLabel(self.gb_roi_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_10.addWidget(self.label_42, 3, 2, 1, 1)

        self.label_43 = QLabel(self.gb_roi_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_10.addWidget(self.label_43, 1, 2, 1, 1)

        self.ROI_H_2 = QSpinBox(self.gb_roi_2)
        self.ROI_H_2.setObjectName(u"ROI_H_2")
        self.ROI_H_2.setMinimumSize(QSize(0, 20))
        self.ROI_H_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_H_2.setMaximum(2000)
        self.ROI_H_2.setValue(1000)

        self.gridLayout_10.addWidget(self.ROI_H_2, 3, 3, 1, 1)

        self.btn_roi_set_2 = QPushButton(self.gb_roi_2)
        self.btn_roi_set_2.setObjectName(u"btn_roi_set_2")
        self.btn_roi_set_2.setMinimumSize(QSize(0, 20))
        self.btn_roi_set_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_roi_set_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.gridLayout_10.addWidget(self.btn_roi_set_2, 4, 3, 1, 1)

        self.ckb_roi_2 = QCheckBox(self.gb_roi_2)
        self.ckb_roi_2.setObjectName(u"ckb_roi_2")
        self.ckb_roi_2.setMinimumSize(QSize(0, 20))

        self.gridLayout_10.addWidget(self.ckb_roi_2, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.ROI_X_2 = QSpinBox(self.gb_roi_2)
        self.ROI_X_2.setObjectName(u"ROI_X_2")
        self.ROI_X_2.setMinimumSize(QSize(0, 20))
        self.ROI_X_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_X_2.setMinimum(0)
        self.ROI_X_2.setMaximum(1000)
        self.ROI_X_2.setValue(20)

        self.gridLayout_10.addWidget(self.ROI_X_2, 1, 1, 1, 1)

        self.label_44 = QLabel(self.gb_roi_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_10.addWidget(self.label_44, 1, 0, 1, 1)

        self.ROI_Y_2 = QSpinBox(self.gb_roi_2)
        self.ROI_Y_2.setObjectName(u"ROI_Y_2")
        self.ROI_Y_2.setMinimumSize(QSize(0, 20))
        self.ROI_Y_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_Y_2.setMinimum(0)
        self.ROI_Y_2.setMaximum(1000)
        self.ROI_Y_2.setValue(20)

        self.gridLayout_10.addWidget(self.ROI_Y_2, 1, 3, 1, 1)

        self.ROI_W_2 = QSpinBox(self.gb_roi_2)
        self.ROI_W_2.setObjectName(u"ROI_W_2")
        self.ROI_W_2.setMinimumSize(QSize(0, 20))
        self.ROI_W_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_W_2.setMaximum(2000)
        self.ROI_W_2.setValue(1000)

        self.gridLayout_10.addWidget(self.ROI_W_2, 3, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.verticalLayout_53.addWidget(self.gb_roi_2)


        self.horizontalLayout_23.addWidget(self.box_config_cameras_2)

        self.frame_17 = QFrame(self.painel_bottom_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 9, 0, 0)
        self.groupBox_visu_2 = QGroupBox(self.frame_17)
        self.groupBox_visu_2.setObjectName(u"groupBox_visu_2")
        self.groupBox_visu_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_visu_2.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";\n"
"color: rgb(192, 192, 192);\n"
"")
        self.gridLayout_5 = QGridLayout(self.groupBox_visu_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(2)
        self.gridLayout_5.setContentsMargins(4, 1, 4, 1)
        self.btn_visu_2 = QPushButton(self.groupBox_visu_2)
        self.btn_visu_2.setObjectName(u"btn_visu_2")
        self.btn_visu_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visu_2.setStyleSheet(u"QPushButton{\n"
"	padding: 4px;\n"
"	border: none;\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.gridLayout_5.addWidget(self.btn_visu_2, 0, 0, 1, 1)

        self.btn_stop_visu_2 = QPushButton(self.groupBox_visu_2)
        self.btn_stop_visu_2.setObjectName(u"btn_stop_visu_2")
        self.btn_stop_visu_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_visu_2.setStyleSheet(u"QPushButton{\n"
"	padding: 4px;\n"
"	border: none;\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.gridLayout_5.addWidget(self.btn_stop_visu_2, 1, 0, 1, 1)

        self.btn_init_rec_2 = QPushButton(self.groupBox_visu_2)
        self.btn_init_rec_2.setObjectName(u"btn_init_rec_2")
        self.btn_init_rec_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_init_rec_2.setStyleSheet(u"QPushButton{\n"
"	padding: 4px;\n"
"	border: none;\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.gridLayout_5.addWidget(self.btn_init_rec_2, 2, 0, 1, 1)

        self.btn_stop_rec_2 = QPushButton(self.groupBox_visu_2)
        self.btn_stop_rec_2.setObjectName(u"btn_stop_rec_2")
        self.btn_stop_rec_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_rec_2.setStyleSheet(u"QPushButton{\n"
"	padding: 4px;\n"
"	border: none;\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.gridLayout_5.addWidget(self.btn_stop_rec_2, 3, 0, 1, 1)


        self.horizontalLayout_26.addWidget(self.groupBox_visu_2)


        self.horizontalLayout_23.addWidget(self.frame_17)

        self.box_HSV_configs_2 = QFrame(self.painel_bottom_2)
        self.box_HSV_configs_2.setObjectName(u"box_HSV_configs_2")
        self.box_HSV_configs_2.setMaximumSize(QSize(400, 16777215))
        self.box_HSV_configs_2.setStyleSheet(u"\n"
"QSlider::handle:hover {\n"
"	background-color: rgb(255, 255, 0);\n"
"}")
        self.box_HSV_configs_2.setFrameShape(QFrame.StyledPanel)
        self.box_HSV_configs_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.box_HSV_configs_2)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 9, 0, 0)
        self.groupBox_7 = QGroupBox(self.box_HSV_configs_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(228, 100))
        self.groupBox_7.setAutoFillBackground(False)
        self.groupBox_7.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";\n"
"color: rgb(192, 192, 192);")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.verticalLayout_55 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_55.setSpacing(4)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.titles_hsv_2 = QFrame(self.groupBox_7)
        self.titles_hsv_2.setObjectName(u"titles_hsv_2")
        self.titles_hsv_2.setMinimumSize(QSize(0, 23))
        self.titles_hsv_2.setMaximumSize(QSize(16777215, 40))
        self.titles_hsv_2.setStyleSheet(u"")
        self.titles_hsv_2.setFrameShape(QFrame.NoFrame)
        self.titles_hsv_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.titles_hsv_2)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(9, 5, 9, 0)
        self.left_title_2 = QLabel(self.titles_hsv_2)
        self.left_title_2.setObjectName(u"left_title_2")
        self.left_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.left_title_2)

        self.right_title_2 = QLabel(self.titles_hsv_2)
        self.right_title_2.setObjectName(u"right_title_2")
        self.right_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.right_title_2)


        self.verticalLayout_55.addWidget(self.titles_hsv_2)

        self.content_box_2 = QFrame(self.groupBox_7)
        self.content_box_2.setObjectName(u"content_box_2")
        self.content_box_2.setMinimumSize(QSize(0, 0))
        self.content_box_2.setFrameShape(QFrame.NoFrame)
        self.content_box_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.content_box_2)
        self.horizontalLayout_28.setSpacing(4)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 5)
        self.frame_18 = QFrame(self.content_box_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(135, 16777215))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_18)
        self.verticalLayout_56.setSpacing(2)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(1, 1, 1, 1)
        self.box_h_max_2 = QFrame(self.frame_18)
        self.box_h_max_2.setObjectName(u"box_h_max_2")
        self.box_h_max_2.setStyleSheet(u"")
        self.box_h_max_2.setFrameShape(QFrame.NoFrame)
        self.box_h_max_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.box_h_max_2)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_45 = QLabel(self.box_h_max_2)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_29.addWidget(self.label_45)

        self.horizontalSlider_7 = QSlider(self.box_h_max_2)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        self.horizontalSlider_7.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_7.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_7.setStyleSheet(u"QSlider::handle {\n"
"    height: 10px; /* Largura do manipulador do slider */\n"
"}")
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.horizontalLayout_29.addWidget(self.horizontalSlider_7)

        self.label_46 = QLabel(self.box_h_max_2)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_29.addWidget(self.label_46)


        self.verticalLayout_56.addWidget(self.box_h_max_2)

        self.box_s_max_2 = QFrame(self.frame_18)
        self.box_s_max_2.setObjectName(u"box_s_max_2")
        self.box_s_max_2.setStyleSheet(u"")
        self.box_s_max_2.setFrameShape(QFrame.NoFrame)
        self.box_s_max_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.box_s_max_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_47 = QLabel(self.box_s_max_2)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_30.addWidget(self.label_47)

        self.horizontalSlider_8 = QSlider(self.box_s_max_2)
        self.horizontalSlider_8.setObjectName(u"horizontalSlider_8")
        self.horizontalSlider_8.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_8.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_8.setStyleSheet(u"")
        self.horizontalSlider_8.setOrientation(Qt.Horizontal)

        self.horizontalLayout_30.addWidget(self.horizontalSlider_8)

        self.label_48 = QLabel(self.box_s_max_2)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_30.addWidget(self.label_48)


        self.verticalLayout_56.addWidget(self.box_s_max_2)

        self.box_v_max_2 = QFrame(self.frame_18)
        self.box_v_max_2.setObjectName(u"box_v_max_2")
        self.box_v_max_2.setStyleSheet(u"")
        self.box_v_max_2.setFrameShape(QFrame.NoFrame)
        self.box_v_max_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.box_v_max_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_49 = QLabel(self.box_v_max_2)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_31.addWidget(self.label_49)

        self.horizontalSlider_9 = QSlider(self.box_v_max_2)
        self.horizontalSlider_9.setObjectName(u"horizontalSlider_9")
        self.horizontalSlider_9.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_9.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_9.setOrientation(Qt.Horizontal)

        self.horizontalLayout_31.addWidget(self.horizontalSlider_9)

        self.label_50 = QLabel(self.box_v_max_2)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_31.addWidget(self.label_50)


        self.verticalLayout_56.addWidget(self.box_v_max_2)


        self.horizontalLayout_28.addWidget(self.frame_18)

        self.box_right_2 = QFrame(self.content_box_2)
        self.box_right_2.setObjectName(u"box_right_2")
        self.box_right_2.setMaximumSize(QSize(135, 16777215))
        self.box_right_2.setStyleSheet(u"")
        self.box_right_2.setFrameShape(QFrame.NoFrame)
        self.box_right_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.box_right_2)
        self.verticalLayout_57.setSpacing(2)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(1, 1, 1, 1)
        self.box_h_min_2 = QFrame(self.box_right_2)
        self.box_h_min_2.setObjectName(u"box_h_min_2")
        self.box_h_min_2.setStyleSheet(u"")
        self.box_h_min_2.setFrameShape(QFrame.NoFrame)
        self.box_h_min_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.box_h_min_2)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_51 = QLabel(self.box_h_min_2)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_32.addWidget(self.label_51)

        self.horizontalSlider_10 = QSlider(self.box_h_min_2)
        self.horizontalSlider_10.setObjectName(u"horizontalSlider_10")
        self.horizontalSlider_10.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_10.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_10.setOrientation(Qt.Horizontal)

        self.horizontalLayout_32.addWidget(self.horizontalSlider_10)

        self.label_52 = QLabel(self.box_h_min_2)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_32.addWidget(self.label_52)


        self.verticalLayout_57.addWidget(self.box_h_min_2)

        self.box_s_min_2 = QFrame(self.box_right_2)
        self.box_s_min_2.setObjectName(u"box_s_min_2")
        self.box_s_min_2.setStyleSheet(u"")
        self.box_s_min_2.setFrameShape(QFrame.NoFrame)
        self.box_s_min_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.box_s_min_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_53 = QLabel(self.box_s_min_2)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_33.addWidget(self.label_53)

        self.horizontalSlider_11 = QSlider(self.box_s_min_2)
        self.horizontalSlider_11.setObjectName(u"horizontalSlider_11")
        self.horizontalSlider_11.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_11.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_11.setOrientation(Qt.Horizontal)

        self.horizontalLayout_33.addWidget(self.horizontalSlider_11)

        self.label_54 = QLabel(self.box_s_min_2)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_33.addWidget(self.label_54)


        self.verticalLayout_57.addWidget(self.box_s_min_2)

        self.box_v_min_2 = QFrame(self.box_right_2)
        self.box_v_min_2.setObjectName(u"box_v_min_2")
        self.box_v_min_2.setStyleSheet(u"")
        self.box_v_min_2.setFrameShape(QFrame.NoFrame)
        self.box_v_min_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.box_v_min_2)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_55 = QLabel(self.box_v_min_2)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_34.addWidget(self.label_55)

        self.horizontalSlider_12 = QSlider(self.box_v_min_2)
        self.horizontalSlider_12.setObjectName(u"horizontalSlider_12")
        self.horizontalSlider_12.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_12.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_12.setOrientation(Qt.Horizontal)

        self.horizontalLayout_34.addWidget(self.horizontalSlider_12)

        self.label_56 = QLabel(self.box_v_min_2)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_34.addWidget(self.label_56)


        self.verticalLayout_57.addWidget(self.box_v_min_2)


        self.horizontalLayout_28.addWidget(self.box_right_2)


        self.verticalLayout_55.addWidget(self.content_box_2)


        self.verticalLayout_54.addWidget(self.groupBox_7)


        self.horizontalLayout_23.addWidget(self.box_HSV_configs_2)

        self.infor_system_2 = QFrame(self.painel_bottom_2)
        self.infor_system_2.setObjectName(u"infor_system_2")
        self.infor_system_2.setMaximumSize(QSize(400, 16777215))
        self.infor_system_2.setFrameShape(QFrame.StyledPanel)
        self.infor_system_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.infor_system_2)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.infor_system_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_19)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.system_infos_2 = QFrame(self.frame_19)
        self.system_infos_2.setObjectName(u"system_infos_2")
        self.system_infos_2.setStyleSheet(u"color: rgb(192, 192, 192);")
        self.system_infos_2.setFrameShape(QFrame.StyledPanel)
        self.system_infos_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.system_infos_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_57 = QLabel(self.system_infos_2)
        self.label_57.setObjectName(u"label_57")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Variable Small"])
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_57.setFont(font4)
        self.label_57.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_57, 0, 4, 1, 1)

        self.label_58 = QLabel(self.system_infos_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font4)
        self.label_58.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_58, 0, 1, 1, 1)

        self.Qlabel_cpu_2 = QLabel(self.system_infos_2)
        self.Qlabel_cpu_2.setObjectName(u"Qlabel_cpu_2")
        self.Qlabel_cpu_2.setFont(font4)
        self.Qlabel_cpu_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.Qlabel_cpu_2, 1, 1, 1, 1)

        self.label_59 = QLabel(self.system_infos_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font4)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_59, 0, 3, 1, 1)

        self.Qlabel_fps_2 = QLabel(self.system_infos_2)
        self.Qlabel_fps_2.setObjectName(u"Qlabel_fps_2")
        self.Qlabel_fps_2.setFont(font4)
        self.Qlabel_fps_2.setStyleSheet(u"color: rgb(237, 85, 59);")
        self.Qlabel_fps_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.Qlabel_fps_2, 1, 0, 1, 1)

        self.label_60 = QLabel(self.system_infos_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font4)
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_60, 0, 0, 1, 1)

        self.Qlabel_ram_2 = QLabel(self.system_infos_2)
        self.Qlabel_ram_2.setObjectName(u"Qlabel_ram_2")
        self.Qlabel_ram_2.setFont(font4)
        self.Qlabel_ram_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.Qlabel_ram_2, 1, 3, 1, 1)

        self.Qlabel_temp_2 = QLabel(self.system_infos_2)
        self.Qlabel_temp_2.setObjectName(u"Qlabel_temp_2")
        self.Qlabel_temp_2.setFont(font4)
        self.Qlabel_temp_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.Qlabel_temp_2, 1, 4, 1, 1)


        self.verticalLayout_59.addWidget(self.system_infos_2)

        self.alarm_box_2 = QFrame(self.frame_19)
        self.alarm_box_2.setObjectName(u"alarm_box_2")
        self.alarm_box_2.setFrameShape(QFrame.StyledPanel)
        self.alarm_box_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.alarm_box_2)
        self.horizontalLayout_35.setSpacing(5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Qlabel_greenlight_2 = QLabel(self.alarm_box_2)
        self.Qlabel_greenlight_2.setObjectName(u"Qlabel_greenlight_2")
        self.Qlabel_greenlight_2.setFont(font4)
        self.Qlabel_greenlight_2.setStyleSheet(u"background-color: rgb(34, 139, 34);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.Qlabel_greenlight_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.Qlabel_greenlight_2)


        self.verticalLayout_59.addWidget(self.alarm_box_2)


        self.verticalLayout_58.addWidget(self.frame_19)


        self.horizontalLayout_23.addWidget(self.infor_system_2)


        self.verticalLayout_44.addWidget(self.painel_bottom_2)


        self.verticalLayout_60.addWidget(self.frame_14)


        self.verticalLayout_20.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SafeMac</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/images/images/icon.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText("")
        self.label_logo.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Esconder", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.btn_cameras.setText(QCoreApplication.translate("MainWindow", u"C\u00e2meras", None))
        self.btn_videos.setText(QCoreApplication.translate("MainWindow", u"Grava\u00e7\u00f5es", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"SafeMac - Construindo seguran\u00e7a, Prote\u00e7\u00e3o Inteligente", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Bem vindo</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Adicione pelo menos uma c\u00e2mera antes de monitorar o sistema pela primeira vez.</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.image_box_calibrate.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_select_images.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; color:#c0c0c0;\">Selecione ao menos 15 imagens de boa qualidade para calibrar a c\u00e2mera. Lembre-se de repetir a calibra\u00e7\u00e3o sempre que a c\u00e2mera for reposicionada ou se houver mudan\u00e7as significativas no ambiente, como altera\u00e7\u00f5es dr\u00e1sticas na ilumina\u00e7\u00e3o.</span></p></body></html>", None))
        self.select_imgs.setText(QCoreApplication.translate("MainWindow", u"Selecionar Imagens", None))
        self.label_visu_cameras.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; color:#c0c0c0;\">Utilize este bot\u00e3o para visualizar as c\u00e2meras j\u00e1 calibradas, exibindo em tempo real a representa\u00e7\u00e3o virtual do cen\u00e1rio. Esta funcionalidade permite conferir a precis\u00e3o da calibra\u00e7\u00e3o e ajustar se necess\u00e1rio.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.view_cameras.setText(QCoreApplication.translate("MainWindow", u"Visualizar c\u00e2meras", None))
        self.lb_camera_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">camera 1</p></body></html>", None))
        self.lb_camera_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">camera 2</p></body></html>", None))
        self.lb_camera_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">camera 3</p></body></html>", None))
        self.lb_camera_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">camera 5</p></body></html>", None))
        self.lb_camera_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">camera 4</p></body></html>", None))
        self.lb_camera_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">camera 6</p></body></html>", None))
        self.virtualized_image_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">tela \u00e1reas de interesse</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_39.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">Adicionar uma nova c\u00e2mera</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Nova c\u00e2mera", None))
        self.btn_add_camera_2.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_recordings_2.setText(QCoreApplication.translate("MainWindow", u"Grava\u00e7\u00f5es", None))
        self.gb_roi_2.setTitle(QCoreApplication.translate("MainWindow", u"Regi\u00e3o de interesse central", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Desenhar malha", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"W:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"H:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.btn_roi_set_2.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.ckb_roi_2.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.groupBox_visu_2.setTitle(QCoreApplication.translate("MainWindow", u"Visualiza\u00e7\u00e3o", None))
        self.btn_visu_2.setText(QCoreApplication.translate("MainWindow", u"Iniciar visualiza\u00e7\u00e3o", None))
        self.btn_stop_visu_2.setText(QCoreApplication.translate("MainWindow", u"Parar visualiza\u00e7\u00e3o", None))
        self.btn_init_rec_2.setText(QCoreApplication.translate("MainWindow", u"Iniciar grava\u00e7\u00e3o", None))
        self.btn_stop_rec_2.setText(QCoreApplication.translate("MainWindow", u"Parar grava\u00e7\u00e3o", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es de HSV", None))
        self.left_title_2.setText(QCoreApplication.translate("MainWindow", u"HSV Max", None))
        self.right_title_2.setText(QCoreApplication.translate("MainWindow", u"HSV Min", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_57.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">Temperatura da CPU</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"TEMP", None))
#if QT_CONFIG(tooltip)
        self.label_58.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">CPU usada</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.Qlabel_cpu_2.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
#if QT_CONFIG(tooltip)
        self.label_59.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">RAM usada</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.Qlabel_fps_2.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
#if QT_CONFIG(tooltip)
        self.label_60.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">FPS tela de \u00e1reas de interesse</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.Qlabel_ram_2.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.Qlabel_temp_2.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.Qlabel_greenlight_2.setText(QCoreApplication.translate("MainWindow", u"Alarme", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"SafeMac \u00a9 2023 Voxar Labs - Todos os direitos reservados.", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.2", None))
    # retranslateUi

