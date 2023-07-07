# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMmqRzA.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 698)
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
"    color: #ffffff;\n"
"    background-color: blue;\n"
"    border: none;\n"
"	border-left: 5px solid yellow;\n"
"    padding: 5px;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QToolTip::text {\n"
"    background-color: #3a8ab0;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #000033;\n"
"	border: 1px solid #000066;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #000080;\n"
"}\n"
"#topLogo {\n"
"	background-color: #000033;\n"
"	background-image: ur"
                        "l(:/images/images/images/PyDracula.png);\n"
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
""
                        "}\n"
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
"	background-color: #0935B0;\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-r"
                        "epeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: #FFD700; border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: #E6C300; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"\n"
"#extraContent{\n"
"	border-top: 3px solid #262680;\n"
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
"	background-color: #000033;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: #0935B0;\n"
""
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
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SET"
                        "TINGS */\n"
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
"	background-color: #000033;\n"
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
"	gridline-color: #000033;\n"
"	border-bottom: 1px solid #262680;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #000033;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #000033;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #0935B0;\n"
"}\n"
"QHeaderView::section{\n"
""
                        "	background-color: #000033;\n"
"	max-width: 30px;\n"
"	border: 1px solid #000033;\n"
"	border-style: none;\n"
"    border-bottom: 1px solid #000033;\n"
"    border-right: 1px solid #000033;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #000033;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #000033;\n"
"	background-color: #000033;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #000033;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #000033;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #000033;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #ffff00;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91,"
                        " 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #000033;\n"
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
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0935B0;\n"
"    min-width: 25px;\n"
"	bord"
                        "er-radius: 4px\n"
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
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #0935B0;\n"
"    min-height:"
                        " 25px;\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px"
                        ";\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background"
                        "-color: #000033;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #000033;\n"
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
"	border-left-color: red;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #ffff00;	\n"
"	background-color: #000033;\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-c"
                        "olor: rgb(52, 59, 72);\n"
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
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #0935B0;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-co"
                        "lor: #ffff00;\n"
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
"	background-color: #000033;\n"
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
"	background-color: yellow;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
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
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"")

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

        self.btn_new_video = QPushButton(self.extraTopMenu)
        self.btn_new_video.setObjectName(u"btn_new_video")
        sizePolicy.setHeightForWidth(self.btn_new_video.sizePolicy().hasHeightForWidth())
        self.btn_new_video.setSizePolicy(sizePolicy)
        self.btn_new_video.setMinimumSize(QSize(0, 45))
        self.btn_new_video.setFont(font)
        self.btn_new_video.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_video.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_video.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-camera-roll.png);")

        self.verticalLayout_11.addWidget(self.btn_new_video)


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
        self.settingsTopBtn.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #FFD700;\n"
"}\n"
"")
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
        self.minimizeAppBtn.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #FFD700;\n"
"}\n"
"")
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
        self.maximizeRestoreAppBtn.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #FFD700;\n"
"}\n"
"")
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
        self.closeAppBtn.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #FFD700;\n"
"}\n"
"")
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
        self.verticalLayout_44 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.verticalLayout_34 = QVBoxLayout(self.home)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.box_top = QFrame(self.frame)
        self.box_top.setObjectName(u"box_top")
        self.box_top.setMaximumSize(QSize(16777215, 120))
        self.box_top.setStyleSheet(u"")
        self.box_top.setFrameShape(QFrame.NoFrame)
        self.box_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.box_top)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.welcome_box = QFrame(self.box_top)
        self.welcome_box.setObjectName(u"welcome_box")
        self.welcome_box.setStyleSheet(u"background-color: none;")
        self.welcome_box.setFrameShape(QFrame.NoFrame)
        self.welcome_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.welcome_box)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_7 = QLabel(self.welcome_box)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(162, 162, 162);\n"
"font: 36pt \"Segoe UI Variable Small\";\n"
"background-color: none;\n"
"")

        self.verticalLayout_32.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.welcome_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(162, 162, 162);\n"
"font: 8pt \"Segoe UI Variable Small\";\n"
"background-color: none;")

        self.verticalLayout_32.addWidget(self.label_8)


        self.verticalLayout_31.addWidget(self.welcome_box)


        self.verticalLayout_24.addWidget(self.box_top)

        self.box_bottom = QFrame(self.frame)
        self.box_bottom.setObjectName(u"box_bottom")
        self.box_bottom.setMaximumSize(QSize(16777215, 400))
        self.box_bottom.setStyleSheet(u"")
        self.box_bottom.setFrameShape(QFrame.StyledPanel)
        self.box_bottom.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.box_bottom)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setContentsMargins(80, -1, 80, 40)
        self.box_calibrate = QFrame(self.box_bottom)
        self.box_calibrate.setObjectName(u"box_calibrate")
        self.box_calibrate.setMinimumSize(QSize(230, 0))
        self.box_calibrate.setMaximumSize(QSize(400, 16777215))
        self.box_calibrate.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.517, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 0, 102, 255), stop:1 rgba(0, 0, 255, 242));\n"
