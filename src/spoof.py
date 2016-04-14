#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

HIGH=1
LOW=0
def output(pinnum, state):
    exec("pin{0} = {1}".format(pinnum,state))
