import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):  # se crea pantalla principal
    def __init__(self):  # creamos el init de MainWindow
        super().__init__()  # ejecutamos el init eredado de QMainWindows
        self.setWindowTitle('Ventana Principal')  # le ponemos un titulo
        self.setMinimumSize(QSize(480, 320))  # le damos un tamaño
        texto = QLineEdit()  # creamos un QLineEdit
        texto.textChanged.connect(self.texto_modificado)
        ''' cuando cambia texto llamamos a texto_modificado'''
        self.setCentralWidget(texto)  # ubicamos a texto en el Widget central
        self.texto = texto  # creamos puntero para acceder al Widget desde un método externo

    def texto_modificado(self):
        '''captura el texto del interior de QLinEdit
        y lo pasa al titulo modificandolo  '''
        texto_recuperado = self.texto.text()  # capuramos texto
        self.setWindowTitle(texto_recuperado)  # modificamos titulo


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
