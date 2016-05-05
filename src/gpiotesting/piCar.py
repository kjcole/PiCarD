#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
if sys.version_info.major == 2:
    input = raw_input

from PySide.QtCore import *
from PySide.QtGui  import *

#import lazythread
from windows import *
import gui as gui #Change first gui to whatever your gui file is named

class Dashboard(QDialog, gui.Ui_Dashboard):
    def __init__(self, parent=None):
        """Construct a Dialog window and fill with widgets"""
        super(Dashboard, self).__init__(parent)
        self.setupUi(self)
        self.leftWinButton.clicked.connect(self.leftWinAction)
        self.workerThreads = []

    def leftWinAction(self):
        "Add function like this x=(x+1)%2"
        leftwin = open("./.stat/leftwin", "r")
        status = leftwin.read()
        leftwin.close()
        if status == "o":
            self.leftWinButton.setText("Left window is Closing")
            leftWinClose()
            self.leftWinButton.setStyleSheet("color: #F0F;")
            self.leftWinButton.setDisabled(True)
            "Code to grey out button goes here"
            workerThread = WorkerThread(len(self.workerThreads) + 1, leftWinMax)
            self.workerThreads.append(workerThread)
            #self.workerThreads[-1].talk.connect(self.thread.Done)
            self.workerThreads[-1].start()
            "run following code when thread finishes"
            self.leftWinButton.setText("Close Left Window")
            "sset button to closing instead of opening"
        elif status == "c":
            self.leftWinButton.setText("Left window is Closing")
            leftWinOpen()
            self.leftWinButton.setDisabled(True)
            "Code to grey out button goes here"
            workerThread = WorkerThread(len(self.workerThreads) + 1, leftWinMax)
            self.workerThreads.append(workerThread)
            #self.workerThreads[-1].talk.connect(self.thread.Done)
            self.workerThreads[-1].start()
            "run following code when thread finishes"
            "set button to opening instead of closing"


    def rightWinButton(self):
        pass

    def sunRoofButton(self):
        pass

class WorkerThread(QThread):
    def __init__(self, threadNumber, job, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.threadNumber = threadNumber
        self.job = job

    def run(self):
        self.job()

def main():
    app = QApplication(sys.argv)
    form = Dashboard()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
