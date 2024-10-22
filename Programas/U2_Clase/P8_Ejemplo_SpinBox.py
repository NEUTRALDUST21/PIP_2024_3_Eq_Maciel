import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P8_Ejemplo_SpinBox.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(255)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(100)
        self.spinBox.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("100")

    # Area de los Slots
    def cambiaValor(self):
        valor = self.spinBox.value()
        print(valor)
        self.txt_valor.setText(str(valor))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    