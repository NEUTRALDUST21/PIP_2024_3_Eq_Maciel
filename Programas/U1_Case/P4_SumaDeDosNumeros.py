import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P4_SumaDeDosNumeros.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals (Evento)
        try:
            self.btn_sumar.clicked.connect(self.sumar)
        except Exception as error:
            print(error)
    # Area de los Slots (Funciones)
    def sumar(self):
        num1 = self.txt_numero1.text() #str
        num2 = self.txt_numero2.text() #str

        num1 = int(num1)
        num2 = int(num2)

        resultado = num1 + num2

        self.mensaje("La suma es: " + str(resultado))

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())