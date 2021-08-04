import sys
import sqlite3
import re
import os
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from ConsultaBaseDatosDialog import ConsultaBaseDatosDialog
from sqlite3 import Error


class ConsultaBaseDatosAplicacion(QDialog):
    def __init__(self):
        super().__init__()

        patron = '[a-zA-Z]+'
        self.validador = re.compile(patron)

        self.mensajes = QMessageBox()
        self.mensajes.setWindowTitle('Mensajes')

        self.ui = ConsultaBaseDatosDialog()
        self.ui.setupUi(self)

        self.ui.btn_concultar_datos.clicked.connect(self.consultar_datatos)

        self.show()

    def consultar_datatos(self):
        nombre_bd = self.ui.txt_nombre_base_datos.text().strip()

        if self.validador.match(nombre_bd) is not None:
            nombre_bd = nombre_bd + '.db'

            if os.path.exists(nombre_bd):
                nombre_tabla = self.ui.txt_nombre_tabla.text().strip()
                if self.validador.match(nombre_tabla) is not None:
                    try:
                        conexion = sqlite3.connect(nombre_bd)
                        cur = conexion.cursor()

                        sql = '''SELECT * FROM {}'''.format(nombre_tabla)

                        productos = cur.execute(sql).fetchall()

                        if len(productos) > 0:
                            fila = 0

                            for p in productos:
                                columna = 0
                                for c in p:
                                    celda = QTableWidgetItem(c)
                                    self.ui.tbl_datos.setItem(fila, columna, celda)
                                    columna += 1

                                fila += 1 

                        else:
                            self.mensajes.setText('La tabla no tiene ningún registro')
                            self.mensajes.setIcon(QMessageBox.Warning)
                            self.mensajes.exec()

                    except Error as e:
                        self.mensajes.setText('La tabla indicada no existe')
                        self.mensajes.setIcon(QMessageBox.Warning)
                        self.mensajes.exec()
                    finally:
                        conexion.close()

                else:
                    self.mensajes.setText('Debe de introducir un nombre valido para la Tabla')
                    self.mensajes.setIcon(QMessageBox.Warning)
                    self.mensajes.exec()

            else:
                self.mensajes.setText('La base de datos no existe')
                self.mensajes.setIcon(QMessageBox.Warning)
                self.mensajes.exec()        
        else:          
            self.mensajes.setText('Debe de introducir un nombre valido para la base de datos')
            self.mensajes.setIcon(QMessageBox.Warning)
            self.mensajes.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ventana = ConsultaBaseDatosAplicacion()
    Ventana.show()

    sys.exit(app.exec())