#!/usr/bin/env python
# coding=utf8

import psutil
import sys
import os
import signal


pid = int(sys.argv[1])
signalValue = int(sys.argv[2])
print pid

# os.kill(pid, signal.SIGTERM)
os.kill(pid, signalValue)

# parent = psutil.Process(pid)

# children = parent.children(recursive=True)
# kill_children_level = 2
# for child in children:
#     kill_children_level -= 1
#     # print child.pid
#     os.kill(child.pid, signal.SIGTERM)
#     if kill_children_level == 0:
#         break
