#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from sleep import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Not on a Raspberry Pi, use antipi.py for testing purposes")
#    sys.exit(1)
    import Spoof as GPIO
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
    GPIO.output(0, GPIO.HIGH)
    leftwin = open("./.stat/leftwin", "w")
    leftwin.write("o")  # Opening...
    leftwin.close()


def leftWinClose():
    GPIO.output(2, GPIO.HIGH)
    leftwin = open("./.stat/leftwin", "w")
    leftwin.write("c")  # Closing...
    leftwin.close()


def leftWinMax():
   while GPIO.input(3) == GPIO.LOW:
       sleep(0.001)
    leftwin = open("./.stat/leftwin", "r")
    status = leftwin.read()
    leftwin.close()
    if status == "o":
        GPIO.output(0, GPIO.LOW)
    elif status == "c":
        GPIO.output(2, GPIO.LOW)
    else:
        print("WTF???")

def rightWinOpen():
    GPIO.output(4, GPIO.HIGH)
    rightwin = open("./.stat/rightwin", "w")
    rightwin.write("o")  # Opening...
    rightwin.close()


def rightWinClose():
    GPIO.output(6, GPIO.HIGH)
    rightwin = open("./.stat/rightwin", "w")
    rightwin.write("o")  # Opening...
    rightwin.close()


def rightWinMax():
   while GPIO.input(5) == GPIO.LOW:
       sleep(0.001)
    rightwin = open("./.stat/rightwin", "r")
    status = rightwin.read()
    rightwin.close()
    if status == "o":
        GPIO.output(4, GPIO.LOW)
    elif status == "c":
        GPIO.output(6, GPIO.LOW)
    else:
        print("WTF???")


def sunRoofOpen():
    GPIO.output(22, GPIO.HIGH)
    sunroof = open("./.stat/sunroof", "w")
    sunroof.write("o")  # Opening...
    sunroof.close()


def sunRoofClose():
    GPIO.output(24, GPIO.HIGH)
    sunroof = open("./.stat/sunroof", "w")
    sunroof.write("o")  # Opening...
    sunroof.close()


def sunRoofMax():
   while GPIO.input(25) == GPIO.LOW:
       sleep(0.001)
    sunroof = open("./.stat/sunroof", "r")
    status = sunroof.read()
    sunroof.close()
    if status == "o":
        GPIO.output(22, GPIO.LOW)
    elif status == "c":
        GPIO.output(24, GPIO.LOW)
    else:
        print("WTF???")
