# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTabWidget, QTableView, QTreeView,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 780)
        MainWindow.setMinimumSize(QSize(945, 530))
        MainWindow.setMaximumSize(QSize(1050, 780))
        font = QFont()
        font.setFamilies([u"Calibri"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"imgs/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0.403, x2:1, y2:0.631, stop:0 rgba(25, 56, 73, 255), stop:1 rgba(28, 44, 68, 255))")
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 75))
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0.557, x2:1, y2:0.545, stop:0 rgba(6, 191, 255, 255), stop:1 rgba(45, 115, 255, 255));\n"
"border-radius:7px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setMaximumSize(QSize(177, 30))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"	   \n"
"border-radius:3px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_outro = QPushButton(self.frame)
        self.btn_outro.setObjectName(u"btn_outro")
        self.btn_outro.setMinimumSize(QSize(0, 30))
        self.btn_outro.setMaximumSize(QSize(177, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.btn_outro.setFont(font2)
        self.btn_outro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_outro.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:3px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout.addWidget(self.btn_outro)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 30))
        self.btn_tables.setMaximumSize(QSize(177, 16777215))
        self.btn_tables.setFont(font2)
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:3px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_excluir_usuarios = QPushButton(self.frame)
        self.btn_excluir_usuarios.setObjectName(u"btn_excluir_usuarios")
        self.btn_excluir_usuarios.setMinimumSize(QSize(0, 30))
        self.btn_excluir_usuarios.setMaximumSize(QSize(177, 16777215))
        self.btn_excluir_usuarios.setFont(font2)
        self.btn_excluir_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_usuarios.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:3px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout.addWidget(self.btn_excluir_usuarios)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setMaximumSize(QSize(177, 16777215))
        self.btn_sobre.setFont(font2)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:3px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 30))
        self.btn_contato.setMaximumSize(QSize(177, 16777215))
        self.btn_contato.setFont(font2)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:3px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setMinimumSize(QSize(315, 280))
        self.Pages.setMaximumSize(QSize(16777215, 690))
        self.Pages.setFont(font)
        self.Pages.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0.557, x2:1, y2:0.545, stop:0 rgba(6, 191, 255, 255), stop:1 rgba(45, 115, 255, 255))\n"
