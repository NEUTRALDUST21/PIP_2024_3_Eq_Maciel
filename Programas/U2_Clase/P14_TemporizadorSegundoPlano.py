### manera INCORRECTA de hacerlo... :p
import time as t
import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P14_TemporizadorSegundoPlano.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.lcdNumber.setNumDigits(4) #Numero de digitos
        self.valor_inicial = 10
        self.lcdNumber.display(self.valor_inicial)

        self.btn_iniciar.clicked.connect(self.contar)

    def contar(self):
        self.valor_inicial = 10
        for i in range(self.valor_inicial, 0, -1):
            print(i)
            self.lcdNumber.display(i)
            t.sleep(.25) #segundos

    # Area de los Slots

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

