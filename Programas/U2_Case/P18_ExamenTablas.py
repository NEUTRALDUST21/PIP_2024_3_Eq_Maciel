import sys
from PyQt5 import uic,QtWidgets, QtCore
qtCreatorFile = "P18_ExamenTablas.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # Area de los Signals
        self.lista_nombres = [ "Angel S.", "Jazmin", "Carolina", "Fernando", "Dilan", "Maciel", "Yahir", "Carlos", "Angel A."]
        self.index_nombre = 0
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])
        self.txt_nombre.setEnabled(False)

        self.btn_control.clicked.connect(self.control)

        self.hiloSegundoPlano = QtCore.QTimer() #
        self.hiloSegundoPlano.timeout.connect(self.contar)

        self.txt_tabla.setEnabled(False)
        self.txt_numero.setEnabled(False)
        self.txt_resultado.setEnabled(False)
        self.txt_resultado.setText("")

        self.resp_validada = 1
        self.btn_validar.clicked.connect(self.valida)

    def valida(self):
        try:
            resultado = self.tabla * self.numero
            resp_usuario = int(self.txt_resultado.text())

            if resultado == resp_usuario:
                QtWidgets.QMessageBox.information(self, "Validación", "¡Respuesta Correcta!")
                self.resp_validada = 1
            else:
                QtWidgets.QMessageBox.warning(self, "Validación", "Respuesta Incorrecta")
                self.resp_validada = 0
                self.genera_pregunta()  # Genera nueva pregunta si la respuesta es incorrecta
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Por favor ingresa un número válido.")
            self.resp_validada = 0

    def control(self):
        texto_boton = self.btn_control.text()

        if texto_boton == "INICIAR" and self.resp_validada == 1:#####mal
            self.index_nombre = 0
            self.hiloSegundoPlano.start(10) #Inicia el hilo en segundo plano, valor milisengundos (500) cambia cada medio segundo
            self.btn_control.setText("DETENER")
            self.txt_resultado.setEnabled(False)
            self.txt_resultado.setText("")
        else:
            self.hiloSegundoPlano.stop()
            self.btn_control.setText("INICIAR")
            self.txt_resultado.setEnabled(True)
            self.genera_pregunta()

    def genera_pregunta(self):
        import random as rnd
        self.tabla = rnd.randint(1, 10)
        self.numero = rnd.randint(1, 10)
        self.txt_tabla.setText(str(self.tabla))
        self.txt_numero.setText(str(self.numero))

    def contar(self):
        self.index_nombre += 1
        self.index_nombre %= len(self.lista_nombres)
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])

    # Area de los Slots
    #El programa trata de que valide y si pregunta incorrecto que no cambie el nombre y pero cambie el problema

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())