"")
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.horizontalLayout_4 = QHBoxLayout(self.page_table)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.page_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(900, 280))
        self.tabWidget.setMaximumSize(QSize(1010, 670))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(9)
        self.tabWidget.setFont(font3)
        self.tabWidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.486, y1:0, x2:0.497, y2:1, stop:0 rgba(42, 71, 94, 255), stop:1 rgba(28, 41, 56, 255))")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_9 = QVBoxLayout(self.tables)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.tables)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(11)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_6.addWidget(self.label_4)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setFont(font)
        self.tw_estoque.setStyleSheet(u"QTreeWidget::item {\n"
"background-color:rgb(189, 189, 189);\n"
"border-left:1px solid black;\n"
"border: 1px solid black;\n"
"border-bottom:1px solid black;\n"
"}\n"
"QTreeWidget {\n"
"background-color:rgb(189, 189, 189);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"	")
        self.tw_estoque.setFrameShape(QFrame.StyledPanel)
        self.tw_estoque.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_estoque.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_6.addWidget(self.tw_estoque)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(13)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setFont(font)
        self.tw_saida.setStyleSheet(u"QTreeWidget::item {\n"
"background-color:rgb(189, 189, 189);\n"
"border-left:1px solid black;\n"
"border: 1px solid black;\n"
"border-bottom:1px solid black;\n"
"}\n"
"QTreeWidget {\n"
"background-color:rgb(189, 189, 189);\n"
"\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_saida = QPushButton(self.frame_2)
        self.btn_saida.setObjectName(u"btn_saida")
        self.btn_saida.setMinimumSize(QSize(100, 91))
        self.btn_saida.setFont(font2)
        self.btn_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saida.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.verticalLayout_3.addWidget(self.btn_saida)

        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 65))
        font6 = QFont()
        font6.setPointSize(9)
        self.label_40.setFont(font6)
        self.label_40.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_3.addWidget(self.label_40)

        self.btn_estornar = QPushButton(self.frame_2)
        self.btn_estornar.setObjectName(u"btn_estornar")
        self.btn_estornar.setMinimumSize(QSize(100, 91))
        self.btn_estornar.setFont(font2)
        self.btn_estornar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estornar.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.verticalLayout_3.addWidget(self.btn_estornar)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tables_2 = QWidget()
        self.tables_2.setObjectName(u"tables_2")
        self.verticalLayout_12 = QVBoxLayout(self.tables_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_4 = QFrame(self.tables_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color:rgb(40, 42, 54);\n"
"\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        font7 = QFont()
        font7.setFamilies([u"Calibri"])
        font7.setPointSize(18)
        self.label_18.setFont(font7)

        self.verticalLayout_13.addWidget(self.label_18)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn_grafico = QPushButton(self.frame_4)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(151, 30))
        self.btn_grafico.setMaximumSize(QSize(177, 41))
        font8 = QFont()
        font8.setFamilies([u"Calibri"])
        font8.setPointSize(14)
        font8.setBold(True)
        self.btn_grafico.setFont(font8)
        self.btn_grafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grafico.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_23.addWidget(self.btn_grafico)

        self.btn_excluir = QPushButton(self.frame_4)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(151, 30))
        self.btn_excluir.setMaximumSize(QSize(177, 41))
        self.btn_excluir.setFont(font8)
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_23.addWidget(self.btn_excluir)

        self.btn_excel = QPushButton(self.frame_4)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(151, 30))
        self.btn_excel.setMaximumSize(QSize(177, 41))
        self.btn_excel.setFont(font8)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_23.addWidget(self.btn_excel)


        self.verticalLayout_13.addLayout(self.horizontalLayout_23)

        self.txt_filtro = QLineEdit(self.frame_4)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMinimumSize(QSize(0, 30))
        font9 = QFont()
        font9.setFamilies([u"Calibri"])
        font9.setPointSize(14)
        self.txt_filtro.setFont(font9)
        self.txt_filtro.setCursor(QCursor(Qt.IBeamCursor))
        self.txt_filtro.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_filtro)

        self.tb_geral = QTableView(self.frame_4)
        self.tb_geral.setObjectName(u"tb_geral")
        self.tb_geral.setMaximumSize(QSize(968, 256))
        self.tb_geral.setStyleSheet(u"background-color:rgb(189, 189, 189)")
        self.tb_geral.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_13.addWidget(self.tb_geral)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tables_2, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.Pages.addWidget(self.page_table)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_34 = QLabel(self.page_home)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"background-color:transparent")

        self.verticalLayout.addWidget(self.label_34)

        self.label_36 = QLabel(self.page_home)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background-color:transparent")
        self.label_36.setPixmap(QPixmap(u"imgs/pngwing.com.png"))

        self.verticalLayout.addWidget(self.label_36, 0, Qt.AlignHCenter)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 300))
        font10 = QFont()
        font10.setFamilies([u"Calibri"])
        font10.setPointSize(8)
        font10.setBold(True)
        self.label.setFont(font10)
        self.label.setStyleSheet(u"background-color:transparent")

        self.verticalLayout.addWidget(self.label)

        self.label_35 = QLabel(self.page_home)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"background-color:transparent")

        self.verticalLayout.addWidget(self.label_35)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.Pages.addWidget(self.page_home)
        self.page_usuarios = QWidget()
        self.page_usuarios.setObjectName(u"page_usuarios")
        self.horizontalLayout_20 = QHBoxLayout(self.page_usuarios)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_5 = QFrame(self.page_usuarios)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 320))
        self.frame_5.setMaximumSize(QSize(800, 671))
        self.frame_5.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.486, y1:0, x2:0.497, y2:1, stop:0 rgba(42, 71, 94, 255), stop:1 rgba(28, 41, 56, 255));\n"
