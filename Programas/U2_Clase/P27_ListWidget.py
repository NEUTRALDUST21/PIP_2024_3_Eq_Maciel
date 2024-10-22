import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P27_ListWidget.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets. QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.lista_alumnos = [] #lista vacia de alummos
        self.lw_alumnos.currentItemChanged.connect(self.cambia_valor)

    # Area de los Slots
    def agregar(self):
        nombre_alumno = self.txt_nombre.text()
        self.lista_alumnos.append(nombre_alumno)
        self.lw_alumnos.addItem(nombre_alumno)

    def cambia_valor(self):
        print(self.lw_alumnos.currentItem().text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())