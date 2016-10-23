#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
from datetime import datetime
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

def create_knock_message():
    msg_template = 'someone knock a door at {time}'
    attime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    return msg_template.format(time=attime)


if __name__ == "__main__":
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_SWITCH , GPIO.IN)
    GPIO.setup(PIN_BELL   , GPIO.OUT)

    GPIO.output(PIN_BELL, False)

    # read private config
    properties = load_properties()
    api_token = properties['line_api_token']

    while True:
        # fetch swtich status -- 5 times/1 sec
        knocked = False
        for var in range(0, 5):
            value = GPIO.input(PIN_SWITCH)
            time.sleep(0.2)
            if value == 0 : knocked = True

        if knocked == 1 :
            print "knock. knock."

            # ring door bell
            GPIO.output(PIN_BELL, True)
            time.sleep(1.5) 
            GPIO.output(PIN_BELL, False)

            # send Line notify
            req = LineNotifyRequest()
            req.setToken(api_token)
            req.setMessage(create_knock_message())
            print req.send()

            time.sleep(3.5) # long wait

    GPIO.cleanup()



