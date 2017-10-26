#!/usr/bin/env python
# coding=utf8


def list_lower(my_list):
    if my_list is not None and len(my_list) > 0:
        return [e.lower() for e in my_list]
    else:
        return []


print list_lower(["A", "B1111"])
print list_lower(None)
