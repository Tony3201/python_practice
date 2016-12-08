#!/usr/bin/env python
# coding=utf8

sum = 0
for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print sum
# 233168