"	border-radius: 7px;\n"
"	text-align: justify;\n"
"}")
        self.box_calibrate.setFrameShape(QFrame.NoFrame)
        self.box_calibrate.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.box_calibrate)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.box_calibrate)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 140))
        self.frame_10.setStyleSheet(u"background-color: none;")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.img_calibrate = QLabel(self.frame_10)
        self.img_calibrate.setObjectName(u"img_calibrate")
        self.img_calibrate.setStyleSheet(u"border-radius: 7px;")

        self.horizontalLayout_9.addWidget(self.img_calibrate)


        self.verticalLayout_35.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.box_calibrate)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: none;")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_13)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_9.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.label_9)


        self.verticalLayout_35.addWidget(self.frame_13)

        self.btn_calibrate = QPushButton(self.box_calibrate)
        self.btn_calibrate.setObjectName(u"btn_calibrate")
        self.btn_calibrate.setMinimumSize(QSize(0, 50))
        self.btn_calibrate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calibrate.setStyleSheet(u"QPushButton {\n"
"    padding: 4px;\n"
"    border: none;\n"
"    color: #c0c0c0;\n"
"    border-radius: 7px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.verticalLayout_35.addWidget(self.btn_calibrate)


        self.gridLayout_2.addWidget(self.box_calibrate, 0, 0, 1, 1)

        self.box_visualize = QFrame(self.box_bottom)
        self.box_visualize.setObjectName(u"box_visualize")
        self.box_visualize.setMinimumSize(QSize(230, 0))
        self.box_visualize.setMaximumSize(QSize(400, 16777215))
        self.box_visualize.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.517, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 0, 102, 255), stop:1 rgba(0, 0, 255, 242));\n"
"	border-radius: 7px;\n"
"}")
        self.box_visualize.setFrameShape(QFrame.NoFrame)
        self.box_visualize.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.box_visualize)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.box_visualize)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 140))
        self.frame_22.setStyleSheet(u"background-color: none;")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.img_visualize = QLabel(self.frame_22)
        self.img_visualize.setObjectName(u"img_visualize")
        self.img_visualize.setStyleSheet(u"border-radius: 7px;")

        self.horizontalLayout_12.addWidget(self.img_visualize)


        self.verticalLayout_37.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.box_visualize)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: none;")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_23)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_10 = QLabel(self.frame_23)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_10.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_37.addWidget(self.frame_23)

        self.btn_visualize = QPushButton(self.box_visualize)
        self.btn_visualize.setObjectName(u"btn_visualize")
        self.btn_visualize.setMinimumSize(QSize(0, 50))
        self.btn_visualize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visualize.setStyleSheet(u"QPushButton {\n"
"    padding: 4px;\n"
"    border: none;\n"
"    color: #c0c0c0;\n"
"    border-radius: 7px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.verticalLayout_37.addWidget(self.btn_visualize)


        self.gridLayout_2.addWidget(self.box_visualize, 0, 1, 1, 1)

        self.box_instructions = QFrame(self.box_bottom)
        self.box_instructions.setObjectName(u"box_instructions")
        self.box_instructions.setMinimumSize(QSize(230, 0))
        self.box_instructions.setMaximumSize(QSize(400, 16777215))
        self.box_instructions.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.517, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 0, 102, 255), stop:1 rgba(0, 0, 255, 242));\n"
"	border-radius: 7px;\n"
"}")
        self.box_instructions.setFrameShape(QFrame.NoFrame)
        self.box_instructions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.box_instructions)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.box_instructions)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 140))
        self.frame_24.setStyleSheet(u"background-color: none;")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.img_instructions = QLabel(self.frame_24)
        self.img_instructions.setObjectName(u"img_instructions")
        self.img_instructions.setStyleSheet(u"border-radius: 7px;")

        self.horizontalLayout_13.addWidget(self.img_instructions)


        self.verticalLayout_39.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.box_instructions)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: none;")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_25)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, 9, -1, -1)
        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_11.setWordWrap(True)

        self.verticalLayout_40.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_39.addWidget(self.frame_25)

        self.btn_instructions = QPushButton(self.box_instructions)
        self.btn_instructions.setObjectName(u"btn_instructions")
        self.btn_instructions.setMinimumSize(QSize(0, 50))
        self.btn_instructions.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_instructions.setStyleSheet(u"QPushButton {\n"
"    padding: 4px;\n"
"    border: none;\n"
"    color: #c0c0c0;\n"
"    border-radius: 7px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.verticalLayout_39.addWidget(self.btn_instructions)


        self.gridLayout_2.addWidget(self.box_instructions, 0, 2, 1, 1)


        self.verticalLayout_24.addWidget(self.box_bottom)


        self.verticalLayout_34.addWidget(self.frame)

        self.stackedWidget.addWidget(self.home)
        self.tabs = QWidget()
        self.tabs.setObjectName(u"tabs")
        self.tabs.setStyleSheet(u"b")
        self.verticalLayout_15 = QVBoxLayout(self.tabs)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.tabs)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.infos_saves = QTabWidget(self.frame_5)
        self.infos_saves.setObjectName(u"infos_saves")
        self.infos_saves.setCursor(QCursor(Qt.ArrowCursor))
        self.infos_saves.setStyleSheet(u"#cameras_tab, #bumps_tab, #config_dest {\n"
"    background: qlineargradient(spread:pad, x1:0.5, y1:0.00568182, x2:0.511, y2:1, stop:0 rgba(0, 0, 68, 255), stop:1 rgba(0, 0, 102, 255));\n"
"    border-radius: 8px;\n"
"    border-top-left-radius: 0;\n"
"}\n"
"\n"
"\n"
"#infos_saves::pane {\n"
"	border: none;\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"	border-top-left-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #0000FF;\n"
"    padding: 4px;\n"
"    border-right: 2px solid #00004D;\n"
"}\n"
"\n"
"QTabBar::tab::last {\n"
"    border-right: none; \n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	background: #ffff00;\n"
"	color: black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background: #00004D;\n"
"	color: #c0c0c0;\n"
"}\n"
"")
        self.cameras_tab = QWidget()
        self.cameras_tab.setObjectName(u"cameras_tab")
        self.verticalLayout_18 = QVBoxLayout(self.cameras_tab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.bottom_table = QFrame(self.cameras_tab)
        self.bottom_table.setObjectName(u"bottom_table")
        self.bottom_table.setFrameShape(QFrame.StyledPanel)
        self.bottom_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.bottom_table)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tableWidget = QTableWidget(self.bottom_table)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    border-radius: 0px;\n"
