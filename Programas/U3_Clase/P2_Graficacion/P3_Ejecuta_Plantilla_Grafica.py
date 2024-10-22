import sys
from PyQt5 import uic,QtWidgets

#qtCreatorFile = "P0_Plantilla.ui" # Nombre del archivo aqui
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
import Plantilla_Grafica as interfaz #import el modulo que tiene la clase con la interfaz convertida
class MyApp(QtWidgets. QMainWindow,interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals


    # Area de los Slots


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

