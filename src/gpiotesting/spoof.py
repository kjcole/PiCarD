#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

VERSION=-1.0
HIGH="HIGH"
LOW="LOW"
IN="IN"
OUT="OUT"
BCM = "BCM"
BOARD = "BOARD"
pinbcm = (None, None, None, 2, None, 3, None, 4, 14, None, 15,
          17, 18, 27, None, 22, 23, None, 24, 10, None,
          9, 25, 11, 8, None, 7, None, None, 5, None,
          6, 12, 13, None, 19, 16, 26, 20, None, 21)

pinboard = (None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40)

pins = []
for pin in range(41):
    pins.append(None)

pins = []
for pin in range(41):
    pins.append({"state": None,
                 "dir": None,
                 "bcm": pinbcm[pin],
                 "board": pin})

def setmode(mode):
    pass

def setup(pinnum, direction):
    pass

def output(pinnum, state):
    global pins
#   pinnum = state
#   exec("pin{0} = {1}".format(pinnum,state), globals())
#   pins[pinnum] = state
    pins[pinnum]["state"] = state
    print("setting pin",pinnum,"to",state)

def wait(pinnum):
    input("press enter to simulate pin",pinnum,"being turned to high for 0.1 seconds then back to low")

