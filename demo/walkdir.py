#!/usr/bin/python
import os
def dirList(path):
        path = []
        tree = os.walk('/home/python')
        for p in tree:
                path.append(p)
        print path
dirList('/home/python/')