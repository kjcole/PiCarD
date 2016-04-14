#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

HIGH="1"
LOW="0"
def output(pinnum, state):
    exec("pin{0} = {1}".format(pinnum,state), globals())
    print("setting pin",pinnum,"to",state)
def wait(pinnum)
    input("press enter to simulate pin",pinnum,"being turned to high for 0.1 seconds then back to low")

