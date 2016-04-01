#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Anti-Raspberry Pi module Version 0.1")
def leftWinOpen():
    print("Left Window Opening")
    leftwin = open("./.stat/leftwin", "w")
    leftwin.write("o")  # Opening...
    leftwin.close()
    

def leftWinClose():
    print("Left Window Closing")
    leftwin = open("./.stat/leftwin", "w")
    leftwin.write("c")  # Closing...
    leftwin.close()


def leftWinMax():
    input("Press enter to simulate window hitting maximum")
    leftwin = open("./.stat/leftwin", "r")
    status = leftwin.read()
    leftwin.close()
    if status == "o":
        print("Stopping opening left window")
    elif status == "c":
        print("Stopping closing left window")
    else:
        print("WTF???")


def rightWinOpen():
    print("Right Window Opening")
    rightwin = open("./.stat/rightwin", "w")
    rightwin.write("o")  # Opening...
    rightwin.close()


def rightWinClose():
    print("Right Window Closing")
    rightwin = open("./.stat/rightwin", "w")
    rightwin.write("c")  # Closing...
    rightwin.close()


def rightWinMax():
    input("Press enter to simulate window hitting maximum")
    rightwin = open("./.stat/rightwin", "r")
    status = rightwin.read()
    rightwin.close()
    if status == "o":
        print("Stopping opening right window")
    elif status == "c":
        print("Stopping closing right window")
    else:
        print("WTF???")


def sunRoofOpen():
    print("Sunroof Opening")
    sunroof = open("./.stat/sunroof", "w")
    sunroof.write("o")  # Opening...
    sunroof.close()


def sunRoofClose():
    print("Sunroof Closing")
    sunroof = open("./.stat/sunroof", "w")
    sunroof.write("c")  # Closing...
    sunroof.close()


def sunRoofMax():
    input("Press enter to simulate window hitting maximum")
    sunroof = open("./.stat/sunroof", "r")
    status = sunroof.read()
    sunroof.close()
    if status == "o":
        print("Stopping opening sunroof")
    elif status == "c":
        print("Stopping closing sunroof")
    else:
        print("WTF???")


