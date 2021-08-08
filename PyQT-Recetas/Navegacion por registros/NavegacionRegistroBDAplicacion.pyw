import sys
import sqlite3
from sqlite3 import Error
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from NavegacionRegistrosBDDialog import NavegacionRegistrosBDDialog


class NavegacionRegistrosBDAplicacion(QDialog):

    def __init__(self):
        super().__init__()

        self.mensajes = QMessageBox()
        self.mensajes.setWindowTitle('Mensaje')

        self.ui = NavegacionRegistrosBDDialog()
        self.ui.setupUi(self)

        self.ui.btn_primero.clicked.connect(self.primer_registro)
        self.ui.btn_anterior.clicked.connect(self.anterior_registro)
        self.ui.btn_sigiente.clicked.connect(self.siguiente_registro)
        self.ui.btn_ultimo.clicked.connect(self.ultimo_registro)

        self.ui.btn_primero.setEnabled(False)
        self.ui.btn_anterior.setEnabled(False)
        self.ui.btn_sigiente.setEnabled(False)
        self.ui.btn_ultimo.setEnabled(False)

        self.conexion = None
        self.total_registros = 0
        self.registro = 1
        self.conectar_bd()
        self.primer_registro()

        self.show()

    def conectar_bd(self):
        try:
            self.conexion = sqlite3.connect('clientes.db')

            sql = "SELECT * FROM producto"
            cur = self.conexion.cursor()
            self.total_registros = len(cur.execute(sql).fetchall())

            self.ui.btn_primero.setEnabled(True)
            self.ui.btn_anterior.setEnabled(True)
            self.ui.btn_sigiente.setEnabled(True)
            self.ui.btn_ultimo.setEnabled(True)

        except Error:
            self.mensajes.setText('No se ha podido realizar la conexion a la Base de Datos')
            self.mensajes.setIcon(QMessageBox.Warning)
            self.mensajes.exec()

    def primer_registro(self):
        sql = '''SELECT id, nombre FROM producto LIMIT 1'''
        cur = self.conexion.cursor()
        producto = cur.execute(sql).fetchone()
        if len(producto) > 0:
            self.registro = 1
            self.ui.txt_id.setText(str(producto[0]))
            self.ui.txt_nombre.setText(str(producto[1]))
        else:
            self.mensajes.setText('No hay articulos en la Base de Datos')
            self.mensajes.setIcon(QMessageBox.Warning)
            self.mensajes.exec()

    def anterior_registro(self):
        self.registro -= 1
        if self.registro > 0:
            sql = '''SELECT id, nombre FROM producto LIMIT 1 OFFSET ?'''
            cur = self.conexion.cursor()
            producto = cur.execute(sql, (self.registro - 1, )).fetchone()
            self.ui.txt_id.setText(str(producto[0]))
            self.ui.txt_nombre.setText(str(producto[1]))

        else:
            self.ultimo_registro()

    def siguiente_registro(self):
        if self.registro < self.total_registros:
            sql = '''SELECT id, nombre FROM producto LIMIT 1 OFFSET ?'''
            cur = self.conexion.cursor()
            producto = cur.execute(sql, (self.registro, )).fetchone()
            self.ui.txt_id.setText(str(producto[0]))
            self.ui.txt_nombre.setText(str(producto[1]))
            self.registro += 1

        else:
            self.primer_registro()

    def ultimo_registro(self):
        sql = '''SELECT id, nombre FROM producto ORDER BY id DESC LIMIT 1'''
        cur = self.conexion.cursor()
        producto = cur.execute(sql).fetchone()
        self.registro = self.total_registros
        self.ui.txt_id.setText(str(producto[0]))
        self.ui.txt_nombre.setText(str(producto[1]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = NavegacionRegistrosBDAplicacion()
    ventana.show()

    sys.exit(app.exec())
