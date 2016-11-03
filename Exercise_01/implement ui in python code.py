from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

import show


class MainDialog(QDialog, show.Ui_mainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()

# test to learn