"}\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 7px;\n"
"}\n"
"QHeaderView::section {\n"
"    border-top-hight-radius: 7px;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)

        self.horizontalLayout_14.addWidget(self.tableWidget)

        self.config_box = QFrame(self.bottom_table)
        self.config_box.setObjectName(u"config_box")
        self.config_box.setStyleSheet(u"QPushButton{\n"
"	background-color: #000099;\n"
"	padding: 5px;\n"
"	color: #c0c0c0;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: yellow;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: #E6E600;\n"
"	color: black;\n"
"}")
        self.config_box.setFrameShape(QFrame.StyledPanel)
        self.config_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.config_box)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.pushButton = QPushButton(self.config_box)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_41.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.config_box)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_41.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.config_box)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_41.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.config_box)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_41.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.config_box)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_41.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer)


        self.horizontalLayout_14.addWidget(self.config_box)


        self.verticalLayout_18.addWidget(self.bottom_table)

        self.infos_saves.addTab(self.cameras_tab, "")
        self.bumps_tab = QWidget()
        self.bumps_tab.setObjectName(u"bumps_tab")
        self.infos_saves.addTab(self.bumps_tab, "")
        self.config_dest = QWidget()
        self.config_dest.setObjectName(u"config_dest")
        self.infos_saves.addTab(self.config_dest, "")

        self.verticalLayout_17.addWidget(self.infos_saves)


        self.verticalLayout_15.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.tabs)
        self.cameras = QWidget()
        self.cameras.setObjectName(u"cameras")
        self.verticalLayout_42 = QVBoxLayout(self.cameras)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_26 = QFrame(self.cameras)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setAutoFillBackground(False)
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.box_cameras_top = QFrame(self.frame_26)
        self.box_cameras_top.setObjectName(u"box_cameras_top")
        self.box_cameras_top.setMinimumSize(QSize(0, 300))
        self.box_cameras_top.setFrameShape(QFrame.StyledPanel)
        self.box_cameras_top.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.box_cameras_top)
        self.gridLayout_7.setSpacing(4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tela_1 = QFrame(self.box_cameras_top)
        self.tela_1.setObjectName(u"tela_1")
        self.tela_1.setMinimumSize(QSize(0, 0))
        self.tela_1.setStyleSheet(u"background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.tela_1.setFrameShape(QFrame.NoFrame)
        self.tela_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.tela_1)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.lb_camera_1 = QLabel(self.tela_1)
        self.lb_camera_1.setObjectName(u"lb_camera_1")

        self.verticalLayout_63.addWidget(self.lb_camera_1)


        self.gridLayout_7.addWidget(self.tela_1, 0, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.box_cameras_top)


        self.verticalLayout_42.addWidget(self.frame_26)

        self.hide_configs_camera = QPushButton(self.cameras)
        self.hide_configs_camera.setObjectName(u"hide_configs_camera")
        self.hide_configs_camera.setMinimumSize(QSize(0, 0))
        self.hide_configs_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.hide_configs_camera.setStyleSheet(u"QPushButton{\n"
"	padding: 7px;\n"
"	border: none;\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"	font: 600 9pt \"Segoe UI Variable Small\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.verticalLayout_42.addWidget(self.hide_configs_camera)

        self.bottom_configs = QFrame(self.cameras)
        self.bottom_configs.setObjectName(u"bottom_configs")
        self.bottom_configs.setMaximumSize(QSize(16777215, 200))
        self.bottom_configs.setFrameShape(QFrame.NoFrame)
        self.bottom_configs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.bottom_configs)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.configs_video = QFrame(self.bottom_configs)
        self.configs_video.setObjectName(u"configs_video")
        self.configs_video.setMinimumSize(QSize(0, 160))
        self.configs_video.setMaximumSize(QSize(16777215, 200))
        self.configs_video.setStyleSheet(u"")
        self.configs_video.setFrameShape(QFrame.NoFrame)
        self.configs_video.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.configs_video)
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.box_config_cameras = QFrame(self.configs_video)
        self.box_config_cameras.setObjectName(u"box_config_cameras")
        self.box_config_cameras.setMaximumSize(QSize(400, 16777215))
        self.box_config_cameras.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";")
        self.box_config_cameras.setFrameShape(QFrame.NoFrame)
        self.box_config_cameras.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.box_config_cameras)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(3, 0, 3, 1)
        self.frame_27 = QFrame(self.box_config_cameras)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 50))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, -1, -1, -1)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_38.setSpacing(3)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(2, -1, -1, -1)
        self.label_61 = QLabel(self.frame_28)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"color: rgb(192, 192, 192);")

        self.horizontalLayout_38.addWidget(self.label_61)


        self.horizontalLayout_37.addWidget(self.frame_28)

        self.btn_add_camera = QPushButton(self.frame_27)
        self.btn_add_camera.setObjectName(u"btn_add_camera")
        self.btn_add_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_camera.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_37.addWidget(self.btn_add_camera)

        self.btn_recordings = QPushButton(self.frame_27)
        self.btn_recordings.setObjectName(u"btn_recordings")
        self.btn_recordings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recordings.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_37.addWidget(self.btn_recordings)


        self.verticalLayout_65.addWidget(self.frame_27)

        self.gb_roi = QGroupBox(self.box_config_cameras)
        self.gb_roi.setObjectName(u"gb_roi")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gb_roi.sizePolicy().hasHeightForWidth())
        self.gb_roi.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Small"])
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.gb_roi.setFont(font3)
        self.gb_roi.setMouseTracking(False)
        self.gb_roi.setTabletTracking(False)
        self.gb_roi.setFocusPolicy(Qt.NoFocus)
        self.gb_roi.setLayoutDirection(Qt.LeftToRight)
        self.gb_roi.setStyleSheet(u"color: rgb(192, 192, 192);")
        self.gb_roi.setFlat(False)
        self.gridLayout_16 = QGridLayout(self.gb_roi)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(-1, 5, -1, 8)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_62 = QLabel(self.gb_roi)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 20))
        self.label_62.setStyleSheet(u"margin: 0px 0px 2px 0px;")

        self.gridLayout_11.addWidget(self.label_62, 4, 1, 1, 1)

        self.label_63 = QLabel(self.gb_roi)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_11.addWidget(self.label_63, 3, 0, 1, 1)

        self.label_64 = QLabel(self.gb_roi)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_11.addWidget(self.label_64, 3, 2, 1, 1)

        self.label_65 = QLabel(self.gb_roi)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_11.addWidget(self.label_65, 1, 2, 1, 1)

        self.ROI_H = QSpinBox(self.gb_roi)
        self.ROI_H.setObjectName(u"ROI_H")
        self.ROI_H.setMinimumSize(QSize(0, 20))
        self.ROI_H.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_H.setMaximum(2000)
        self.ROI_H.setValue(1000)

        self.gridLayout_11.addWidget(self.ROI_H, 3, 3, 1, 1)

        self.btn_roi_set = QPushButton(self.gb_roi)
        self.btn_roi_set.setObjectName(u"btn_roi_set")
        self.btn_roi_set.setMinimumSize(QSize(0, 20))
        self.btn_roi_set.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_roi_set.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 26, 26);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(63, 63, 63);\n"
