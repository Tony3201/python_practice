#!/usr/bin/python
# coding:utf8

import json


class Object:

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def to_JSON2(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

me = Object()
me.name = "Onur"
me.age = 35
me.dog = Object()
me.dog.name = "Apollo"

print(me.to_JSON())
print(me.to_JSON2())
