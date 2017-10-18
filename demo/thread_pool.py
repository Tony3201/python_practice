#!/usr/bin/env python
# coding=utf8

# example2.py
from concurrent.futures import ProcessPoolExecutor
import time


def return_future_result(message):
    time.sleep(2)
    return message


pool = ProcessPoolExecutor(max_workers=2)

future1 = pool.submit(return_future_result, ("hello"))
future2 = pool.submit(return_future_result, ("world"))
print(future1.done())
time.sleep(3)
print(future2.done())
print(future1.result())
print(future2.result())
