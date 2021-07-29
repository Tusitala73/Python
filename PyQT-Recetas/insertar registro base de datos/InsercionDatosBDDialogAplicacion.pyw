import sys
import sqlite3
import re
import os
from sqlite3 import Error
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from InsercionDatosBDDialog import InsercionDatosBDDialog
from directorio import absPath


class InsercionDatosBDAplicacion(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = InsercionDatosBDDialog()
        self.ui.setupUi(self)

        patron = '[a-zA-Z]+'
        self.regex = re.compile(patron)

        self.ui.btn_conectar.clicked.connect(self.conectar)
        self.ui.btn_insertar_registro.clicked.connect(self.insertar)

        self.ui.txt_nombre_tabla.setEnabled(False)
        self.ui.txt_id.setEnabled(False)
        self.ui.txt_nombre.setEnabled(False)
        self.ui.btn_insertar_registro.setEnabled(False)

        self.mensajes = QMessageBox()
        self.setWindowTitle('Mensajes')
        self.conexion = None

        self.show()

    def conectar(self):
        nombre_bd = self.ui.txt_nombre_base_datos.text().strip()

        if self.regex.match(nombre_bd) is not None:
            nombre_bd = nombre_bd + '.db'
            if os.path.exists(nombre_bd):
                try:
                    self.conexion = sqlite3.connect(absPath("nombre_bd"))
                    self.mensajes.setText('la conexion se realizo correctamente')
                    self.mensajes.setIcon(QMessageBox.Information)
                    self.mensajes.exec()

                    self.ui.txt_id.setEnabled(True)
                    self.ui.txt_nombre_tabla.setEnabled(True)
                    self.ui.txt_nombre.setEnabled(True)
                    self.ui.btn_insertar_registro.setEnabled(True)

                    self.ui.btn_conectar.setEnabled(False)
                    self.ui.txt_nombre_base_datos.setEnabled(False)

                except Error as error:
                    self.mensajes.setText('No se puede abrir la base de datos')
                    self.mensajes.setIcon(QMessageBox.Warning)
                    self.mensajes.exec()
            else:
                self.mensajes.setText('No existe la base de datos: {}'.format(nombre_bd))
                self.mensajes.setIcon(QMessageBox.Warning)
                self.mensajes.exec()
        else:
            self.mensajes.setText('Debe de escribir un nombre valido para la base de datos')
            self.mensajes.setIcon(QMessageBox.Warning)
            self.mensajes.exec()

    def insertar(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = InsercionDatosBDAplicacion()
    ventana.show()

    sys.exit(app.exec())
