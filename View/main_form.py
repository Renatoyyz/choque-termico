# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/main_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1020, 600)
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(20, 180, 971, 291))
        self.label.setStyleSheet("border-image: url(:/img/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btIniciar = QtWidgets.QPushButton(MainForm)
        self.btIniciar.setGeometry(QtCore.QRect(20, 20, 162, 112))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btIniciar.setFont(font)
        self.btIniciar.setObjectName("btIniciar")
        self.btConfig = QtWidgets.QPushButton(MainForm)
        self.btConfig.setGeometry(QtCore.QRect(410, 20, 162, 112))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btConfig.setFont(font)
        self.btConfig.setObjectName("btConfig")
        self.btManual = QtWidgets.QPushButton(MainForm)
        self.btManual.setGeometry(QtCore.QRect(830, 20, 162, 112))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btManual.setFont(font)
        self.btManual.setObjectName("btManual")
        self.txHidden = QtWidgets.QLineEdit(MainForm)
        self.txHidden.setGeometry(QtCore.QRect(210, 130, 113, 30))
        self.txHidden.setObjectName("txHidden")
        self.btDesligar = QtWidgets.QPushButton(MainForm)
        self.btDesligar.setGeometry(QtCore.QRect(410, 480, 162, 112))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btDesligar.setFont(font)
        self.btDesligar.setObjectName("btDesligar")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Janela Principal"))
        self.btIniciar.setText(_translate("MainForm", "Inicar"))
        self.btConfig.setText(_translate("MainForm", "Configurar"))
        self.btManual.setText(_translate("MainForm", "Manual"))
        self.btDesligar.setText(_translate("MainForm", "Desligar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
