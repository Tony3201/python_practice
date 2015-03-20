#!/usr/bin/python

import urllib
import os
import platform

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if platform.system() == 'Windows':
    hosts_file = 'C:\Windows\System32\drivers\etc\\hosts'
elif platform.system() == 'Linux':
    hosts_file = '/etc/hosts'
else:
    print 'you OS is not Linux or Windows'

html = gethtml('http://www.findspace.name/adds/hosts')

fp = open(hosts_file,'w+')
fp.write(html)
fp.close
