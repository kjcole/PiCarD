#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from PySide.QtCore import *
from PySide.QtGui  import *
import sys

from antipi import * #Use antipi, if not run on the Raspberry Pi
import gui as gui #Change first gui to whatever your gui file is named

class Dashboard(QDialog, gui.Ui_Dashboard):
    import thread
    def __init__(self, parent=None):
        """Construct a Dialog window and fill with widgets"""
        super(Dashboard, self).__init__(parent)
        self.setupUi(self)
        self.leftWinButton.clicked.connect(self.leftWinAction)

    def leftWinAction(self):
        "Add function like this x=(x+1)%2"
        leftwin = open("./.stat/leftwin", "r")
        status = leftwin.read()
        leftwin.close()
        if status == "o":
            print("left window is open")
            leftWinClose()
            "Code to grey out button goes here"
            thread.thread(leftWinMax())
            "run following code when thread finishes"
            "sset button to closing instead of opening"
        elif status == "c":
            leftWinOpen()
            "Code to grey out button goes here"
            thread.thread(leftWinMax())
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

    def run(self):
        job()

def main():
    app = QApplication(sys.argv)
    form = Dashboard()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