"border-radius:20px\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_56 = QLabel(self.frame_5)
        self.label_56.setObjectName(u"label_56")
        font11 = QFont()
        font11.setFamilies([u"Calibri"])
        font11.setPointSize(19)
        font11.setBold(True)
        self.label_56.setFont(font11)
        self.label_56.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_15.addWidget(self.label_56)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_17.addWidget(self.label_29)

        self.txt_filtro_usuario = QLineEdit(self.frame_5)
        self.txt_filtro_usuario.setObjectName(u"txt_filtro_usuario")
        self.txt_filtro_usuario.setMinimumSize(QSize(0, 30))
        self.txt_filtro_usuario.setMaximumSize(QSize(600, 16777215))
        self.txt_filtro_usuario.setFont(font9)
        self.txt_filtro_usuario.setCursor(QCursor(Qt.IBeamCursor))
        self.txt_filtro_usuario.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px")
        self.txt_filtro_usuario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.txt_filtro_usuario)

        self.label_46 = QLabel(self.frame_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_17.addWidget(self.label_46)


        self.verticalLayout_15.addLayout(self.horizontalLayout_17)

        self.tb_usuarios = QTreeView(self.frame_5)
        self.tb_usuarios.setObjectName(u"tb_usuarios")
        self.tb_usuarios.setMaximumSize(QSize(800, 500))
        self.tb_usuarios.setStyleSheet(u"background-color:rgb(189, 189, 189)")
        self.tb_usuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_15.addWidget(self.tb_usuarios)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_cadastro_usuario = QPushButton(self.frame_5)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")
        self.btn_cadastro_usuario.setMinimumSize(QSize(156, 20))
        self.btn_cadastro_usuario.setMaximumSize(QSize(221, 41))
        self.btn_cadastro_usuario.setFont(font2)
        self.btn_cadastro_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro_usuario.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_cadastro_usuario)

        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 50))
        self.label_24.setMaximumSize(QSize(100, 16777215))
        self.label_24.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_14.addWidget(self.label_24)

        self.btn_excluir_users = QPushButton(self.frame_5)
        self.btn_excluir_users.setObjectName(u"btn_excluir_users")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_excluir_users.sizePolicy().hasHeightForWidth())
        self.btn_excluir_users.setSizePolicy(sizePolicy)
        self.btn_excluir_users.setMinimumSize(QSize(156, 20))
        self.btn_excluir_users.setMaximumSize(QSize(221, 41))
        self.btn_excluir_users.setFont(font2)
        self.btn_excluir_users.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_users.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_excluir_users)

        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 50))
        self.label_25.setMaximumSize(QSize(100, 16777215))
        self.label_25.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_14.addWidget(self.label_25)

        self.btn_atualizar_usuario = QPushButton(self.frame_5)
        self.btn_atualizar_usuario.setObjectName(u"btn_atualizar_usuario")
        self.btn_atualizar_usuario.setMinimumSize(QSize(156, 20))
        self.btn_atualizar_usuario.setMaximumSize(QSize(221, 41))
        self.btn_atualizar_usuario.setFont(font2)
        self.btn_atualizar_usuario.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_atualizar_usuario)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_20.addWidget(self.frame_5)

        self.Pages.addWidget(self.page_usuarios)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_19 = QHBoxLayout(self.page)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(250, 320))
        self.frame_10.setMaximumSize(QSize(500, 671))
        self.frame_10.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.486, y1:0, x2:0.497, y2:1, stop:0 rgba(42, 71, 94, 255), stop:1 rgba(28, 41, 56, 255));\n"
