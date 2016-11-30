#!/usr/bin/python
# coding:utf8

import psutil

socketnum = psutil.cpu_count(logical=False)
corenum = psutil.cpu_count(logical=True)


print "socketnum=%d" % (socketnum)
print "corenum=%d" % (corenum)

if corenum / socketnum == 2:
    print "threadnum=2"
else:
    print "threadnum=1"
