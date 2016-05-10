#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

from PySide.QtCore import *
from PySide.QtGui  import *

import time
import buttonsv1


class MainDialog(QDialog, buttonsv1.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()

        self.setupUi(self)


def main():
    import sys
    app = QApplication(sys.argv)
    touchscreen = MainDialog()
    touchscreen.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
