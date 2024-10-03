import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P6_PromedioCalificaciones.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals (Evento)
        try:
            self.btn_calcular.clicked.connect(self.calcular)
        except Exception as error:
            print(error)

    # Area de los Slots (Funciones)
    def calcular(self):
        calificaciones = self.txt_calificaciones.text() #str "10 9 8"

        #CONVIERTE LA CADENA DE CARACTERES EN UNA LISTA DE CADENAS
        lista_calificaciones = calificaciones.split(" ") # ["10", "9", "8"]

        #CONVIERTE LA LISTA DE CADENAS EN LISTA DE NUMEROS
        lista_calificaciones = [int(i) for i in lista_calificaciones] #[10, 9 , 8]

        resultado = sum(lista_calificaciones)/len(lista_calificaciones)

        #self.mensaje("La suma es: " + str(resultado))

        self.txt_resultado.setText(str(resultado))

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())