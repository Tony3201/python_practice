#!/usr/bin/python
# coding:utf8

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


print sizeof_fmt(10240)
print sizeof_fmt(1024)
print sizeof_fmt(102400000)
print sizeof_fmt(368954645)
print sizeof_fmt(123)