# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(616, 191)
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameEdit = QtWidgets.QLineEdit(mainDialog)
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.showButton = QtWidgets.QPushButton(mainDialog)
        self.showButton.setObjectName("showButton")
        self.horizontalLayout.addWidget(self.showButton)

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        _translate = QtCore.QCoreApplication.translate
        mainDialog.setWindowTitle(_translate("mainDialog", "Main Dialog"))
        self.nameEdit.setPlaceholderText(_translate("mainDialog", "What is your name?"))
        self.showButton.setText(_translate("mainDialog", "Show!"))

