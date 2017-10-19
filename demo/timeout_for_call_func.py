#!/usr/bin/env python
# coding=utf8


import time
import threading


def timeFunc(seconds):
    print "seconds = ", seconds
    time.sleep(seconds)


t = threading.Thread(target=timeFunc, args=(10,))
t.setDaemon(True)
t.start()
t.join(1)

print "end=============="
