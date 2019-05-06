# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgMain(object):
    def setupUi(self, dlgMain):
        dlgMain.setObjectName("dlgMain")
        dlgMain.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/jack_cast_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgMain.setWindowIcon(icon)
        self.btnStart = QtWidgets.QPushButton(dlgMain)
        self.btnStart.setGeometry(QtCore.QRect(120, 70, 171, 41))
        self.btnStart.setObjectName("btnStart")
        self.btnSettings = QtWidgets.QPushButton(dlgMain)
        self.btnSettings.setGeometry(QtCore.QRect(120, 140, 171, 41))
        self.btnSettings.setObjectName("btnSettings")
        self.btnExit = QtWidgets.QPushButton(dlgMain)
        self.btnExit.setGeometry(QtCore.QRect(120, 210, 171, 41))
        self.btnExit.setObjectName("btnExit")
        self.label = QtWidgets.QLabel(dlgMain)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(dlgMain)
        QtCore.QMetaObject.connectSlotsByName(dlgMain)

    def retranslateUi(self, dlgMain):
        _translate = QtCore.QCoreApplication.translate
        dlgMain.setWindowTitle(_translate("dlgMain", "Jack Cast"))
        self.btnStart.setText(_translate("dlgMain", "Start"))
        self.btnSettings.setText(_translate("dlgMain", "Settings"))
        self.btnExit.setText(_translate("dlgMain", "Exit"))
        self.label.setText(_translate("dlgMain", "Jack Cast"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgMain = QtWidgets.QDialog()
    ui = Ui_dlgMain()
    ui.setupUi(dlgMain)
    dlgMain.show()
    sys.exit(app.exec_())

