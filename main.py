#!/usr/bin/env python
# -*- coding: utf-8 -*-

import LineNotifyRequest

api_token = 'YOUR TOKEN';

req = LineNotifyRequest()
req.setToken(api_token)
req.setMessage('hogehoge')
req.send()



