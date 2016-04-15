#!/usr/bin/env python
# coding=utf8


class queryReq:
    isWideFormat = "888"
    isLongFormat = "666"
    isAllStates = "a"
    isFinish = "d"
    isPend = "p"
    isSuspend = "s"
    isRun = "r"
    isJobArray = "A"
    Host = "m"
    Queue = "q"
    User = "u"
    Project = "P"
    Normalized = "N"
    JobName = "J"
    JobId = "jobId"
    Version = "V"
    CmdOpcode = 1
    MsgOpcode = 0

    def __init__(self):

        self.isWideFormat = "w"
        #self.isLongFormat = "l"
        self.isAllStates = "a"
        self.isFinish = "d"
        self.isPend = "p"
        self.isSuspend = "s"
        self.isRun = "r"
        self.isJobArray = "A"

        self.Host = "m"
        self.Queue = "q"
        self.User = "u"
        self.Project = "P"
        self.Normalized = "N"
        self.JobName = "J"
        self.JobId = "jobId"

        self.Version = "V"

        self.CmdOpcode = 1
        self.MsgOpcode = 0

    def convertObjToDict(self):
        dict = {}
        dict.update(self.__dict__)
        return dict


if __name__ == '__main__':

    newReq = queryReq()
    print newReq.isLongFormat
    reqDict = newReq.convertObjToDict()
    print reqDict
