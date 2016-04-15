#!/usr/bin/env python
# coding=utf8

maxNum = 4000000
FibSeq = [1, 2]
sum = 0
i = 0
while True:

    i = i + 1
    if FibSeq[i] > maxNum:
        break
    else:
        FibSeq.append(FibSeq[i] + FibSeq[i - 1])

for evenNum in FibSeq:
    if evenNum % 2 == 0:
        print evenNum
        sum += evenNum
print sum
