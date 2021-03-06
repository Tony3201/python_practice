#!/usr/bin/env python
# coding=utf8


# python 2.7.6

def gcd(x, y):
    if y == 0:
        print 'x=%d' % (x)
        return x
    else:
        print 'x = %d, y = %d, x mod y = %d' % (x, y, x % y)
        return gcd(y, x % y)


print 'gcd(60, 24) = %d' % (gcd(60, 24))
print 'gcd(24, 60) = %d' % (gcd(24, 60))


def num(data, isIndex):
    isNum = True
    try:
        if isIndex is False and int(data) <= 0:
            isNum = False
            print "Job Id <= 0 is out of valid range." % data
            sys.exit(-1)
        if isIndex is True and int(data) < 0:
            isNum = False
            print "Job Array index out of valid range." % data
            sys.exit(-1)
    except:
        isNum = False

    return isNum
