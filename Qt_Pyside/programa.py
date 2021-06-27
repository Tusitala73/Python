import sys
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Principal')
        boton = QPushButton('BOTON GORDO')
        self.setCentralWidget(boton)
        self.setMinimumSize(QSize(480, 320))
        # boton.clicked.connect(self.boton_clicado)
        # boton.pressed.connect(self.boton_presionado)
        # boton.released.connect(self.boton_liberado)
        boton.setCheckable(True)  # este método convierte el boton de un pulsador a un interruptor devuelve un valor de True o False
        boton.clicked.connect(self.boton_alternado)

    def boton_clicado(self):
        print("el boton esta siendo pulsado")

    def boton_presionado(self):
        print("el boton esta siendo presionado")

    def boton_liberado(self):
        print("el boton se a soltado")

    def boton_alternado(self, valor):
        print("boton alternado?", valor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
