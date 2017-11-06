#!/usr/bin/env python
# coding = utf8

import win32net
import win32netcon


def get_total_login_users(host_name=None):
    resume_handle = 1
    user_set = set()
    try:
        while resume_handle:
            (user_list, _, rt_res) = win32net.NetWkstaUserEnum(
                host_name,
                1,
                resume_handle,
                win32netcon.MAX_PREFERRED_LENGTH)
            for user_dict in user_list:
                if user_dict['logon_server'] != '':
                    user_set.add(user_dict['username'])
            resume_handle = rt_res

    except win32net.error:
        pass

    finally:
        return len(user_set)


print get_total_login_users(r'localhost')
