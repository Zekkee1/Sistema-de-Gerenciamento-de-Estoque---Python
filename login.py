# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(585, 571)
        Login.setMinimumSize(QSize(518, 0))
        Login.setMaximumSize(QSize(585, 571))
        icon = QIcon()
        icon.addFile(u"imgs/kisspng-inventory-management-stock-taking-clip-art-service-icon-5aead231daa902.8297761415253386738956.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.486, y1:0, x2:0.497, y2:1, stop:0 rgba(42, 71, 94, 255), stop:1 rgba(28, 41, 56, 255))")
        self.horizontalLayout = QHBoxLayout(Login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 500))
        self.frame.setMaximumSize(QSize(500, 500))
        font = QFont()
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0.557, x2:1, y2:0.545, stop:0 rgba(6, 191, 255, 255), stop:1 rgba(45, 115, 255, 255));\n"
"border-radius:85px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(187, 40))
        font1 = QFont()
        font1.setPointSize(23)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color:transparent\n"
"")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setCursor(QCursor(Qt.ArrowCursor))
        self.label.setStyleSheet(u"background-color:transparent")
        self.label.setPixmap(QPixmap(u"imgs/pngegg.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.txt_username = QLineEdit(self.frame)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setMaximumSize(QSize(300, 30))
        font2 = QFont()
        font2.setPointSize(11)
        self.txt_username.setFont(font2)
        self.txt_username.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_username, 0, Qt.AlignHCenter)

        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setMaximumSize(QSize(300, 30))
        self.txt_password.setFont(font2)
        self.txt_password.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"}")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_password, 0, Qt.AlignHCenter)

        self.botton_login = QPushButton(self.frame)
        self.botton_login.setObjectName(u"botton_login")
        self.botton_login.setMinimumSize(QSize(100, 0))
        self.botton_login.setMaximumSize(QSize(200, 25))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.botton_login.setFont(font3)
        self.botton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.botton_login.setStyleSheet(u"QPushButton {\n"
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
        self.botton_login.setIconSize(QSize(16, 16))
        self.botton_login.setCheckable(False)

        self.verticalLayout.addWidget(self.botton_login, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"BEM-VINDO", None))
        self.label.setText("")
        self.txt_username.setPlaceholderText(QCoreApplication.translate("Login", u"USERNAME", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"SENHA", None))
        self.botton_login.setText(QCoreApplication.translate("Login", u"LOGIN", None))
    # retranslateUi

