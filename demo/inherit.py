#!/usr/bin/env python
# coding=utf8
import json


class User:
    def __init__(self):
        self.UserName = ''
        self.UId = 0
        self.GId = 0


class Req(User):

    def __init__(self):
        User.__init__(self)
        self.Opcode = 88


def convert_obj_to_dict(obj):
    dict_tmp = {}
    dict_tmp.update(obj.__dict__)
    return dict_tmp


r = Req()
print r.Opcode
print r.UserName
print r.UId

jdata = json.dumps(convert_obj_to_dict(r))
print jdata
