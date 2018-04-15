_auther__='Mohamed Hamada Salama'
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path
import sys







import urllib.request

Form_Class,_=loadUiType(path.join(path.dirname(__file__),"Download.ui"))


class MainApp(QMainWindow , Form_Class ):
    def __init__(self , parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Ui()

        def main():
            app = QApplication(sys.argv)
            window = MainApp()
            window.show()
            app.exec_()  # infinite loop

        if __name__ == '__main__':
            main()