def teclas(tecla, label, line):
    '''
    teclas - recibe la teclas que se pulsan, filtra solo las teclas corectas y modifica el lineEdit para usarlo como pantalla 
    Args:
        tecla ([]): [recibe argumentos desde keyPressEvent  ]
        label ([]): [es la Qlabel - label]
        line  ([]): [es el lineEdit - lineEdit] 
    '''
    texto = label.text() # captura el texto del label 
    
    if 40  <= tecla.key() <= 57: # Filtra las teclas con un código  entre 40 y 57
        label.setText(texto + tecla.text()) # Modifica el label siendo variable texto mas la tecla
        
    elif 16777220 <= tecla.key() <= 16777221: # filtra los dos Intros
        line.clear()
        
        try:
            line.insert(str(eval(texto))) # con la función eval calculamos la expresion que tenmops en Texto, al hacerlo nos devuelve un integer, pero lineEdit solomuestra string asi que tenemos que trasformarlo
        except:
            line.insert('ERROR')
            
    elif tecla.key() == 16777219: # Filtra la tecla  borrar
        label.setText(texto[:-1]) # algoritmo para borrar    
    