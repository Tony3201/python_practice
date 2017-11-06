#!/usr/bin/env python
# coding = utf8

import psutil


def get_total_login_users():
    total_login_users = 0
    ls_dict = {}
    user_set = set()
    try:
        users = psutil.users()
        for user in users:
            user_set.add(user.name)
    except:
        pass

    finally:
        total_login_users = len(user_set)

    ls_dict['ls'] = total_login_users
    return ls_dict


print get_total_login_users()
