# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NavegacionRegistrosBDDialoglWLklz.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class NavegacionRegistrosBDDialog(object):
    def setupUi(self, NavegacionRegistrosBDDialog):
        if not NavegacionRegistrosBDDialog.objectName():
            NavegacionRegistrosBDDialog.setObjectName(u"NavegacionRegistrosBDDialog")
        NavegacionRegistrosBDDialog.resize(442, 159)
        self.lbl_id = QLabel(NavegacionRegistrosBDDialog)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setGeometry(QRect(20, 20, 31, 16))
        self.txt_id = QLineEdit(NavegacionRegistrosBDDialog)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setGeometry(QRect(140, 20, 281, 22))
        self.txt_id.setReadOnly(True)
        self.lbl_nombre = QLabel(NavegacionRegistrosBDDialog)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(21, 54, 49, 16))
        self.txt_nombre = QLineEdit(NavegacionRegistrosBDDialog)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(140, 50, 281, 22))
        self.txt_nombre.setReadOnly(True)
        self.horizontalLayoutWidget = QWidget(NavegacionRegistrosBDDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 80, 401, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_primero = QPushButton(self.horizontalLayoutWidget)
        self.btn_primero.setObjectName(u"btn_primero")

        self.horizontalLayout.addWidget(self.btn_primero)

        self.btn_anterior = QPushButton(self.horizontalLayoutWidget)
        self.btn_anterior.setObjectName(u"btn_anterior")

        self.horizontalLayout.addWidget(self.btn_anterior)

        self.btn_sigiente = QPushButton(self.horizontalLayoutWidget)
        self.btn_sigiente.setObjectName(u"btn_sigiente")

        self.horizontalLayout.addWidget(self.btn_sigiente)

        self.btn_ultimo = QPushButton(self.horizontalLayoutWidget)
        self.btn_ultimo.setObjectName(u"btn_ultimo")

        self.horizontalLayout.addWidget(self.btn_ultimo)


        self.retranslateUi(NavegacionRegistrosBDDialog)

        QMetaObject.connectSlotsByName(NavegacionRegistrosBDDialog)
    # setupUi

    def retranslateUi(self, NavegacionRegistrosBDDialog):
        NavegacionRegistrosBDDialog.setWindowTitle(QCoreApplication.translate("NavegacionRegistrosBDDialog", u"SQLite: Navegacion de R.egistros", None))
        self.lbl_id.setText(QCoreApplication.translate("NavegacionRegistrosBDDialog", u"ID:", None))
        self.lbl_nombre.setText(QCoreApplication.translate("NavegacionRegistrosBDDialog", u"Nombre", None))
        self.btn_primero.setText(QCoreApplication.translate("NavegacionRegistrosBDDialog", u"Primero", None))
        self.btn_anterior.setText(QCoreApplication.translate("NavegacionRegistrosBDDialog", u"Anterior", None))
        self.btn_sigiente.setText(QCoreApplication.translate("NavegacionRegistrosBDDialog", u"Siguiente", None))
        self.btn_ultimo.setText(QCoreApplication.translate("NavegacionRegistrosBDDialog", u"\u00daltimo", None))
    # retranslateUi

