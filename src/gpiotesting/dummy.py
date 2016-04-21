# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dummy.ui'
#
# Created: Mon Mar 21 12:34:26 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class UI(object):
    def setupUi(self, UI):
        UI.setObjectName("UI")
        UI.resize(421, 106)
        UI.setWindowTitle("Threading demo")

        self.someLabel = QtGui.QLabel(UI)
        self.someLabel.setObjectName("someLabel")
        self.someLabel.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.someLabel.setText("Type here:")

        self.someText = QtGui.QLineEdit(UI)
        self.someText.setObjectName("someText")
        self.someText.setGeometry(QtCore.QRect(90, 20, 321, 23))

        self.threadStarter = QtGui.QPushButton(UI)
        self.threadStarter.setObjectName("threadStarter")
        self.threadStarter.setGeometry(QtCore.QRect(300, 70, 101, 23))
        self.threadStarter.setText("Start a thread")

        QtCore.QMetaObject.connectSlotsByName(UI)
