#!/usr/bin/env  python
# coding=utf8


optionvalue = (
    lambda optionvalue: optionvalue if optionvalue is None else optionvalue.split())

print optionvalue("u1 u2 u3")
print optionvalue(None)
print optionvalue("")
print optionvalue("    ")
