import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P10_OperacionesAritmeticas_V2.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_sumar.clicked.connect(self.operacion)
        self.btn_restar.clicked.connect(self.operacion)
        self.btn_multiplicar.clicked.connect(self.operacion)
        self.btn_dividir.clicked.connect(self.operacion)

    # Area de los Slots
    def operacion(self):
        objeto = self.sender()
        nombre_objeto = objeto.objectName()
        print(nombre_objeto)
        numA = int(self.txt_A.text())
        numB = int(self.txt_B.text())
        ####
        if nombre_objeto == "btn_sumar": resultado = numA + numB
        elif nombre_objeto == "btn_restar": resultado = numA - numB
        elif nombre_objeto == "btn_multiplicar": resultado = numA * numB
        elif nombre_objeto == "btn_dividir": resultado = numA / numB
        ####
        self.txt_resultado.setText(str(resultado))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())