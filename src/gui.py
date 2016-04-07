# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clockless.ui'
#
# Created: Thu Mar 10 18:12:12 2016
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(573, 339)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(218, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        Dashboard.setPalette(palette)
        self.groupBox = QtGui.QGroupBox(Dashboard)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 521, 281))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sunroofopen = QtGui.QPushButton(self.groupBox)
        self.sunroofopen.setCheckable(False)
        self.sunroofopen.setAutoRepeat(False)
        self.sunroofopen.setObjectName("sunroofopen")
        self.gridLayout_2.addWidget(self.sunroofopen, 1, 1, 1, 1)
        self.calendarWidget = QtGui.QCalendarWidget(self.groupBox)
        self.calendarWidget.setBaseSize(QtCore.QSize(0, 0))
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 2)
        self.rightwinopen = QtGui.QPushButton(self.groupBox)
        self.rightwinopen.setObjectName("rightwinopen")
        self.gridLayout_2.addWidget(self.rightwinopen, 1, 2, 1, 1)
        self.leftWinButton = QtGui.QPushButton(self.groupBox)
        self.leftWinButton.setObjectName("leftWinButton")
        self.gridLayout_2.addWidget(self.leftWinButton, 1, 0, 1, 1)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QtGui.QApplication.translate("Dashboard", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.sunroofopen.setText(QtGui.QApplication.translate("Dashboard", "Sunroof Open", None, QtGui.QApplication.UnicodeUTF8))
        self.rightwinopen.setText(QtGui.QApplication.translate("Dashboard", "Right Window Open", None, QtGui.QApplication.UnicodeUTF8))
        self.leftWinButton.setText(QtGui.QApplication.translate("Dashboard", "Left Window Open", None, QtGui.QApplication.UnicodeUTF8))

