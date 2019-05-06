import zlib
import socket
import struct
from screenshot import ScreenShotObj
import pygame
from Main_Menu import Ui_dlgMain
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import sys


class StartUp(Ui_dlgMain):

    def __init__(self, dialog):
        Ui_dlgMain.__init__(self)
        self.setupUi(dialog)
        # Ui_dlgMain.btnStart
        self.btnStart.clicked.connect(self.start_client())
        self.btnExit.clicked.connect(self.exit())



    def start_client(self):
        print('IT WORKED')

    def exit(self):
        print('Exiting')
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = StartUp(dialog)

    dialog.show()
    sys.exit(app.exec_())

