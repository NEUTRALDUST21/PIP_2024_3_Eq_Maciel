import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P8_Ejemplo_DoubleSpinBox.ui"  # Nombre del archivo UI aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.doubleSpinBox.setMinimum(0.0)
        self.doubleSpinBox.setMaximum(255.0)
        self.doubleSpinBox.setSingleStep(0.5)  # Paso de 0.5 para valores decimales
        self.doubleSpinBox.setValue(100.0)
        self.doubleSpinBox.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("100.0")

    # Área de los Slots
    def cambiaValor(self):
        valor = self.doubleSpinBox.value()
        print(valor)
        self.txt_valor.setText(f"{valor:.1f}")  # Formatear el valor a 1 decimal

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



