# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p3_calcula_imc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 239)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 50, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(24, 90, 71, 20))
        self.label_2.setObjectName("label_2")
        self.txt_altura = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_altura.setGeometry(QtCore.QRect(130, 50, 113, 22))
        self.txt_altura.setText("")
        self.txt_altura.setObjectName("txt_altura")
        self.txt_peso = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_peso.setGeometry(QtCore.QRect(130, 90, 113, 22))
        self.txt_peso.setText("")
        self.txt_peso.setObjectName("txt_peso")
        self.btn_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calcular.setGeometry(QtCore.QRect(120, 140, 111, 28))
        self.btn_calcular.setObjectName("btn_calcular")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Altura (m):"))
        self.label_2.setText(_translate("MainWindow", "Peso (Kg):"))
        self.btn_calcular.setText(_translate("MainWindow", "CALCULAR IMC"))