#!/usr/bin/env python
# coding=utf8


class A:

    def __init__(self):
        pass

    def funca(self):
        print "print ClassA"


class B(A):

    def __init__(self):
        A.__init__(self)

    def funcb(self):
        print "print ClassB"

b = B()
b.funcb()

b.funca()
