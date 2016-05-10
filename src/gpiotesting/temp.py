#!/usr/bin/env python3
# -*- coding: utf-8 -*-

VERSION=-1.0
HIGH="HIGH"
LOW="LOW"
IN="IN"
OUT="OUT"
BCM = "BCM"
BOARD = "BOARD"

mode = None

class Pin(object):
    def __init__(self):
#        self.num = num
        self.state = None
        self.dir = None

pinbcm = (None, None, 2, None, 3, None, 4, 14, None, 15,
          17, 18, 27, None, 22, 23, None, 24, 10, None,
          9, 25, 11, 8, None, 7, None, None, 5, None,
          6, 12, 13, None, 19, 16, 26, 20, None, 21)


pins = {}

#pins = []
#for pin in range(40):
#    pins.append(Pin(None))

def setmode(numsys):
    global mode, pins
    mode = numsys
    pins = {}
    for pin in range(40):
        if mode == BCM:
            pins[pinbcm[pin-1]] = Pin()
        elif mode == BOARD:
            pins[pin+1] = Pin()
        else:
###### For some reason setmode will not work a second time even if everything is reset to defaults ###### ---fixed
            print("something's wrong")
    print("setting mode to", mode)

def setup(pinnum, direction):
#    for pin in range(40):
#        if pins[pin].num == pinnum:
#            pins[pin].dir = direction
    pins[pinnum].dir = direction

def output(pinnum, state):
    if pins[pinnum].dir == OUT:
#    for pin in range(40):
#        if pins[pin].num == pinnum:
#            pins[pin].state = state
        pins[pinnum].state = state
        print("setting {0} pin {1} to {2}".format(mode, pinnum, state))
    elif pins[pinnum].dir == IN:
        print("Make sure the pin is on output")
    else:
        print("Make sure to set the pin direction with setup(dir)")
