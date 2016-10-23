#!/usr/bin/env python
# -*- coding: utf-8 -*-

from LineNotifyRequest import *

api_token = 'YOUR_TOKEN';

if __name__ == "__main__":
    req = LineNotifyRequest()
    req.setToken(api_token)
    req.setMessage('hogehoge')
    req.send()



