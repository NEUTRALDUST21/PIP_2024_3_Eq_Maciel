import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P7_Ejemplo_VerticalSlider.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setValue(100)
        self.verticalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("100")

    # Area de los Slots
    def cambiaValor(self):
        valor = self.verticalSlider.value()
        print(valor)
        self.txt_valor.setText(str(valor))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

