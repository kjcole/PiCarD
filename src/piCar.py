#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui  import *
import sys

from antipi import * #Use antipi, if not run on the Raspberry Pi
import gui as gui #Change first gui to whatever your gui file is named

class Dashboard(QDialog, gui.Ui_Dashboard):
    def __init__(self, parent=None):
        """Construct a Dialog window and fill with widgets"""
        super(Dashboard, self).__init__(parent) 
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = Dashboard()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
