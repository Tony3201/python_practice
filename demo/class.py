#!/usr/bin/env python
# coding=utf8

import getpass


class submitReq:
    Id = 0
    # get job user
    User = getpass.getuser()
    Hosts = ''
    Options = 0
    Queue = ''
    ResReq = ''
    BeginTime = 888
    TermTime = 0
    InFile = ''
    Command = ''

    def __init__(self):
        self.BeginTime = 999
        pass


l = submitReq()
print l.User
print __name__
