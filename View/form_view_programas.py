# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/form_view_programas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormViewProgramas(object):
    def setupUi(self, FormViewProgramas):
        FormViewProgramas.setObjectName("FormViewProgramas")
        FormViewProgramas.resize(768, 538)
        self.tblViewProgramas = QtWidgets.QTableView(FormViewProgramas)
        self.tblViewProgramas.setGeometry(QtCore.QRect(40, 0, 681, 421))
        self.tblViewProgramas.setObjectName("tblViewProgramas")
        self.btVoltar = QtWidgets.QPushButton(FormViewProgramas)
        self.btVoltar.setGeometry(QtCore.QRect(330, 440, 113, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btVoltar.setFont(font)
        self.btVoltar.setObjectName("btVoltar")

        self.retranslateUi(FormViewProgramas)
        QtCore.QMetaObject.connectSlotsByName(FormViewProgramas)

    def retranslateUi(self, FormViewProgramas):
        _translate = QtCore.QCoreApplication.translate
        FormViewProgramas.setWindowTitle(_translate("FormViewProgramas", "Form"))
        self.btVoltar.setText(_translate("FormViewProgramas", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormViewProgramas = QtWidgets.QWidget()
    ui = Ui_FormViewProgramas()
    ui.setupUi(FormViewProgramas)
    FormViewProgramas.show()
    sys.exit(app.exec_())