"	background-color: rgb(255, 255, 38);\n"
"}")

        self.gridLayout_11.addWidget(self.btn_roi_set, 4, 3, 1, 1)

        self.ckb_roi = QCheckBox(self.gb_roi)
        self.ckb_roi.setObjectName(u"ckb_roi")
        self.ckb_roi.setMinimumSize(QSize(0, 20))

        self.gridLayout_11.addWidget(self.ckb_roi, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.ROI_X = QSpinBox(self.gb_roi)
        self.ROI_X.setObjectName(u"ROI_X")
        self.ROI_X.setMinimumSize(QSize(0, 20))
        self.ROI_X.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_X.setMinimum(0)
        self.ROI_X.setMaximum(1000)
        self.ROI_X.setValue(20)

        self.gridLayout_11.addWidget(self.ROI_X, 1, 1, 1, 1)

        self.label_66 = QLabel(self.gb_roi)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_11.addWidget(self.label_66, 1, 0, 1, 1)

        self.ROI_Y = QSpinBox(self.gb_roi)
        self.ROI_Y.setObjectName(u"ROI_Y")
        self.ROI_Y.setMinimumSize(QSize(0, 20))
        self.ROI_Y.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_Y.setMinimum(0)
        self.ROI_Y.setMaximum(1000)
        self.ROI_Y.setValue(20)

        self.gridLayout_11.addWidget(self.ROI_Y, 1, 3, 1, 1)

        self.ROI_W = QSpinBox(self.gb_roi)
        self.ROI_W.setObjectName(u"ROI_W")
        self.ROI_W.setMinimumSize(QSize(0, 20))
        self.ROI_W.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"margin: 0px 0px 2px 0px;\n"
"background-color: rgb(195, 204, 223);\n"
"font: 500 9pt \"Segoe UI Variable Small\";")
        self.ROI_W.setMaximum(2000)
        self.ROI_W.setValue(1000)

        self.gridLayout_11.addWidget(self.ROI_W, 3, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.verticalLayout_65.addWidget(self.gb_roi)


        self.horizontalLayout_36.addWidget(self.box_config_cameras)

        self.frame_29 = QFrame(self.configs_video)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 9, 0, 0)
        self.groupBox_visu = QGroupBox(self.frame_29)
        self.groupBox_visu.setObjectName(u"groupBox_visu")
        self.groupBox_visu.setMinimumSize(QSize(210, 0))
        self.groupBox_visu.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_visu.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";\n"
