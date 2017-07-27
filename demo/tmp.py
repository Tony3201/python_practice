#!/usr/bin/python


empty_str = ""

if empty_str:
    print 'if empty_str is True'
else:
    print 'if empty_str is False'


int_0 = 0

if int_0:
    print 'if int_0 is True'
else:
    print 'if int_0 is False'

arrayjob.jobName = arrayjob.jobName[:len(arrayjob.jobName) - 1] \
    + '-' + str(replydata.get('ArrIdxSlice')[-1]) + ']'
