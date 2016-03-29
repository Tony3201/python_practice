#!/usr/bin/python
# coding:utf8

import wmi
c = wmi.WMI()
for item in c.Win32_PhysicalMedia():
    print item