#!/usr/bin/env python
# coding=utf8

import subprocess


def _loginusersnum():  # ls
    p = subprocess.Popen('users', stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    info = []
    for i in out.split(' '):
        if i.strip('\n'):
            info.append(i.strip('\n'))
    usernum = len(set(info))
    tmpsize = {}
    tmpsize["ls"] = usernum
    return tmpsize

print _loginusersnum()

