import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P5_Ejemplo_Dial.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.dial.setMinimum(0)
        self.dial.setMaximum(255)
        self.dial.setSingleStep(1)
        self.dial.setValue(100)
        self.dial.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("100")

    # Area de los Slots
    def cambiaValor(self):
        valor = self.dial.value()
        print(valor)
        self.txt_valor.setText(str(valor))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())