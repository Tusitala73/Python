from PyQt5.QtWidgets import *
from Vista.ui_editor import Ui_editor
import sys, eventos

class Editor(QMainWindow):
    
    def __init__(self):
        super(Editor, self).__init__()
        self.editor = Ui_editor()
        self.editor.setupUi(self)
        self.titulo = "Editor de Texto"
        self.ruta = ""
        self.control = 0                
        
    #--- Eventos propios --- 
        self.editor.textEdit.textChanged.connect(self.textChanged)
        

    #--- Eventos externos ---
        self.editor.actionAbrir.triggered.connect(lambda: )
        

    def textChanged(self):
        if self.titulo == "Editor de Texto" or self.titulo == "Editor de Texto - *":
            self.setWindowTitle("Editor de Texto - *")
        else:
            self.setWindowTitle(self.titulo)
            
    def abrirArchivo(self):
        self.ruta = eventos.abrirArchivo(
            QFileDialog(),
            self.editor.textEdit,
            self
        )
        self.titulo = f"editor de texto - {self.ruta}"
        

if __name__ == "__main__":
    app =QApplication(sys.argv)
    mi_aplicacion = Editor()
    mi_aplicacion.show()
    sys.exit(app.exec_())