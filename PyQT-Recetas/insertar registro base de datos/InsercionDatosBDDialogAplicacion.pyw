import sys
import sqlite3
import re
import os
from sqlite3 import Error
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from InsercionDatosBDDialog import InsercionDatosBDDialog
# from directorio import absPath


class InsercionDatosBDAplicacion(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = InsercionDatosBDDialog()
        self.ui.setupUi(self)

        patron = '[a-zA-Z]+'
        self.regex = re.compile(patron)

        patron = '[1-9]{1}[0-9]*'
        self.regex_numero = re.compile(patron)

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
        nombre_bd = self.ui.txt_nombre_base_datos.text().strip()  # captura el texto del line edit y le quita los espacios del inicio y final con .sprip

        if self.regex.match(nombre_bd) is not None:
            nombre_bd = nombre_bd + '.db'
            if os.path.exists(nombre_bd):
                try:
                    self.conexion = sqlite3.connect(nombre_bd)
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
                    self.mensajes.setText('No se puede abrir la base de datos' + str(error))
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
        nombre_tabla = self.ui.txt_nombre_tabla().strip()

        if self.regex.match(nombre_tabla) is not None:
            valor_id = self.ui.txt_id().strip()

            if self.regex_numero.match(valor_id) is not None:
                if not self.existe_id(nombre_tabla, valor_id):
                    nombre_producto = self.ui.txt_nombre.text().strip()
                    if self.regex.match(nombre_producto) is not None:
                        sql = '''INSERT INTO {} VALUES({}, {})'''.format(nombre_tabla, valor_id, nombre_producto)
                        cur = self.conexion.cursor()
                        cur.execute(sql)
                        self.conexion.commit()

                    else:
                        self.mensajes.setText('debe de introducir un nombre de producto valido')
                        self.mensajes.setIcon(QMessageBox.Warning)
                        self.mensajes.exec()

                else:
                    self.mensajes.setText('ese ID ya existe en la base de datos')
                    self.mensajes.setIcon(QMessageBox.Warning)
                    self.mensajes.exec()
            else:
                self.mensajes.setText('Debe de escribir un Id valido')
                self.mensajes.setIcon(QMessageBox.Warning)
                self.mensajes.exec()

        else:
            self.mensajes.setText('Debe de escribir un nombre valido para la tabla')
            self.mensajes.setIcon(QMessageBox.Warning)
            self.mensajes.exec()

    def existe_id(self, tabla, valor_id):
        sql = '''SELECT * FROM {} WHERE id = {}'''.format(tabla, valor_id)
        cur = self.conexion.cursor()
        resultado = cur.execute(sql).fetchall()

        return len(resultado) > 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = InsercionDatosBDAplicacion()
    ventana.show()

    sys.exit(app.exec())
