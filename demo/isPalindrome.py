#!/usr/bin/python
# coding:utf8

import sys


def isPalindrome(s):

    reverse_s = s[::-1]
    # reverse s eg: s = "hello" reverse_s = "olleh"
    if s == reverse_s:
        print "%s is palindrome!" % s
    else:
        print "%s is not palindrome!" % s


isPalindrome(sys.argv[1])
