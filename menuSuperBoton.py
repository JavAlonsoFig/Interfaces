# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuSuperBoton.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 845)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Super = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Super.setGeometry(QtCore.QRect(190, 250, 671, 301))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.btn_Super.setFont(font)
        self.btn_Super.setObjectName("btn_Super")
        self.lb_Texto = QtWidgets.QLabel(self.centralwidget)
        self.lb_Texto.setGeometry(QtCore.QRect(460, 220, 131, 16))
        self.lb_Texto.setObjectName("lb_Texto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto1"))
        self.btn_Super.setText(_translate("MainWindow", "SUPER BOTON"))
        self.lb_Texto.setText(_translate("MainWindow", "ESTE ES EL SUPER BOTON"))
