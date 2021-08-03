# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsultaBaseDatosDialogRYVZHm.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class ConsultaBaseDatosDialog(object):
    def setupUi(self, ConsultaBaseDatosDialog):
        if not ConsultaBaseDatosDialog.objectName():
            ConsultaBaseDatosDialog.setObjectName(u"ConsultaBaseDatosDialog")
        ConsultaBaseDatosDialog.resize(439, 349)
        self.lbl_nombre_base_datos = QLabel(ConsultaBaseDatosDialog)
        self.lbl_nombre_base_datos.setObjectName(u"lbl_nombre_base_datos")
        self.lbl_nombre_base_datos.setGeometry(QRect(20, 34, 131, 16))
        self.txt_nombre_base_datos = QLineEdit(ConsultaBaseDatosDialog)
        self.txt_nombre_base_datos.setObjectName(u"txt_nombre_base_datos")
        self.txt_nombre_base_datos.setGeometry(QRect(180, 30, 241, 22))
        self.lbl_nombre_tabla = QLabel(ConsultaBaseDatosDialog)
        self.lbl_nombre_tabla.setObjectName(u"lbl_nombre_tabla")
        self.lbl_nombre_tabla.setGeometry(QRect(20, 63, 91, 16))
        self.txt_nombre_tabla = QLineEdit(ConsultaBaseDatosDialog)
        self.txt_nombre_tabla.setObjectName(u"txt_nombre_tabla")
        self.txt_nombre_tabla.setGeometry(QRect(180, 60, 241, 22))
        self.btn_concultar_datos = QPushButton(ConsultaBaseDatosDialog)
        self.btn_concultar_datos.setObjectName(u"btn_concultar_datos")
        self.btn_concultar_datos.setGeometry(QRect(180, 90, 241, 24))
        self.tbl_datos = QTableWidget(ConsultaBaseDatosDialog)
        if (self.tbl_datos.columnCount() < 2):
            self.tbl_datos.setColumnCount(2)
        if (self.tbl_datos.rowCount() < 3):
            self.tbl_datos.setRowCount(3)
        self.tbl_datos.setObjectName(u"tbl_datos")
        self.tbl_datos.setGeometry(QRect(10, 130, 411, 181))
        self.tbl_datos.setRowCount(3)
        self.tbl_datos.setColumnCount(2)

        self.retranslateUi(ConsultaBaseDatosDialog)

        QMetaObject.connectSlotsByName(ConsultaBaseDatosDialog)
    # setupUi

    def retranslateUi(self, ConsultaBaseDatosDialog):
        ConsultaBaseDatosDialog.setWindowTitle(QCoreApplication.translate("ConsultaBaseDatosDialog", u"SQLite: Consulta de Datos", None))
        self.lbl_nombre_base_datos.setText(QCoreApplication.translate("ConsultaBaseDatosDialog", u"Nombre base de datos:", None))
        self.lbl_nombre_tabla.setText(QCoreApplication.translate("ConsultaBaseDatosDialog", u"Nombre Tabla:", None))
        self.btn_concultar_datos.setText(QCoreApplication.translate("ConsultaBaseDatosDialog", u"Consultar datos", None))
    # retranslateUi

