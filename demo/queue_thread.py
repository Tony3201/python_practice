#!/usr/bin/env python
# coding=utf8

import time
import threading
import Queue

queue = Queue.Queue()


def testa():
    time.sleep(10)
    queue.put('testa')


def testb():
    time.sleep(5)
    queue.put('testb')


ta = threading.Thread(target=testa)
tb = threading.Thread(target=testb)

for t in [ta, tb]:
    t.start()

print queue.get()
