#!/usr/bin/env python
# coding = utf8

import psutil


def get_total_login_users():
    ls_dict = {}
    user_set = set()
    try:
        users = psutil.users()
        for user in users:
            user_set.add(user.name)
    except:
        pass

    ls_dict['ls'] = len(user_set)
    return ls_dict


print get_total_login_users()
