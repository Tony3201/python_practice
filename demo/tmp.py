#!/usr/bin/env python
# coding=utf8

import httplib
import urllib

params = urllib.urlencode({'@number': 12524,
                           '@type': 'issue',
                           '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("localhost", 8080)
conn.request("POST", "", params, headers)
response = conn.getresponse()
print response.status
print response.reason
