#!/usr/bin/python

import urllib
import os
import platform

'''
TBD
1)backup the old hosts and update the hosts, and append it
2)ping google server whether to update hosts(use ping or ouropen)
3)can not connect the hosts_server,exit the script
4)have not permission to wirte this hosts
'''

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

html = gethtml('http://www.findspace.name/adds/hosts2')

fp = open(hosts_file,'w+')
fp.write(html)
fp.close
