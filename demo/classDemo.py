#!/usr/bin/env python
# coding=utf8


class MyStruct:
    pass
    test = '9'

    def __init__(self):
        self.test1 = 8


ms = MyStruct()

ms.foo = 1
ms.bar = 2

print ms.foo
print ms.bar
print ms.test
