#!/usr/bin/python
# coding:utf8

JJOBS_V_OPTION = (1 << 0)
JJOBS_W_OPTION = (1 << 1)
JJOBS_L_OPTION = (1 << 2)
JJOBS_A_OPTION = (1 << 3)  # 8
JJOBS_D_OPTION = (1 << 4)  # 16
JJOBS_P_OPTION = (1 << 5)
JJOBS_S_OPTION = (1 << 6)
JJOBS_R_OPTION = (1 << 7)


BoolOptions = 0


BoolOptions = BoolOptions | JJOBS_A_OPTION

BoolOptions = BoolOptions | JJOBS_D_OPTION

print BoolOptions
# 00000000