"border-radius:20px\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_107 = QLabel(self.frame_10)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(175, 168))
        self.label_107.setMaximumSize(QSize(175, 168))
        self.label_107.setStyleSheet(u"background-color:transparent")
        self.label_107.setPixmap(QPixmap(u"imgs/male-user-edit_25348.png"))
        self.label_107.setScaledContents(True)
        self.label_107.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_107, 0, Qt.AlignHCenter)

        self.label_108 = QLabel(self.frame_10)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(240, 30))
        self.label_108.setMaximumSize(QSize(16777215, 190))
        self.label_108.setFont(font10)
        self.label_108.setStyleSheet(u"background-color:transparent")
        self.label_108.setScaledContents(True)
        self.label_108.setWordWrap(False)

        self.verticalLayout_16.addWidget(self.label_108)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_109 = QLabel(self.frame_10)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_45.addWidget(self.label_109)

        self.txt_nome_atualizar = QLineEdit(self.frame_10)
        self.txt_nome_atualizar.setObjectName(u"txt_nome_atualizar")
        self.txt_nome_atualizar.setMinimumSize(QSize(0, 30))
        self.txt_nome_atualizar.setMaximumSize(QSize(300, 16777215))
        font12 = QFont()
        font12.setFamilies([u"Calibri"])
        font12.setPointSize(12)
        self.txt_nome_atualizar.setFont(font12)
        self.txt_nome_atualizar.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_nome_atualizar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.txt_nome_atualizar)

        self.label_110 = QLabel(self.frame_10)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_45.addWidget(self.label_110)


        self.verticalLayout_16.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_111 = QLabel(self.frame_10)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_46.addWidget(self.label_111)

        self.txt_usuario_atualizar = QLineEdit(self.frame_10)
        self.txt_usuario_atualizar.setObjectName(u"txt_usuario_atualizar")
        self.txt_usuario_atualizar.setMinimumSize(QSize(0, 30))
        self.txt_usuario_atualizar.setMaximumSize(QSize(300, 16777215))
        self.txt_usuario_atualizar.setFont(font12)
        self.txt_usuario_atualizar.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_usuario_atualizar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.txt_usuario_atualizar)

        self.label_112 = QLabel(self.frame_10)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_46.addWidget(self.label_112)


        self.verticalLayout_16.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_113 = QLabel(self.frame_10)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_47.addWidget(self.label_113)

        self.txt_senha_atualizar = QLineEdit(self.frame_10)
        self.txt_senha_atualizar.setObjectName(u"txt_senha_atualizar")
        self.txt_senha_atualizar.setMinimumSize(QSize(0, 30))
        self.txt_senha_atualizar.setMaximumSize(QSize(300, 16777215))
        self.txt_senha_atualizar.setFont(font12)
        self.txt_senha_atualizar.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_senha_atualizar.setEchoMode(QLineEdit.Password)
        self.txt_senha_atualizar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.txt_senha_atualizar)

        self.label_114 = QLabel(self.frame_10)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_47.addWidget(self.label_114)


        self.verticalLayout_16.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_117 = QLabel(self.frame_10)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMaximumSize(QSize(108, 16777215))
        self.label_117.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_49.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_10)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMaximumSize(QSize(45, 16777215))
        self.label_118.setFont(font5)
        self.label_118.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_49.addWidget(self.label_118)

        self.box_perfil_atualizar = QComboBox(self.frame_10)
        self.box_perfil_atualizar.addItem("")
        self.box_perfil_atualizar.addItem("")
        self.box_perfil_atualizar.setObjectName(u"box_perfil_atualizar")
        self.box_perfil_atualizar.setMinimumSize(QSize(0, 25))
        self.box_perfil_atualizar.setMaximumSize(QSize(300, 16777215))
        font13 = QFont()
        font13.setFamilies([u"Calibri"])
        font13.setPointSize(10)
        self.box_perfil_atualizar.setFont(font13)
        self.box_perfil_atualizar.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.box_perfil_atualizar.setEditable(False)
        self.box_perfil_atualizar.setInsertPolicy(QComboBox.InsertAtBottom)

        self.horizontalLayout_49.addWidget(self.box_perfil_atualizar)

        self.label_119 = QLabel(self.frame_10)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_49.addWidget(self.label_119)


        self.verticalLayout_16.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_120 = QLabel(self.frame_10)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_18.addWidget(self.label_120)

        self.btn_confirmar = QPushButton(self.frame_10)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        sizePolicy.setHeightForWidth(self.btn_confirmar.sizePolicy().hasHeightForWidth())
        self.btn_confirmar.setSizePolicy(sizePolicy)
        self.btn_confirmar.setMinimumSize(QSize(156, 20))
        self.btn_confirmar.setMaximumSize(QSize(221, 41))
        self.btn_confirmar.setFont(font2)
        self.btn_confirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirmar.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_confirmar)

        self.label_123 = QLabel(self.frame_10)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_18.addWidget(self.label_123)

        self.btn_cancelar1 = QPushButton(self.frame_10)
        self.btn_cancelar1.setObjectName(u"btn_cancelar1")
        sizePolicy.setHeightForWidth(self.btn_cancelar1.sizePolicy().hasHeightForWidth())
        self.btn_cancelar1.setSizePolicy(sizePolicy)
        self.btn_cancelar1.setMinimumSize(QSize(156, 20))
        self.btn_cancelar1.setMaximumSize(QSize(221, 41))
        self.btn_cancelar1.setFont(font2)
        self.btn_cancelar1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar1.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_cancelar1)

        self.label_122 = QLabel(self.frame_10)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_18.addWidget(self.label_122)


        self.verticalLayout_16.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_19.addWidget(self.frame_10)

        self.Pages.addWidget(self.page)
        self.page_contato = QWidget()
        self.page_contato.setObjectName(u"page_contato")
        self.verticalLayout_11 = QVBoxLayout(self.page_contato)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_21 = QLabel(self.page_contato)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 140))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_11.addWidget(self.label_21)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_43 = QLabel(self.page_contato)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(241, 0))
        self.label_43.setMaximumSize(QSize(310, 125))
        self.label_43.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_12.addWidget(self.label_43)

        self.label_26 = QLabel(self.page_contato)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(64, 125))
        self.label_26.setStyleSheet(u"background-color:transparent")
        self.label_26.setPixmap(QPixmap(u"imgs/linkedin.png"))

        self.horizontalLayout_12.addWidget(self.label_26)

        self.label_23 = QLabel(self.page_contato)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setMaximumSize(QSize(239, 90))
        self.label_23.setFont(font)
        self.label_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_23.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_12.addWidget(self.label_23)

        self.label_30 = QLabel(self.page_contato)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(241, 0))
        self.label_30.setMaximumSize(QSize(310, 125))
        self.label_30.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_12.addWidget(self.label_30)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_44 = QLabel(self.page_contato)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(241, 0))
        self.label_44.setMaximumSize(QSize(310, 125))
        self.label_44.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_13.addWidget(self.label_44)

        self.label_27 = QLabel(self.page_contato)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(64, 125))
        self.label_27.setStyleSheet(u"background-color:transparent")
        self.label_27.setPixmap(QPixmap(u"imgs/gmail.png"))

        self.horizontalLayout_13.addWidget(self.label_27)

        self.label_28 = QLabel(self.page_contato)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(239, 90))
        self.label_28.setFont(font)
        self.label_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_28.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_13.addWidget(self.label_28)

        self.label_42 = QLabel(self.page_contato)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(241, 0))
        self.label_42.setMaximumSize(QSize(310, 125))
        self.label_42.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_13.addWidget(self.label_42)


        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.label_22 = QLabel(self.page_contato)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 70))
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_11.addWidget(self.label_22)

        self.Pages.addWidget(self.page_contato)
        self.page_cadastro = QWidget()
        self.page_cadastro.setObjectName(u"page_cadastro")
        self.horizontalLayout_15 = QHBoxLayout(self.page_cadastro)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_3 = QFrame(self.page_cadastro)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(250, 320))
        self.frame_3.setMaximumSize(QSize(500, 671))
        self.frame_3.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.486, y1:0, x2:0.497, y2:1, stop:0 rgba(42, 71, 94, 255), stop:1 rgba(28, 41, 56, 255));\n"
