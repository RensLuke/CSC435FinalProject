from Main_Menu import Ui_dlgMain
from Settings_Menu import Ui_dlgSettings
from PyQt5 import QtWidgets, QtCore
import sys
import client
import helper


ip = 'temp'
multicast = 'temp'
resolution = 'temp'
saved = False


class StartSettings(Ui_dlgSettings):

    def __init__(self, window2):
        Ui_dlgSettings.__init__(self)
        self.setupUi(window2)
        self.init_ui()

    def init_ui(self):
        # Initialize settings menu
        network = helper.NetworkingObj()
        self.txtIP.setText(network.get_sfa_ip())  # TODO: change this to be the SFA IP set
        self.buttonBox.accepted.connect(lambda: self.save_settings())
        self.buttonBox.rejected.connect(lambda: self.cancel())
        print('settings opened')

    def save_settings(self):
        global ip, multicast, resolution, saved
        ip = self.txtIP.text().strip()
        multicast = self.cmbMulticast.currentText()
        resolution = self.cmbResolution.currentText()
        saved = True
        print('settings saved')

    def cancel(self):
        print('canceled without saving')


class StartUp(Ui_dlgMain):

    def __init__(self, window):
        Ui_dlgMain.__init__(self)
        self.setupUi(window)
        self.init_ui()

    def init_ui(self):
        # Initialize main menu
        self.label.setGeometry(QtCore.QRect(10, 10, 300, 41))
        self.label.setText('Jack Cast Receiver')
        self.btnStart.clicked.connect(lambda: self.start())
        self.btnExit.clicked.connect(lambda: self.exit())
        self.btnSettings.clicked.connect(lambda: self.settings())
        print('main menu')

    def start(self):
        # Start Client/Server respectively
        print('Starting')
        client.run_me(ip, multicast, resolution, saved)

    def exit(self):
        print('Exiting')
        sys.exit()

    def settings(self):
        # Opens the settings dialog
        global prog2
        self.dialog2 = QtWidgets.QDialog()
        prog2 = StartSettings(self.dialog2)
        self.dialog2.show()


if __name__ == '__main__':
    # Opens the main dialog
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = StartUp(dialog)

    dialog.show()
    sys.exit(app.exec_())

