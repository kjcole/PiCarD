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
    GPIO.output(0, GPIO.HIGH)
    leftwin = open("./stat/leftwino", "wb")
    leftwin.write(1)
    leftwin.close()


def leftWinClose():
    GPIO.output(2, GPIO.HIGH)
    leftwin = open("./stat/leftwinc", "wb")
    leftwin.write(1)
    leftwin.close()


def leftWinMax():
    while GPIO.input(3) == GPIO.LOW:
        sleep(0.001)
    leftwin = open("./stat/leftwino", "rb")
    status = leftwin.read()
    leftwin.close()
    if status:
        GPIO.output(0, GPIO.LOW)
    leftwin = open("./stat/leftwinc", "rb")
    status = leftwin.read()
    leftwin.close()
    if status:
        GPIO.output(2, GPIO.LOW)
    

def rightWinOpen():
    GPIO.output(4, GPIO.HIGH)


def rightWinClose():
    GPIO.output(6, GPIO.HIGH)


def sunRoofOpen():
    GPIO.output(22, GPIO.HIGH)


def sunRoofClose():
    GPIO.output(24, GPIO.HIGH)
