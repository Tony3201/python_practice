#!/usr/bin/env python
# coding = utf8

import psutil
import platform


def get_total_login_users():
    total_login_users = 0
    login_user_dict = {}
    user_set = set()
    if platform.system() == 'Windows':
        import win32net
        import win32netcon
        resume_handle = 1
        try:
            while resume_handle:
                (user_list, _, rt_res) = win32net.NetWkstaUserEnum(
                    None,
                    1,
                    resume_handle,
                    win32netcon.MAX_PREFERRED_LENGTH)

                for user_dict in user_list:
                    if user_dict['logon_server'] != '':
                        user_set.add(user_dict['username'])
                resume_handle = rt_res

        except:
            pass

        finally:
            total_login_users = len(user_set)
    else:
        try:
            users = psutil.users()
            for user in users:
                user_set.add(user.name)
        except:
            pass

        finally:
            total_login_users = len(user_set)

    login_user_dict['ls'] = total_login_users
    return login_user_dict


print get_total_login_users()
