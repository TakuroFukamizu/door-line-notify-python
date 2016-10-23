#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from LineNotifyRequest import *

"""
# properties.json template
{
    "line_api_token" : "YOUR_TOKEN"
}
"""

def load_properties():
    pf = open('properties.json', 'r')
    properties = json.load(pf)
    pf.close()
    return properties

if __name__ == "__main__":
    # read private config
    properties = load_properties()
    api_token = properties['line_api_token']

    # send Line notify
    req = LineNotifyRequest()
    req.setToken(api_token)
    req.setMessage('hogehoge')
    req.send()



