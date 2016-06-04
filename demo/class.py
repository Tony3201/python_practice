#!/usr/bin/env python
# coding=utf8
import json


class queryReq:

    def __init__(self):

        self.isWideFormat = 888
        self.isLongFormat = 9999


def convert_obj_to_dict(obj):
    dict = {}
    dict.update(obj.__dict__)
    return dict


if __name__ == '__main__':

    newReq = queryReq()
    # print newReq.isLongFormat
    # reqDict = convert_obj_to_dict(newReq)
    # print reqDict
    print(json.dumps(newReq, default=lambda newReq: newReq.__dict__))
