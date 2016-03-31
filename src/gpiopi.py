#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Not on a Raspberry Pi, use antipi.py for testing purposes")
    sys.exit(1)
GPIO.setmode(GPIO.BCM)

GPIO.setup(0, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

print("Raspberry Pi GPIO module Version {0}".format(GPIO.VERSION))

def leftWinOpen():
    pass


def leftWinClose():
    pass


def rightWinOpen():
    pass


def rightWinClose():
    pass


def sunRoofOpen():
    pass


def sunRoofClose():
    pass
