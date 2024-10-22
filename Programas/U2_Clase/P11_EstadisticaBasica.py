import sys
from PyQt5 import uic,QtWidgets
import statistics # Módulo para hacer operaciones estadísticas
qtCreatorFile = "P11_EstadisticaBasica.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los Signals
        self.btn_promedio.clicked.connect(self.estadistica)
        self.btn_mediana.clicked.connect(self.estadistica)
        self.btn_desviacion.clicked.connect(self.estadistica)
        self.btn_varianza.clicked.connect(self.estadistica)
        self.btn_valor_mayor.clicked.connect(self.estadistica)
        self.btn_valor_menor.clicked.connect(self.estadistica)

    # Area de los Slots
    def estadistica(self):
        lista = self.txt_A.text()## 10, 20, 30, 40,
        print(lista)
        numeros = lista.split(",") ## numeros en cadena de caracteres
        print(numeros)
        numeros = [int(i) for i in numeros]
        print(numeros)

        # Identificar cual boton fue presionado
        objeto = self.sender()
        nombre_objeto = objeto.objectName()
        print(nombre_objeto)

        # Realizar la operación según el botón presionado
        if nombre_objeto == "btn_promedio":
            resultado = statistics.mean(numeros)  # Promedio
        elif nombre_objeto == "btn_mediana":
            resultado = statistics.median(numeros)  # Mediana
        elif nombre_objeto == "btn_desviacion":
            resultado = statistics.stdev(numeros)  # Desviación estándar
        elif nombre_objeto == "btn_varianza":
            resultado = statistics.variance(numeros)  # Varianza
        elif nombre_objeto == "btn_valor_mayor":
            resultado = max(numeros)  # Valor máximo
        elif nombre_objeto == "btn_valor_menor":
            resultado = min(numeros)  # Valor mínimo

        # Mostrar el resultado en el campo de texto correspondiente
        self.txt_resultado.setText(str(resultado))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())