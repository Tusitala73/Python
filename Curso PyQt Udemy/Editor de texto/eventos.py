def abrirArchivo(file_dialog, textEdit, editor): 
    ruta = file_dialog.getOpenFileName(None, "Selecciona un archivo", "", "Python (*.py);;Texto (*.txt)")
    if ruta[0] != '':
        with open(ruta[0], "r") as archivo:
            textEdit.setText(("").join(archivo.readlines()))
        editor.setWindowTitle(f"Editor de texto - {ruta[0]}")