#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
from LineNotifyRequest import *

import RPi.GPIO as GPIO

"""
# properties.json template
{
    "line_api_token" : "YOUR_TOKEN"
}
"""

PIN_SWITCH = 4
PIN_BELL = 17

def load_properties():
    pf = open('properties.json', 'r')
    properties = json.load(pf)
    pf.close()
    return properties

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_SWITCH , GPIO.IN)
    GPIO.setup(PIN_BELL   , GPIO.OUT)

    # read private config
    properties = load_properties()
    api_token = properties['line_api_token']

    while True:
        value = GPIO.input(PIN_SWITCH)
        print value

        if value == True :
            time.sleep(1.0)
        else:
            GPIO.output(PIN_BELL,True)
            # send Line notify
            req = LineNotifyRequest()
            req.setToken(api_token)
            req.setMessage('hogehoge')
            print req.send()

            time.sleep(5.0)

    GPIO.cleanup()



