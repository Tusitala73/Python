# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'primera_app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Imagenes import source

class Ui_Contadordeclicks(object):
    def setupUi(self, Contadordeclicks):
        if not Contadordeclicks.objectName():
            Contadordeclicks.setObjectName(u"Contadordeclicks")
        Contadordeclicks.resize(202, 382)
        self.titulo = QLabel(Contadordeclicks)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(0, 20, 201, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.contador = QLabel(Contadordeclicks)
        self.contador.setObjectName(u"contador")
        self.contador.setGeometry(QRect(50, 60, 91, 71))
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(50)
        font1.setBold(True)
        font1.setWeight(75)
        self.contador.setFont(font1)
        self.contador.setFrameShape(QFrame.Box)
        self.contador.setAlignment(Qt.AlignCenter)
        self.btnClick = QPushButton(Contadordeclicks)
        self.btnClick.setObjectName(u"btnClick")
        self.btnClick.setGeometry(QRect(60, 150, 71, 23))
        self.label_3 = QLabel(Contadordeclicks)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 190, 111, 171))
        self.label_3.setPixmap(QPixmap(u":/Imagenes/479px-Th\u00e9ophile-Alexandre_Steinlen_-_Tourn\u00e9e_du_Chat_Noir_de_Rodolphe_Salis_(Tour_of_Rodolphe_Salis'_Chat_Noir)_-_Google_Art_Project.jpg"))
        self.label_3.setScaledContents(True)

        self.retranslateUi(Contadordeclicks)

        QMetaObject.connectSlotsByName(Contadordeclicks)
    # setupUi

    def retranslateUi(self, Contadordeclicks):
        Contadordeclicks.setWindowTitle(QCoreApplication.translate("Contadordeclicks", u"Contador de clicks", None))
        self.titulo.setText(QCoreApplication.translate("Contadordeclicks", u"Contador de Click", None))
        self.contador.setText(QCoreApplication.translate("Contadordeclicks", u"0", None))
        self.btnClick.setText(QCoreApplication.translate("Contadordeclicks", u"Haz Click", None))
        self.label_3.setText("")
    # retranslateUi

