#!/usr/bin/env python
# coding=utf8


class queryReq:
    isWideFormat = "888"
    isLongFormat = "666"
    isAllStates = "a"
    isFinish = "d"
    isPend = "p"
  
if __name__ == '__main__':

    newReq = queryReq()

    if newReq:
        print newReq
    newReq = None

    if newReq:
        print "None"
