#!/usr/bin/python

import urllib
import os
import time

hosts_file = 'C:\Windows\System32\drivers\etc\\hosts'
def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = gethtml('http://www.findspace.name/adds/hosts')

fp = open(hosts_file,'w+')
fp.write(html)
fp.close
