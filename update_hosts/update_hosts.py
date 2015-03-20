#!/usr/bin/python

import urllib
import os
import platform

if platform.system() == 'Windows':
    hosts_file = 'C:\Windows\System32\drivers\etc\\leohosts'
elif platform.system() == 'Linux':
    hosts_file = '/etc/leohosts'
else:
    print 'you OS is not Linux or Windows'
def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = gethtml('http://www.findspace.name/adds/hosts')

fp = open(hosts_file,'w+')
fp.write(html)
fp.close
