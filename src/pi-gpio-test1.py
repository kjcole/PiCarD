#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pi-gpio-test1.py
#
#  Copyright 2015 Kevin Cole <kevin.cole@novawebcoop.org> 2015.12.17
#
# http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
# http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with this program; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.
#
#

from __future__ import print_function
from six.moves  import input           # use raw_input when I say input
from os.path    import expanduser      # Cross-platform home directory finder

import RPi.GPIO as GPIO
from time import sleep

__appname__    = "Raspberry Pi GPIO: Pin High Test"
__author__     = "Kevin Cole"
__copyright__  = "Copyright 2015, NOVA Web Development, LLC"
__credits__    = ["Kevin Cole"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Kevin Cole"
__email__      = "kevin.cole@novawebcoop.org"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""


def main():
    print("Raspberry Pi GPIO module Version {0}".format(GPIO.VERSION))
#   GPIO.setmode(GPIO.BCM)      # Use BCM-style   numbering
    GPIO.setmode(GPIO.BOARD)    # Use Board-style numbering
    GPIO.setup(12, GPIO.OUT)    # Pin 12 is now an output pin

    GPIO.output(12, GPIO.HIGH)  # Set pin 12 high  (on / True / 1)
    sleep(180)                  # Sleep for three minutes

    return 0                    # Exit with SUCCESS status

if __name__ == "__main__":
    main()
