import sys
from PyQt5 import uic,QtWidgets

#qtCreatorFile = "P0_Plantilla.ui" # Nombre del archivo aqui
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
import P3_Calcula_IMC as interfaz #import el modulo que tiene la clase con la interfaz convertida
class MyApp(QtWidgets. QMainWindow,interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_calcular.clicked.connect(self.calcula_imc)

    # Area de los Slots
    def calcula_imc(self):
        altura = float(self.txt_altura.text())
        peso = float(self.txt_peso.text())
        imc = peso/altura**2
        imc = round(imc, 4)
        self.mensaje("El IMC es: " + str(imc))

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

