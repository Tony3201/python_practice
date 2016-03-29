#!/usr/bin/python

import os

for key in os.environ.keys():
    print "%30s %s \n" % (key, os.environ[key])

print os.environ.keys()
