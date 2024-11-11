import sys
from PyQt5 import uic,QtWidgets,QtGui
qtCreatorFile = "P3_DatosDeImagenes.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.lista_imagenes = {
            1:":/Perros/caramelo1.jpg",
            2:":/Perros/caramelo2.jpg",
            3:":/Logos/Logo.png",
            4:":/Personaje/Anime.png"
        }

        self.clave_imagen = 1 #Primera imagen a mostrar
        self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        # Area de los Slots
    def atras(self):
        print(self.clave_imagen)
        if self.clave_imagen >= 2:
            self.clave_imagen -= 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))

    def adelante(self):
        print(self.clave_imagen)
        if self.clave_imagen < 4:
            self.clave_imagen += 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



