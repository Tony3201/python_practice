#!/usr/bin/python
#coding:utf8

import sys

def isDuplicate(s):
	
	divide_s = set(s)
	#divide s,eg: s = hello divide_s = set(['h', 'e', 'l', 'o'])
	if len(s) == len(divide_s):
		print "%s is not duplicate"%s
	else:
		print "%s is duplicate!"%s

isDuplicate(sys.argv[1])
