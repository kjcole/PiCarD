#!/bin/python2
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

from PySide.QtCore import *
from PySide.QtGui  import *

import time
import buttonsv1
FRONT = 0
REAR = 0
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
        self.Front.clicked.connect(self.fronttoggle)
        self.Rear.clicked.connect(self.reartoggle)

#This only applies to buzzers!
   # def buzz (self):
    #    while True:
     #       GPIO.output(23, GPIO.HIGH)
      #      time.sleep(0.0011)
       #     GPIO.output(23, GPIO.LOW)
        #    time.sleep(0.0011)

    def quiet (self):
        pass

    def fronttoggle (self):
        global FRONT
        if FRONT == 0:
            GPIO.output(23, GPIO.HIGH)
        else:
            GPIO.output(23, GPIO.LOW)
        FRONT = (FRONT + 1) % 2

    def reartoggle (self):
        global REAR
        if REAR == 0:
            GPIO.output(24, GPIO.HIGH)
        else:
            GPIO.output(24, GPIO.LOW)
        REAR = (REAR + 1) % 2

def main():
    import sys
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    app = QApplication(sys.argv)
    touchscreen = MainDialog()
    touchscreen.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
