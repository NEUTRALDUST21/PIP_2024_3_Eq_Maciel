from asyncio import timeout

import serial  #PARA CONECTAR A ARDUNO
import sys
from PyQt5 import uic,QtWidgets , QtGui, QtCore
qtCreatorFile = "P13_InterfazConexionArduino.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)
    # Area de los Slots
    def accion(self):
        texto_boton = self.tbn_accion.text() # nombre del boton
        com = self.txt_com.text() # obtiene el como al que se conectara --->
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)  #dependiendo de leer las lecturas
            self.btn_accion.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen(): # isOpen()
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
        else: ##reconectar
            self.arduino.open()
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")

    def lecturaArduino(self):
        if not self.arduino is None and self.arduino.isOpen(): ##isOpen()
            if self.arduino.inWaiting():
                cadena = self.arduino.readline()
                cadena = cadena.decode()
                cadena = cadena.strip()
                ##print(cadena)
                if cadena != "":
                    #PROCESAR LA CADENA
                    self.datos.addItem(cadena)
                    self.datos.setCurrentRow(self.datos.count()-1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

