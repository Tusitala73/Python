# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculadora(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(247, 343)
        Form.setMaximumSize(QtCore.QSize(247, 343))
        Form.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.contenedor = QtWidgets.QFrame(Form)
        self.contenedor.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.contenedor.setObjectName("contenedor")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.contenedor)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameVisor = QtWidgets.QFrame(self.contenedor)
        self.frameVisor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameVisor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameVisor.setObjectName("frameVisor")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameVisor)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frameVisor)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frameVisor)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frameVisor, 0, 0, 1, 1)
        self.frameBotones = QtWidgets.QFrame(self.contenedor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameBotones.sizePolicy().hasHeightForWidth())
        self.frameBotones.setSizePolicy(sizePolicy)
        self.frameBotones.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameBotones.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameBotones.setObjectName("frameBotones")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameBotones)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnPA = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPA.sizePolicy().hasHeightForWidth())
        self.btnPA.setSizePolicy(sizePolicy)
        self.btnPA.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPA.setObjectName("btnPA")
        self.gridLayout_4.addWidget(self.btnPA, 0, 1, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn1.setObjectName("btn1")
        self.gridLayout_4.addWidget(self.btn1, 3, 0, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn4.setObjectName("btn4")
        self.gridLayout_4.addWidget(self.btn4, 2, 0, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        self.btn7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn7.setObjectName("btn7")
        self.gridLayout_4.addWidget(self.btn7, 1, 0, 1, 1)
        self.btnC = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnC.sizePolicy().hasHeightForWidth())
        self.btnC.setSizePolicy(sizePolicy)
        self.btnC.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnC.setObjectName("btnC")
        self.gridLayout_4.addWidget(self.btnC, 0, 0, 1, 1)
        self.btnPC = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPC.sizePolicy().hasHeightForWidth())
        self.btnPC.setSizePolicy(sizePolicy)
        self.btnPC.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPC.setObjectName("btnPC")
        self.gridLayout_4.addWidget(self.btnPC, 0, 2, 1, 1)
        self.btnPunto = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPunto.sizePolicy().hasHeightForWidth())
        self.btnPunto.setSizePolicy(sizePolicy)
        self.btnPunto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPunto.setObjectName("btnPunto")
        self.gridLayout_4.addWidget(self.btnPunto, 4, 0, 1, 1)
        self.btnMultiplicar = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMultiplicar.sizePolicy().hasHeightForWidth())
        self.btnMultiplicar.setSizePolicy(sizePolicy)
        self.btnMultiplicar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMultiplicar.setObjectName("btnMultiplicar")
        self.gridLayout_4.addWidget(self.btnMultiplicar, 0, 3, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        self.btn8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn8.setObjectName("btn8")
        self.gridLayout_4.addWidget(self.btn8, 1, 1, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        self.btn9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn9.setObjectName("btn9")
        self.gridLayout_4.addWidget(self.btn9, 1, 2, 1, 1)
        self.btnDividir = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDividir.sizePolicy().hasHeightForWidth())
        self.btnDividir.setSizePolicy(sizePolicy)
        self.btnDividir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnDividir.setObjectName("btnDividir")
        self.gridLayout_4.addWidget(self.btnDividir, 1, 3, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn5.setObjectName("btn5")
        self.gridLayout_4.addWidget(self.btn5, 2, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn6.setObjectName("btn6")
        self.gridLayout_4.addWidget(self.btn6, 2, 2, 1, 1)
        self.btnRestar = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRestar.sizePolicy().hasHeightForWidth())
        self.btnRestar.setSizePolicy(sizePolicy)
        self.btnRestar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnRestar.setObjectName("btnRestar")
        self.gridLayout_4.addWidget(self.btnRestar, 2, 3, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn2.setObjectName("btn2")
        self.gridLayout_4.addWidget(self.btn2, 3, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn3.setObjectName("btn3")
        self.gridLayout_4.addWidget(self.btn3, 3, 2, 1, 1)
        self.btnSumar = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSumar.sizePolicy().hasHeightForWidth())
        self.btnSumar.setSizePolicy(sizePolicy)
        self.btnSumar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSumar.setObjectName("btnSumar")
        self.gridLayout_4.addWidget(self.btnSumar, 3, 3, 1, 1)
        self.btnIgual = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnIgual.sizePolicy().hasHeightForWidth())
        self.btnIgual.setSizePolicy(sizePolicy)
        self.btnIgual.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnIgual.setObjectName("btnIgual")
        self.gridLayout_4.addWidget(self.btnIgual, 4, 2, 1, 2)
        self.btn0 = QtWidgets.QPushButton(self.frameBotones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        self.btn0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn0.setObjectName("btn0")
        self.gridLayout_4.addWidget(self.btn0, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frameBotones, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculadora"))
        self.label.setText(_translate("Form", "CalculadoraQT"))
        self.btnPA.setText(_translate("Form", "("))
        self.btn1.setText(_translate("Form", "1"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn7.setText(_translate("Form", "7"))
        self.btnC.setText(_translate("Form", "C"))
        self.btnPC.setText(_translate("Form", ")"))
        self.btnPunto.setText(_translate("Form", "."))
        self.btnMultiplicar.setText(_translate("Form", "*"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn9.setText(_translate("Form", "9"))
        self.btnDividir.setText(_translate("Form", "%"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn6.setText(_translate("Form", "6"))
        self.btnRestar.setText(_translate("Form", "-"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn3.setText(_translate("Form", "3"))
        self.btnSumar.setText(_translate("Form", "+"))
        self.btnIgual.setText(_translate("Form", "="))
        self.btn0.setText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Calculadora()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
