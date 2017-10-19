#!/usr/bin/env python
# coding=utf8

import telnetlib

def MyTelnet(host, port, timeout):
    try:
        tn = telnetlib.Telnet(host=host, port=port, timeout=timeout)
        tn.close()
        return True
    except:
        return False


if __name__ == '__main__':
    print MyTelnet('localhost', 6322, 1)
    print MyTelnet('slave1', 2222, 1)
    print MyTelnet('slave2', 6322, 1)
    print MyTelnet('master', 22, 1)
