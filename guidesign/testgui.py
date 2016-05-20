#!/bin/python2
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

from PySide.QtCore import *
from PySide.QtGui  import *

import time
import buttonsv1

try:
    import RPi.GPIO as GPIO
except ImportError:
#    print("Not on a Raspberry Pi, use antipi.py for testing purposes")
#    sys.exit(1)
    import temp as GPIO

class MainDialog(QDialog, buttonsv1.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()

        self.setupUi(self)
        self.Front.clicked.connect(self.fronton)
        self.Rear.clicked.connect(self.rearon)

#This only applies to buzzers!
   # def buzz (self):
    #    while True:
     #       GPIO.output(23, GPIO.HIGH)
      #      time.sleep(0.0011)
       #     GPIO.output(23, GPIO.LOW)
        #    time.sleep(0.0011)

    def quiet (self):
        pass

    def fronton (self):
        GPIO.output(23, GPIO.HIGH)

    def frontoff (self):
        GPIO.output(23, GPIO.LOW)

    def rearon (self):
        GPIO.output(24, GPIO.HIGH)

    def rearoff (self):
        GPIO.output(24, GPIO.LOW)

def main():
    import sys
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    app = QApplication(sys.argv)
    touchscreen = MainDialog()
    touchscreen.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
