#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib

class LineNotifyRequest:
    url = 'https://notify-api.line.me/api/notify'
    apiToken = None;
    message = None;

    def setToken(self, token):
        self.apiToken = token

    def setMessage(self, message):
        self.message = message

    def send(self):
        values = { 'message' : self.message }
        headers = { 'Authorization' : 'Bearer {t}'.format(t=self.apiToken) }

        data = urllib.urlencode(values)
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page