"color: rgb(192, 192, 192);\n"
"")
        self.gridLayout_8 = QGridLayout(self.groupBox_visu)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(2)
        self.gridLayout_8.setContentsMargins(4, 1, 4, 1)
        self.btn_visu = QPushButton(self.groupBox_visu)
        self.btn_visu.setObjectName(u"btn_visu")
        self.btn_visu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visu.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_8.addWidget(self.btn_visu, 0, 0, 1, 1)

        self.btn_stop_visu = QPushButton(self.groupBox_visu)
        self.btn_stop_visu.setObjectName(u"btn_stop_visu")
        self.btn_stop_visu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_visu.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_8.addWidget(self.btn_stop_visu, 1, 0, 1, 1)

        self.btn_init_rec = QPushButton(self.groupBox_visu)
        self.btn_init_rec.setObjectName(u"btn_init_rec")
        self.btn_init_rec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_init_rec.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_8.addWidget(self.btn_init_rec, 2, 0, 1, 1)

        self.btn_stop_rec = QPushButton(self.groupBox_visu)
        self.btn_stop_rec.setObjectName(u"btn_stop_rec")
        self.btn_stop_rec.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop_rec.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_8.addWidget(self.btn_stop_rec, 3, 0, 1, 1)


        self.horizontalLayout_39.addWidget(self.groupBox_visu)


        self.horizontalLayout_36.addWidget(self.frame_29)

        self.box_HSV_configs = QFrame(self.configs_video)
        self.box_HSV_configs.setObjectName(u"box_HSV_configs")
        self.box_HSV_configs.setMaximumSize(QSize(400, 16777215))
        self.box_HSV_configs.setStyleSheet(u"\n"
"QSlider::handle:hover {\n"
"	background-color: rgb(255, 255, 0);\n"
"}")
        self.box_HSV_configs.setFrameShape(QFrame.StyledPanel)
        self.box_HSV_configs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.box_HSV_configs)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 9, 0, 0)
        self.groupBox_8 = QGroupBox(self.box_HSV_configs)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(228, 100))
        self.groupBox_8.setAutoFillBackground(False)
        self.groupBox_8.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";\n"
