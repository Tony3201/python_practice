#!/usr/bin/python


def modify(dict):
    dict['0'] = 0
    dict['1'] = 100000000000000
    dict['2'] = 20000000008880


dict = {'0': 1, '1': 2, '2': 0}

print dict

modify(dict)

print dict

for key in dict:
    print key
