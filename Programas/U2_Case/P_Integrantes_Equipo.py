import sys
from PyQt5 import uic,QtWidgets,QtGui
qtCreatorFile = "P4_DatosDeImagenes_Completo.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.lista_imagenes = {
            1:":/Integrantes/1.jpg",
            2:":/Integrantes/2.jpg",
            3:":/Integrantes/3.png",
            4:":/Integrantes/4.png"
        }

        #Suarez Martinez, Maciel Francisco
        #Saenz Rico Pérez, Fernando Aron
        #Chong Álvarez, Angel Ivaldi
        #Granados Gallegos, Carlo Sebasti

        self.datos_imagenes = {
            1: ["Suarez Martinez, Maciel Francisco", "21", "ocupacion 1", "Jugar VideoJuegos"],
            2: ["Saenz Rico Pérez, Fernando Aron", "21", "ocupacion 2", "Jugar VideoJuegos"],
            3: ["Chong Álvarez, Angel Ivaldi", "21", "ocupacion 3", "Jugar VideoJuegos"],
            4: ["Granados Gallegos, Carlo Sebasti", "21", "ocupacion 4", "Jugar VideoJuegos"]
        }
        self.clave_imagen = 1 #Primera imagen a mostrar
        self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
        self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
        self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
        self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])

        # Area de los Slots
    def atras(self):
        print(self.clave_imagen)
        if self.clave_imagen >= 2:
            self.clave_imagen -= 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))

            self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
            self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
            self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
            self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])
    def adelante(self):
        print(self.clave_imagen)
        if self.clave_imagen < 4:
            self.clave_imagen += 1
            self.imagen.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.clave_imagen]))

            self.txt_nombre.setText(self.datos_imagenes[self.clave_imagen][0])
            self.txt_edad.setText(self.datos_imagenes[self.clave_imagen][1])
            self.txt_ocupacion.setText(self.datos_imagenes[self.clave_imagen][2])
            self.txt_pasatiempo.setText(self.datos_imagenes[self.clave_imagen][3])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())