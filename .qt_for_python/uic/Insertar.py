# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Insertar.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_InsercionDatosBDDialog(object):
    def setupUi(self, InsercionDatosBDDialog):
        if not InsercionDatosBDDialog.objectName():
            InsercionDatosBDDialog.setObjectName(u"InsercionDatosBDDialog")
        InsercionDatosBDDialog.resize(465, 207)
        self.lbl_nombre_base_datos = QLabel(InsercionDatosBDDialog)
        self.lbl_nombre_base_datos.setObjectName(u"lbl_nombre_base_datos")
        self.lbl_nombre_base_datos.setGeometry(QRect(20, 20, 191, 20))
        self.layoutWidget = QWidget(InsercionDatosBDDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(210, 20, 211, 51))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_nombre_base_datos = QLineEdit(self.layoutWidget)
        self.txt_nombre_base_datos.setObjectName(u"txt_nombre_base_datos")

        self.verticalLayout.addWidget(self.txt_nombre_base_datos)

        self.btn_conectar = QPushButton(self.layoutWidget)
        self.btn_conectar.setObjectName(u"btn_conectar")

        self.verticalLayout.addWidget(self.btn_conectar)

        self.widget = QWidget(InsercionDatosBDDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 91, 181, 71))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_nombre_tabla = QLabel(self.widget)
        self.lbl_nombre_tabla.setObjectName(u"lbl_nombre_tabla")

        self.verticalLayout_3.addWidget(self.lbl_nombre_tabla)

        self.lbl_id = QLabel(self.widget)
        self.lbl_id.setObjectName(u"lbl_id")

        self.verticalLayout_3.addWidget(self.lbl_id)

        self.lbl_nombre = QLabel(self.widget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")

        self.verticalLayout_3.addWidget(self.lbl_nombre)

        self.widget1 = QWidget(InsercionDatosBDDialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(210, 90, 211, 103))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.txt_nombre_tabla = QLineEdit(self.widget1)
        self.txt_nombre_tabla.setObjectName(u"txt_nombre_tabla")

        self.verticalLayout_2.addWidget(self.txt_nombre_tabla)

        self.txt_id = QLineEdit(self.widget1)
        self.txt_id.setObjectName(u"txt_id")

        self.verticalLayout_2.addWidget(self.txt_id)

        self.txt_nombre = QLineEdit(self.widget1)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.verticalLayout_2.addWidget(self.txt_nombre)

        self.btn_insertar_registro = QPushButton(self.widget1)
        self.btn_insertar_registro.setObjectName(u"btn_insertar_registro")

        self.verticalLayout_2.addWidget(self.btn_insertar_registro)


        self.retranslateUi(InsercionDatosBDDialog)

        QMetaObject.connectSlotsByName(InsercionDatosBDDialog)
    # setupUi

    def retranslateUi(self, InsercionDatosBDDialog):
        InsercionDatosBDDialog.setWindowTitle(QCoreApplication.translate("InsercionDatosBDDialog", u"Dialog", None))
        self.lbl_nombre_base_datos.setText(QCoreApplication.translate("InsercionDatosBDDialog", u"Nombre de la base de datos:", None))
        self.btn_conectar.setText(QCoreApplication.translate("InsercionDatosBDDialog", u"Conectar", None))
        self.lbl_nombre_tabla.setText(QCoreApplication.translate("InsercionDatosBDDialog", u"Nombre de tabla:", None))
        self.lbl_id.setText(QCoreApplication.translate("InsercionDatosBDDialog", u"ID:", None))
        self.lbl_nombre.setText(QCoreApplication.translate("InsercionDatosBDDialog", u"Nombre", None))
        self.btn_insertar_registro.setText(QCoreApplication.translate("InsercionDatosBDDialog", u"Insertar Registro", None))
    # retranslateUi

