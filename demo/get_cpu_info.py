#!/usr/bin/python
# coding:utf8

import psutil

logical_cores = psutil.cpu_count(logical=True)
physical_cores = psutil.cpu_count(logical=False)

print "logical_cores: %d" % (logical_cores)
print "physical_cores: %d" % (physical_cores)

if logical_cores / physical_cores == 2:
    print "hyper threading: enable"
else:
    print "hyper threading: disable"
