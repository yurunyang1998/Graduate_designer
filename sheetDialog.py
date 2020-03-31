# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseExcelSheet.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 133)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(11, 11, 321, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 80, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Please choose a excel sheet"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "cancel"))
        self.pushButton.clicked.connect(self.OK)
        self.pushButton_2.clicked.connect(self.cancel)

class SheetDialog(QDialog,Ui_Form):
    def __init__(self):
        super(SheetDialog, self).__init__()
        self.setupUi(self)

    def AddList(self,chooselist):
        for i in chooselist:
            self.comboBox.addItem(i)

    def OK(self):
        if(self.comboBox.currentText()== "Please choose a excel sheet"):
            return
        print(self.comboBox.currentText())
        self.sheet = self.comboBox.currentText()
        self.close()

    def getsheet(self):
        return self.sheet


    def cancel(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooselist = ['a','v','c','d']
    ex = SheetDialog()
    ex.AddList(chooselist)
    ex.exec()
    print(ex.getsheet())
    sys.exit(app.exec_())