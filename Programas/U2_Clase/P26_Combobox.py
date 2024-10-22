import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P26_Combobox.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.dicc_alumnos = {
            "2206": ["Fernando", "IN", 20],
            "REP01": ["Sebastian", "ISC", 22],
            "MACI2": ["Maciel", "IC", 21],
            "CAROL": ["Carolina", "ISC", 25],
        }
        self.cb_alumnos.addItem("Fernando", "2206")    #tres formas de acceder a los elementos de un combobox...
        self.cb_alumnos.addItem("Sebastian", "REP01")  #texto - es lo que ve el usuario
        self.cb_alumnos.addItem("Maciel", "MACI2")     #data - clave
        self.cb_alumnos.addItem("Carolina", "CAROL")   #indice
        self.cb_alumnos.currentTextChanged.connect(self.cambiaIndice)

    # Area de los Slots
    def cambiaIndice(self):
        texto = self.cb_alumnos.currentText()
        data = self.cb_alumnos.currentData()
        indice = self.cb_alumnos.currentIndex()
        print(texto + " - " + data + " - " + str(indice))
        self.cargarDatos(data) #data = clave

    def cargarDatos(self, clave):
        alumno = self.dicc_alumnos[clave]
        self.txt_nombre.setText(alumno[0])
        self.txt_carrera.setText(alumno[1])
        self.txt_edad.setText(str(alumno[2]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())