"color: rgb(192, 192, 192);")
        self.groupBox_8.setFlat(False)
        self.groupBox_8.setCheckable(False)
        self.verticalLayout_67 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_67.setSpacing(4)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.titles_hsv = QFrame(self.groupBox_8)
        self.titles_hsv.setObjectName(u"titles_hsv")
        self.titles_hsv.setMinimumSize(QSize(0, 23))
        self.titles_hsv.setMaximumSize(QSize(16777215, 40))
        self.titles_hsv.setStyleSheet(u"")
        self.titles_hsv.setFrameShape(QFrame.NoFrame)
        self.titles_hsv.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.titles_hsv)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(9, 5, 9, 0)
        self.left_title = QLabel(self.titles_hsv)
        self.left_title.setObjectName(u"left_title")
        self.left_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.left_title)

        self.right_title = QLabel(self.titles_hsv)
        self.right_title.setObjectName(u"right_title")
        self.right_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.right_title)


        self.verticalLayout_67.addWidget(self.titles_hsv)

        self.content_box = QFrame(self.groupBox_8)
        self.content_box.setObjectName(u"content_box")
        self.content_box.setMinimumSize(QSize(0, 0))
        self.content_box.setFrameShape(QFrame.NoFrame)
        self.content_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.content_box)
        self.horizontalLayout_41.setSpacing(4)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 5)
        self.frame_30 = QFrame(self.content_box)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(135, 16777215))
        self.frame_30.setStyleSheet(u"")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_30)
        self.verticalLayout_68.setSpacing(2)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(1, 1, 1, 1)
        self.box_h_max = QFrame(self.frame_30)
        self.box_h_max.setObjectName(u"box_h_max")
        self.box_h_max.setStyleSheet(u"")
        self.box_h_max.setFrameShape(QFrame.NoFrame)
        self.box_h_max.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.box_h_max)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_67 = QLabel(self.box_h_max)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_42.addWidget(self.label_67)

        self.horizontalSlider_13 = QSlider(self.box_h_max)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_13.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_13.setStyleSheet(u"QSlider::handle {\n"
"    height: 10px; /* Largura do manipulador do slider */\n"
"}")
        self.horizontalSlider_13.setOrientation(Qt.Horizontal)

        self.horizontalLayout_42.addWidget(self.horizontalSlider_13)

        self.label_68 = QLabel(self.box_h_max)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_42.addWidget(self.label_68)


        self.verticalLayout_68.addWidget(self.box_h_max)

        self.box_s_max = QFrame(self.frame_30)
        self.box_s_max.setObjectName(u"box_s_max")
        self.box_s_max.setStyleSheet(u"")
        self.box_s_max.setFrameShape(QFrame.NoFrame)
        self.box_s_max.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.box_s_max)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_69 = QLabel(self.box_s_max)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_43.addWidget(self.label_69)

        self.horizontalSlider_14 = QSlider(self.box_s_max)
        self.horizontalSlider_14.setObjectName(u"horizontalSlider_14")
        self.horizontalSlider_14.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_14.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_14.setStyleSheet(u"")
        self.horizontalSlider_14.setOrientation(Qt.Horizontal)

        self.horizontalLayout_43.addWidget(self.horizontalSlider_14)

        self.label_70 = QLabel(self.box_s_max)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_43.addWidget(self.label_70)


        self.verticalLayout_68.addWidget(self.box_s_max)

        self.box_v_max = QFrame(self.frame_30)
        self.box_v_max.setObjectName(u"box_v_max")
        self.box_v_max.setStyleSheet(u"")
        self.box_v_max.setFrameShape(QFrame.NoFrame)
        self.box_v_max.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.box_v_max)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_71 = QLabel(self.box_v_max)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_44.addWidget(self.label_71)

        self.horizontalSlider_15 = QSlider(self.box_v_max)
        self.horizontalSlider_15.setObjectName(u"horizontalSlider_15")
        self.horizontalSlider_15.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_15.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_15.setOrientation(Qt.Horizontal)

        self.horizontalLayout_44.addWidget(self.horizontalSlider_15)

        self.label_72 = QLabel(self.box_v_max)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_44.addWidget(self.label_72)


        self.verticalLayout_68.addWidget(self.box_v_max)


        self.horizontalLayout_41.addWidget(self.frame_30)

        self.box_right = QFrame(self.content_box)
        self.box_right.setObjectName(u"box_right")
        self.box_right.setMaximumSize(QSize(135, 16777215))
        self.box_right.setStyleSheet(u"")
        self.box_right.setFrameShape(QFrame.NoFrame)
        self.box_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.box_right)
        self.verticalLayout_69.setSpacing(2)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(1, 1, 1, 1)
        self.box_h_min = QFrame(self.box_right)
        self.box_h_min.setObjectName(u"box_h_min")
        self.box_h_min.setStyleSheet(u"")
        self.box_h_min.setFrameShape(QFrame.NoFrame)
        self.box_h_min.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.box_h_min)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_12 = QLabel(self.box_h_min)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_45.addWidget(self.label_12)

        self.horizontalSlider_16 = QSlider(self.box_h_min)
        self.horizontalSlider_16.setObjectName(u"horizontalSlider_16")
        self.horizontalSlider_16.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_16.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_16.setOrientation(Qt.Horizontal)

        self.horizontalLayout_45.addWidget(self.horizontalSlider_16)

        self.label_13 = QLabel(self.box_h_min)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_45.addWidget(self.label_13)


        self.verticalLayout_69.addWidget(self.box_h_min)

        self.box_s_min = QFrame(self.box_right)
        self.box_s_min.setObjectName(u"box_s_min")
        self.box_s_min.setStyleSheet(u"")
        self.box_s_min.setFrameShape(QFrame.NoFrame)
        self.box_s_min.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.box_s_min)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_75 = QLabel(self.box_s_min)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_46.addWidget(self.label_75)

        self.horizontalSlider_17 = QSlider(self.box_s_min)
        self.horizontalSlider_17.setObjectName(u"horizontalSlider_17")
        self.horizontalSlider_17.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_17.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_17.setOrientation(Qt.Horizontal)

        self.horizontalLayout_46.addWidget(self.horizontalSlider_17)

        self.label_76 = QLabel(self.box_s_min)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_46.addWidget(self.label_76)


        self.verticalLayout_69.addWidget(self.box_s_min)

        self.box_v_min = QFrame(self.box_right)
        self.box_v_min.setObjectName(u"box_v_min")
        self.box_v_min.setStyleSheet(u"")
        self.box_v_min.setFrameShape(QFrame.NoFrame)
        self.box_v_min.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.box_v_min)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_77 = QLabel(self.box_v_min)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_47.addWidget(self.label_77)

        self.horizontalSlider_18 = QSlider(self.box_v_min)
        self.horizontalSlider_18.setObjectName(u"horizontalSlider_18")
        self.horizontalSlider_18.setMinimumSize(QSize(0, 10))
        self.horizontalSlider_18.setMaximumSize(QSize(16777215, 10))
        self.horizontalSlider_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_18.setOrientation(Qt.Horizontal)

        self.horizontalLayout_47.addWidget(self.horizontalSlider_18)

        self.label_78 = QLabel(self.box_v_min)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_47.addWidget(self.label_78)


        self.verticalLayout_69.addWidget(self.box_v_min)


        self.horizontalLayout_41.addWidget(self.box_right)


        self.verticalLayout_67.addWidget(self.content_box)


        self.verticalLayout_66.addWidget(self.groupBox_8)


        self.horizontalLayout_36.addWidget(self.box_HSV_configs)

        self.infor_system = QFrame(self.configs_video)
        self.infor_system.setObjectName(u"infor_system")
        self.infor_system.setMaximumSize(QSize(400, 16777215))
        self.infor_system.setFrameShape(QFrame.StyledPanel)
        self.infor_system.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.infor_system)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.infor_system)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"font: 600 9pt \"Segoe UI Variable Small\";")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_31)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.system_infos = QFrame(self.frame_31)
        self.system_infos.setObjectName(u"system_infos")
        self.system_infos.setStyleSheet(u"color: rgb(192, 192, 192);")
        self.system_infos.setFrameShape(QFrame.StyledPanel)
        self.system_infos.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.system_infos)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Qlabel_fps = QLabel(self.system_infos)
        self.Qlabel_fps.setObjectName(u"Qlabel_fps")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Variable Small"])
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(False)
        self.Qlabel_fps.setFont(font4)
        self.Qlabel_fps.setStyleSheet(u"color: rgb(237, 85, 59);")
        self.Qlabel_fps.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.Qlabel_fps, 1, 0, 1, 1)

        self.Qlabel_temp = QLabel(self.system_infos)
        self.Qlabel_temp.setObjectName(u"Qlabel_temp")
        self.Qlabel_temp.setFont(font4)
        self.Qlabel_temp.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.Qlabel_temp, 1, 4, 1, 1)

        self.label_79 = QLabel(self.system_infos)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font4)
        self.label_79.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_79, 0, 4, 1, 1)

        self.label_80 = QLabel(self.system_infos)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font4)
        self.label_80.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_80, 0, 1, 1, 1)

        self.Qlabel_cpu = QLabel(self.system_infos)
        self.Qlabel_cpu.setObjectName(u"Qlabel_cpu")
        self.Qlabel_cpu.setFont(font4)
        self.Qlabel_cpu.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.Qlabel_cpu, 1, 1, 1, 1)

        self.label_81 = QLabel(self.system_infos)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font4)
        self.label_81.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_81, 0, 0, 1, 1)

        self.label_82 = QLabel(self.system_infos)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font4)
        self.label_82.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_82, 0, 3, 1, 1)

        self.Qlabel_ram = QLabel(self.system_infos)
        self.Qlabel_ram.setObjectName(u"Qlabel_ram")
        self.Qlabel_ram.setFont(font4)
        self.Qlabel_ram.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.Qlabel_ram, 1, 3, 1, 1)


        self.verticalLayout_71.addWidget(self.system_infos)

        self.alarm_box = QFrame(self.frame_31)
        self.alarm_box.setObjectName(u"alarm_box")
        self.alarm_box.setFrameShape(QFrame.StyledPanel)
        self.alarm_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.alarm_box)
        self.horizontalLayout_48.setSpacing(5)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.Qlabel_greenlight = QLabel(self.alarm_box)
        self.Qlabel_greenlight.setObjectName(u"Qlabel_greenlight")
        self.Qlabel_greenlight.setFont(font4)
        self.Qlabel_greenlight.setStyleSheet(u"background-color: rgb(34, 139, 34);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.Qlabel_greenlight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.Qlabel_greenlight)


        self.verticalLayout_71.addWidget(self.alarm_box)


        self.verticalLayout_70.addWidget(self.frame_31)


        self.horizontalLayout_36.addWidget(self.infor_system)


        self.verticalLayout_43.addWidget(self.configs_video)


        self.verticalLayout_42.addWidget(self.bottom_configs)

        self.stackedWidget.addWidget(self.cameras)

        self.verticalLayout_44.addWidget(self.stackedWidget)


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
        self.infos_saves.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SafeMac</p></body></html>", None))
        self.label_logo.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Esconder", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.btn_cameras.setText(QCoreApplication.translate("MainWindow", u"C\u00e2meras", None))
        self.btn_videos.setText(QCoreApplication.translate("MainWindow", u"Grava\u00e7\u00f5es", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Compartilhar", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
#if QT_CONFIG(tooltip)
        self.btn_new_video.setToolTip(QCoreApplication.translate("MainWindow", u"V\u00eddeo a partir de dataset", None))
#endif // QT_CONFIG(tooltip)
        self.btn_new_video.setText(QCoreApplication.translate("MainWindow", u"Novo v\u00eddeo", None))
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
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Bem vindo</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Adicione pelo menos uma c\u00e2mera antes de monitorar o sistema pela primeira vez.</span></p></body></html>", None))
        self.img_calibrate.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mantenha a boa vis\u00e3o do seu equipamento. A calibra\u00e7\u00e3o garante que estamos vendo tudo com clareza e precis\u00e3o. Sempre calibre ap\u00f3s mover a c\u00e2mera, grandes mudan\u00e7as de ambiente, ou ap\u00f3s manuten\u00e7\u00f5es.", None))
        self.btn_calibrate.setText(QCoreApplication.translate("MainWindow", u"Adicionar C\u00e2mera", None))
        self.img_visualize.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Acesse as c\u00e2meras em tempo real para monitorar continuamente o ambiente ao redor do equipamento. Mantenha-se informado e tome decis\u00f5es seguras com base em informa\u00e7\u00f5es atualizadas.", None))
        self.btn_visualize.setText(QCoreApplication.translate("MainWindow", u"Visualizar Detec\u00e7\u00f5es", None))
        self.img_instructions.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Aqui est\u00e3o as instru\u00e7\u00f5es completas para a utiliza\u00e7\u00e3o e manuten\u00e7\u00e3o adequada do sistema. Familiarize-se com todas as funcionalidades para garantir a m\u00e1xima efici\u00eancia e seguran\u00e7a. Siga as orienta\u00e7\u00f5es e previna acidentes.", None))
        self.btn_instructions.setText(QCoreApplication.translate("MainWindow", u"Instru\u00e7\u00f5es", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Posi\u00e7\u00e3o 3D (x)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Posi\u00e7\u00e3o 3D (y)", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Posi\u00e7\u00e3o 3D (z)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Matriz de Rota\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Matriz de Transla\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ponto Principal (x)", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Ponto Principal (y)", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Distor\u00e7\u00e3o Radial", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Coeficiente de Calibra\u00e7\u00e3o", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Data de Calibra\u00e7\u00e3o", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Editar par\u00e2metros", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Salvar altera\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Reverter altera\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.infos_saves.setTabText(self.infos_saves.indexOf(self.cameras_tab), QCoreApplication.translate("MainWindow", u"C\u00e2meras", None))
        self.infos_saves.setTabText(self.infos_saves.indexOf(self.bumps_tab), QCoreApplication.translate("MainWindow", u"Grava\u00e7\u00f5es", None))
        self.infos_saves.setTabText(self.infos_saves.indexOf(self.config_dest), QCoreApplication.translate("MainWindow", u"Destino", None))
        self.lb_camera_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">camera 1</p></body></html>", None))
        self.hide_configs_camera.setText(QCoreApplication.translate("MainWindow", u"Esconder", None))
#if QT_CONFIG(tooltip)
        self.label_61.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">Adicionar uma nova c\u00e2mera</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Nova c\u00e2mera", None))
        self.btn_add_camera.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_recordings.setText(QCoreApplication.translate("MainWindow", u"Grava\u00e7\u00f5es", None))
        self.gb_roi.setTitle(QCoreApplication.translate("MainWindow", u"Regi\u00e3o de interesse central", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Desenhar malha", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"W:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"H:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.btn_roi_set.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.ckb_roi.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.groupBox_visu.setTitle(QCoreApplication.translate("MainWindow", u"Visualiza\u00e7\u00e3o", None))
        self.btn_visu.setText(QCoreApplication.translate("MainWindow", u"Iniciar visualiza\u00e7\u00e3o", None))
        self.btn_stop_visu.setText(QCoreApplication.translate("MainWindow", u"Parar visualiza\u00e7\u00e3o", None))
        self.btn_init_rec.setText(QCoreApplication.translate("MainWindow", u"Iniciar grava\u00e7\u00e3o", None))
        self.btn_stop_rec.setText(QCoreApplication.translate("MainWindow", u"Parar grava\u00e7\u00e3o", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es de HSV", None))
        self.left_title.setText(QCoreApplication.translate("MainWindow", u"HSV Max", None))
        self.right_title.setText(QCoreApplication.translate("MainWindow", u"HSV Min", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Qlabel_fps.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.Qlabel_temp.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
#if QT_CONFIG(tooltip)
        self.label_79.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">Temperatura da CPU</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"TEMP", None))
#if QT_CONFIG(tooltip)
        self.label_80.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">CPU usada</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.Qlabel_cpu.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
#if QT_CONFIG(tooltip)
        self.label_81.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">FPS tela de \u00e1reas de interesse</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
#if QT_CONFIG(tooltip)
        self.label_82.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1a1a1a;\">RAM usada</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.Qlabel_ram.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.Qlabel_greenlight.setText(QCoreApplication.translate("MainWindow", u"Alarme", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"SafeMac \u00a9 2023 Voxar Labs - Todos os direitos reservados.", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.2", None))
    # retranslateUi

