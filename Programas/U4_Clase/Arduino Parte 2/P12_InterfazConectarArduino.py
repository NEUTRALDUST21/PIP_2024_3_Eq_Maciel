from asyncio import timeout

import serial  #PARA CONECTAR A ARDUNO
import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P12_InterfazConexionArduino.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None

    # Area de los Slots
    def accion(self):
        texto_boton = self.tbn_accion.text() # nombre del boton
        com = self.txt_com.text() # obtiene el como al que se conectara --->
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.btn_accion.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen(): # isOpen()
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
        else: ##reconectar
            self.arduino.open()
            self.btn_accion.setText("DESCONECTAR")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