"border-radius:20px\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(175, 168))
        self.label_37.setMaximumSize(QSize(175, 168))
        self.label_37.setStyleSheet(u"background-color:transparent")
        self.label_37.setPixmap(QPixmap(u"imgs/male-user-add_25347.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(240, 30))
        self.label_3.setMaximumSize(QSize(16777215, 190))
        self.label_3.setFont(font10)
        self.label_3.setStyleSheet(u"background-color:transparent")
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)

        self.verticalLayout_7.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_5.addWidget(self.label_31)

        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(0, 30))
        self.txt_nome.setMaximumSize(QSize(300, 16777215))
        self.txt_nome.setFont(font12)
        self.txt_nome.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.txt_nome)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_5.addWidget(self.label_17)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_6.addWidget(self.label_16)

        self.txt_usuario = QLineEdit(self.frame_3)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMinimumSize(QSize(0, 30))
        self.txt_usuario.setMaximumSize(QSize(300, 16777215))
        self.txt_usuario.setFont(font12)
        self.txt_usuario.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_usuario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.txt_usuario)

        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_6.addWidget(self.label_15)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.txt_senha = QLineEdit(self.frame_3)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 30))
        self.txt_senha.setMaximumSize(QSize(300, 16777215))
        self.txt_senha.setFont(font12)
        self.txt_senha.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.txt_senha)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_7.addWidget(self.label_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.txt_confirmar_senha = QLineEdit(self.frame_3)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        self.txt_confirmar_senha.setMinimumSize(QSize(0, 30))
        self.txt_confirmar_senha.setMaximumSize(QSize(300, 16777215))
        self.txt_confirmar_senha.setFont(font12)
        self.txt_confirmar_senha.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)
        self.txt_confirmar_senha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.txt_confirmar_senha)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_8.addWidget(self.label_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(108, 16777215))
        self.label_7.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(45, 16777215))
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.box_perfil = QComboBox(self.frame_3)
        self.box_perfil.addItem("")
        self.box_perfil.addItem("")
        self.box_perfil.setObjectName(u"box_perfil")
        self.box_perfil.setMinimumSize(QSize(0, 25))
        self.box_perfil.setMaximumSize(QSize(300, 16777215))
        self.box_perfil.setFont(font13)
        self.box_perfil.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.box_perfil.setEditable(False)
        self.box_perfil.setInsertPolicy(QComboBox.InsertAtBottom)

        self.horizontalLayout_9.addWidget(self.box_perfil)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_9.addWidget(self.label_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_10.addWidget(self.label_32)

        self.btn_cadastrar = QPushButton(self.frame_3)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        sizePolicy.setHeightForWidth(self.btn_cadastrar.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar.setSizePolicy(sizePolicy)
        self.btn_cadastrar.setMinimumSize(QSize(156, 20))
        self.btn_cadastrar.setMaximumSize(QSize(221, 41))
        self.btn_cadastrar.setFont(font2)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_10.addWidget(self.label_33)

        self.btn_cancelar2 = QPushButton(self.frame_3)
        self.btn_cancelar2.setObjectName(u"btn_cancelar2")
        sizePolicy.setHeightForWidth(self.btn_cancelar2.sizePolicy().hasHeightForWidth())
        self.btn_cancelar2.setSizePolicy(sizePolicy)
        self.btn_cancelar2.setMinimumSize(QSize(156, 20))
        self.btn_cancelar2.setMaximumSize(QSize(221, 41))
        self.btn_cancelar2.setFont(font2)
        self.btn_cancelar2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar2.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cancelar2)

        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_10.addWidget(self.label_45)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_15.addWidget(self.frame_3)

        self.Pages.addWidget(self.page_cadastro)
        self.page_importar = QWidget()
        self.page_importar.setObjectName(u"page_importar")
        self.verticalLayout_10 = QVBoxLayout(self.page_importar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_importar)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 300))
        font14 = QFont()
        font14.setFamilies([u"Calibri"])
        font14.setPointSize(9)
        font14.setBold(True)
        self.label_6.setFont(font14)
        self.label_6.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_10.addWidget(self.label_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit = QLineEdit(self.page_importar)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setFont(font5)
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lineEdit)

        self.bnt_open_xml = QPushButton(self.page_importar)
        self.bnt_open_xml.setObjectName(u"bnt_open_xml")
        self.bnt_open_xml.setMinimumSize(QSize(180, 40))
        self.bnt_open_xml.setFont(font12)
        self.bnt_open_xml.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_open_xml.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}")

        self.horizontalLayout_16.addWidget(self.bnt_open_xml)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_9 = QLabel(self.page_importar)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_22.addWidget(self.label_9)

        self.btn_tables_2 = QPushButton(self.page_importar)
        self.btn_tables_2.setObjectName(u"btn_tables_2")
        self.btn_tables_2.setMinimumSize(QSize(150, 30))
        self.btn_tables_2.setMaximumSize(QSize(300, 41))
        self.btn_tables_2.setFont(font12)
        self.btn_tables_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables_2.setStyleSheet(u"QPushButton {\n"
"  color: black;\n"
"  background-color: rgb(255,255,255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
" \n"
"  background-color:rgb(207, 207, 207)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(78, 125, 195);\n"
"  \n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_tables_2)

        self.label_10 = QLabel(self.page_importar)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 100))
        self.label_10.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_22.addWidget(self.label_10)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_39 = QLabel(self.page_importar)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(47, 100))
        self.label_39.setMaximumSize(QSize(16777215, 100))
        self.label_39.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_11.addWidget(self.label_39)

        self.label_38 = QLabel(self.page_importar)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(47, 100))
        self.label_38.setMaximumSize(QSize(16777215, 100))
        self.label_38.setStyleSheet(u"background-color:transparent")

        self.horizontalLayout_11.addWidget(self.label_38)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.Pages.addWidget(self.page_importar)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.verticalLayout_14 = QVBoxLayout(self.page_sobre)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_19 = QLabel(self.page_sobre)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 217))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_14.addWidget(self.label_19)

        self.label_20 = QLabel(self.page_sobre)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 200))
        self.label_20.setFont(font12)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setStyleSheet(u"background-color:transparent")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_20)

        self.label_41 = QLabel(self.page_sobre)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font12)
        self.label_41.setStyleSheet(u"background-color:transparent")

        self.verticalLayout_14.addWidget(self.label_41)

        self.Pages.addWidget(self.page_sobre)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tela Principal", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_outro.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_excluir_usuarios.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIOS", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Estoque</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(14, QCoreApplication.translate("MainWindow", u"Usuario Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Data da Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Valor Produto", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Unidade de medida", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Qntd", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Cod", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Itens da Nota", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"ValorNFe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Nome emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"cnpj emitente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data emissao", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Sa\u00edda</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data Sa\u00edda", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.btn_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar saida", None))
        self.label_40.setText("")
        self.btn_estornar.setText(QCoreApplication.translate("MainWindow", u"Estornar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; text-decoration: underline; color:#ffffff;\">GERAL</span></p></body></html>", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir NFe", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setText("")
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar N\u00famero da NFe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables_2), QCoreApplication.translate("MainWindow", u"Geral", None))
        self.label_34.setText("")
        self.label_36.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">SISTEMA DE GERENCIAMENTO DE ESTOQUE</span></p></body></html>", None))
        self.label_35.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">USU\u00c1RIOS</span></p></body></html>", None))
        self.label_29.setText("")
        self.txt_filtro_usuario.setText("")
        self.txt_filtro_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar Usu\u00e1rio", None))
        self.label_46.setText("")
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.label_24.setText("")
        self.btn_excluir_users.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR USU\u00c1RIO", None))
        self.label_25.setText("")
        self.btn_atualizar_usuario.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR USU\u00c1RIO", None))
        self.label_107.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Atualizar dados do  Usu\u00e1rio</span><span style=\" color:#ffffff;\"><br/></span></p></body></html>", None))
        self.label_109.setText("")
        self.txt_nome_atualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_110.setText("")
        self.label_111.setText("")
        self.txt_usuario_atualizar.setText("")
        self.txt_usuario_atualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None))
        self.label_112.setText("")
        self.label_113.setText("")
        self.txt_senha_atualizar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.label_114.setText("")
        self.label_117.setText("")
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Perf\u00edl:</span></p></body></html>", None))
        self.box_perfil_atualizar.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.box_perfil_atualizar.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_119.setText("")
        self.label_120.setText("")
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.label_123.setText("")
        self.btn_cancelar1.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_122.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; text-decoration: underline; color:#ffffff;\">CONTATOS</span></p></body></html>", None))
        self.label_43.setText("")
        self.label_26.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span><a href=\"https://www.linkedin.com/in/lucas-martins-100596203/\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">linkedin.com/in/lucas-martins-100596203/</span></a></p></body></html>", None))
        self.label_30.setText("")
        self.label_44.setText("")
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://criarmeulink.com.br/u/1705351867\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">lmartins763@gmail.com</span></a></p></body></html>", None))
        self.label_42.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Desenvolvedor: </span><span style=\" font-size:24pt; color:#ffffff;\">Lucas Martins</span></p></body></html>", None))
        self.label_37.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Cadastro de Usu\u00e1rio</span><span style=\" color:#ffffff;\"><br/></span></p></body></html>", None))
        self.label_31.setText("")
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_17.setText("")
        self.label_16.setText("")
        self.txt_usuario.setText("")
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None))
        self.label_15.setText("")
        self.label_14.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.label_13.setText("")
        self.label_12.setText("")
        self.txt_confirmar_senha.setText("")
        self.txt_confirmar_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CONFIRMAR SENHA", None))
        self.label_11.setText("")
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Perf\u00edl:</span></p></body></html>", None))
        self.box_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.box_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_8.setText("")
        self.label_32.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_33.setText("")
        self.btn_cancelar2.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_45.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; text-decoration: underline; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML --->", None))
        self.bnt_open_xml.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.label_9.setText("")
        self.btn_tables_2.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_10.setText("")
        self.label_39.setText("")
        self.label_38.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; text-decoration: underline; color:#ffffff;\">SOBRE</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Este sistema faz a importa\u00e7\u00e3o de arquivos XML e faz o controle do estoque de acordo com a entrada de notas e sa\u00eddas apontadas pelo usu\u00e1rio.</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ff0000;\">Permiss\u00f5es do Administrador: </span><span style=\" font-size:20pt; color:#ffffff;\">Cadastrar/Excluir/Alterar Dados do Usu\u00e1rios, Cadastrar NFes, </span></p><p><span style=\" font-size:20pt; color:#ffffff;\">Gerar Sa\u00eddas, Excluir sa\u00eddas, Excluir NFes do Banco de Dados.</span></p><p><span style=\" font-size:20pt; color:#ff0000;\">Permiss\u00f5es do Usu\u00e1rio: </span><span style=\" font-size:20pt; color:#ffffff;\">Cadastrar NFes, Gerar Sa\u00eddas.</span></p></body></html>", None))
    # retranslateUi

