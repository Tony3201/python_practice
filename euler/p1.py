#!/usr/bin/env python
# coding=utf8

maxNum = 1000
sum = 0

for num in range(3, maxNum):
    if num % 3 == 0 or num % 5 == 0:
        sum += num

print sum
