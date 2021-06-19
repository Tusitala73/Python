from PyQt5.QtWidgets  import *
from Vista.ui_calculadora import Ui_Calculadora
import sys, eventos

class Calculadora(QDialog):

    
    def __init__(self):
        super(Calculadora, self).__init__()
        self.calculadora = Ui_Calculadora()
        self.calculadora.setupUi(self)
        
        # -- Button: clicked ---
        '''
         Al clicar el boton lo conecta con una función lambda  que llama a 
         la función btnClicled y le pasa como argumento el string que identifica el boton
        '''
        self.calculadora.btn1.clicked.connect(lambda: self.btnClicked("1"))
        self.calculadora.btn2.clicked.connect(lambda: self.btnClicked("2"))
        self.calculadora.btn3.clicked.connect(lambda: self.btnClicked("3"))
        self.calculadora.btn4.clicked.connect(lambda: self.btnClicked("4"))
        self.calculadora.btn5.clicked.connect(lambda: self.btnClicked("5"))
        self.calculadora.btn6.clicked.connect(lambda: self.btnClicked("6"))
        self.calculadora.btn7.clicked.connect(lambda: self.btnClicked("7"))
        self.calculadora.btn8.clicked.connect(lambda: self.btnClicked("8"))
        self.calculadora.btn9.clicked.connect(lambda: self.btnClicked("9"))
        self.calculadora.btn0.clicked.connect(lambda: self.btnClicked("0"))
        self.calculadora.btnSumar.clicked.connect(lambda: self.btnClicked("+"))
        self.calculadora.btnRestar.clicked.connect(lambda: self.btnClicked("-"))
        self.calculadora.btnMultiplicar.clicked.connect(lambda: self.btnClicked("*"))
        self.calculadora.btnDividir.clicked.connect(lambda: self.btnClicked("/"))
        self.calculadora.btnPA.clicked.connect(lambda: self.btnClicked("("))
        self.calculadora.btnPC.clicked.connect(lambda: self.btnClicked(")"))
        self.calculadora.btnPunto.clicked.connect(lambda: self.btnClicked("."))
        self.calculadora.btnC.clicked.connect(lambda: self.btnClicked("C"))
        self.calculadora.btnIgual.clicked.connect(lambda: self.btnClicked("="))      
    
    
    def keyPressEvent(self, event):
        '''
        keyPressEvent hace que al pulsar una tecla se pase el texto y la key de a misma en los argumentos 

        Args:
            event ([]): se pasa la key y texto de de la tecla pulsada
        '''
        self.validarLabel()
        eventos.teclas(
            event, 
            self.calculadora.label,
            self.calculadora.lineEdit,
        ) # manda  a eventos la función teclas y le pasa los distintos  argumentos 
    
    def btnClicked(self, boton):
        '''
        btnClicked recibe los argumentos de la función lambda de click.connect          

        Args:
            boton ([string]): [con el valor del la tecla que se pulsa]
        '''
        self.validarLabel()
        texto = self.calculadora.label.text() # captura el valor de label y lo pasa a variable texto
        
        if ((boton.isnumeric() == True) or (boton.isalnum() == False) and boton != "="): #? repasar lógica condicional
            self.calculadora.label.setText(texto + boton) # escribe el texto
        
        elif boton == "C":
            self.calculadora.label.setText(texto[:-1]) # borra texto
        
        elif boton == "=":
            self.calculadora.lineEdit.clear() #borra el resultado anterior
            
            try:#comprueba si la siguiente función devuelve un error
                self.calculadora.lineEdit.insert(str(eval(texto))) # calcula 
            except: #si devuelve error, ejecuta lo siguiente 
                self.calculadora.lineEdit.clear() #borra el error anterior
                self.calculadora.lineEdit.insert('ERROR') 

            
            
            
    def validarLabel(self):
        '''
        validarLabel borra label solo si label es CalculadoraQT
        '''
        if self.calculadora.label.text() == "CalculadoraQT":
            self.calculadora.label.setText("")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_aplicacion = Calculadora()
    mi_aplicacion.show()
    sys.exit(app.exec_())