import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P24_RadioButton_3_correcta.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.rb_soltero.toggled.connect(self.soltero) #self.rb_soltero.clicked.connect(self.soltero)
        self.rb_casado.toggled.connect(self.casado) #self.rb_casado.clicked.connect(self.casado)
        self.rb_unionlibre.toggled.connect(self.unionlibre) #self.rb_unionlibre.clicked.connect(self.unionlibre)

        self.rb_perro.toggled.connect(self.perro)
        self.rb_gato.toggled.connect(self.gato)
        self.rb_hamster.toggled.connect(self.hamster)

        # Area de los Slots
    def soltero(self):
        check = self.rb_soltero.isChecked()
        if check:
            print("Soltero")
        else:
            print("se desmarco soltero")
    def casado(self):
        check = self.rb_casado.isChecked()
        if check:
            print("Casado")
        else:
            print("se desmarco casado")
    def unionlibre(self):
        check = self.rb_unionlibre.isChecked()
        if check:
            print("Unionlibre")
        else:
            print("se desmarco unionlibre")


    def perro(self):
        check = self.rb_perro.isChecked()
        if check:
            print("Perro")
        else:
            print("se desmarco Perro")
    def gato(self):
        check = self.rb_gato.isChecked()
        if check:
            print("Gato")
        else:
            print("se desmarco Gato")
    def hamster(self):
        check = self.rb_hamster.isChecked()
        if check:
            print("Hamster")
        else:
            print("se desmarco Hamster")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())