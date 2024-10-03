import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P13_LcdNumber.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.lcdNumber.setNumDigits(3) #Numero de digitos
        self.lcdNumber.display(123)#Numero que mandas ejemplo tambien se puede poner ("10")
        #self.lcdNumber.display("A") #Se puede poner letras

    # Area de los Slots

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())