from Main_Menu import Ui_dlgMain
from Settings_Menu import Ui_dlgSettings
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

ip = 'temp'
multicast = 'temp'
resolution = 'temp'


class StartSettings(Ui_dlgSettings):

    def __init__(self, window2):
        Ui_dlgSettings.__init__(self)
        self.setupUi(window2)
        self.init_ui()

    def init_ui(self):
        self.txtIP.setText('127.0.0.1')  # TODO: change this to be the SFA IP set
        # self.buttonBox.accepted.connect(self.save_settings())
        # self.buttonBox.rejected.connect(self.cancel())
        print('settings opened')

    def save_settings(self):
        global ip, multicast, resolution
        ip = self.txtIP.text().strip()
        multicast = self.cmbMulticast.currentText()
        resolution = self.cmbResolution.currentText()
        print('settings saved')

    def cancel(self):
        print('canceled without saving')


class StartUp(Ui_dlgMain):

    def __init__(self, window):
        Ui_dlgMain.__init__(self)
        self.setupUi(window)
        self.init_ui()

    def init_ui(self):
        # self.btnStart.clicked.connect(self.start())
        # self.btnExit.clicked.connect(self.exit())
        # self.btnSettings.clicked.connect(self.settings())
        print('main menu')

    def start(self):
        print('Starting')
        # TODO: Put the client/server code here in each file

    def exit(self):
        print('Exiting')
        sys.exit()

    def settings(self):
        # Opens the settings dialog
        app2 = QtWidgets.QApplication(sys.argv)
        dialog2 = QtWidgets.QDialog()
        prog2 = StartSettings(dialog2)

        dialog2.show()
        sys.exit(app2.exec_())


if __name__ == '__main__':
    # Opens the main dialog
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = StartUp(dialog)

    dialog.show()
    sys.exit(app.exec_())

