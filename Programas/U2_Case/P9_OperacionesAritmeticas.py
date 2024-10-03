import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P9_OperacionesAritmeticas.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_restar.clicked.connect(self.restar)
        self.btn_multiplicar.clicked.connect(self.multiplicar)
        self.btn_dividir.clicked.connect(self.dividir)

    # Area de los Slots
    def sumar(self):
        numA = int(self.txt_A.text())
        numB = int(self.txt_B.text())
        resultado = numA + numB
        self.txt_resultado.setText(str(resultado))
    def restar(self):
        numA = int(self.txt_A.text())
        numB = int(self.txt_B.text())
        resultado = numA - numB
        self.txt_resultado.setText(str(resultado))
    def multiplicar(self):
        # try , except y print para para saber el error y me lo imprima y dentro de ellas se pone el codigo
        try:
            numA = int(self.txt_A.text())
            numB = int(self.txt_B.text())
            resultado = numA * numB
            self.txt_resultado.setText(str(resultado))
        except Exception as error:
            print(error)
    def dividir(self):
        numA = int(self.txt_A.text())
        numB = int(self.txt_B.text())
        resultado = numA / numB
        self.txt_resultado.setText(str(resultado))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())