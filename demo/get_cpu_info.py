#!/usr/bin/python
# coding:utf8

import psutil

logical_cores = psutil.cpu_count(logical=True)
if logical_cores is None:
    logical_cores = 1

physical_cores = psutil.cpu_count(logical=False)
if physical_cores is None:
    physical_cores = 1

print "logical_cores: %d" % (logical_cores)
print "physical_cores: %d" % (physical_cores)

if logical_cores / physical_cores == 2:
    print "hyper threading: enable"
else:
    print "hyper threading: disable"
