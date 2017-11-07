#!/usr/bin/env python
# coding = utf8

import psutil

def statictime(prev_idle, prev_time, IdleL=[0], TimeL=[0]):
    if prev_idle == 0 and prev_time == 0:
        if len(IdleL) == 1:
            IdleL.insert(0, prev_idle)
            TimeL.insert(0, prev_time)
    elif IdleL == [0, 0] and TimeL == [0, 0]:
        IdleL.pop()
        TimeL.pop()
        IdleL.insert(0, prev_idle)
        TimeL.insert(0, prev_time)
    else:
        IdleL.insert(0, prev_idle)
        TimeL.insert(0, prev_time)
        if len(IdleL) > 2:
            IdleL.pop()
            TimeL.pop()
    TotalL = []
    TotalL.append(IdleL)
    TotalL.append(TimeL)
    return TotalL

def _getPage(isPaging):
    pagedicsec = {}
    f = open("/proc/vmstat", 'r')
    while True:
        line = f.readline()
        if line:
            index = line.find(' ')
            tag = line[0:index]
            value = line[index + 1:-1]
            if isPaging:
                if tag == "pswpin":
                    page_in = int(value)
                elif tag == "pswpout":
                    page_out = int(value)
            else:
                if tag == "pgpgin":
                    page_in = int(value)
                elif tag == "pgpgout":
                    page_out = int(value)
        else:
            break
    f.close()
    pagedicsec["page_in"] = page_in
    pagedicsec["page_out"] = page_out
    return pagedicsec

def _cpuTime():
    cpu_time_dic = {}
    cputime = psutil.cpu_times()
    cpu_time_dic["itime"] = cputime.idle * 100
    total_cpus = psutil.cpu_count(logical=False)
    total_cpu_times = cputime.idle + cputime.system + cputime.user
    cpu_time_dic["etime"] = total_cpu_times / total_cpus
    return cpu_time_dic
    # f = open("/proc/stat", 'r')
    # i = 0
    # if i == 0:
    #     line = f.readline()
    #     if line:
    #         index = line.find(' ')
    #         tag = line[0:index]
    #         line1 = line[index + 2:-1]
    #         index1 = line1.find(' ')
    #         cpu_userstr = line1[0:index1]

    #         line2 = line1[index1 + 1:-1]
    #         index2 = line2.find(' ')
    #         cpu_nicestr = line2[0:index2]

    #         line3 = line2[index2 + 1:-1]
    #         index3 = line3.find(' ')
    #         cpu_sysstr = line3[0:index3]

    #         line4 = line3[index3 + 1:-1]
    #         index4 = line4.find(' ')
    #         cpu_idlestr = line4[0:index4]
    #         cpu_user = int(cpu_userstr)
    #         cpu_nice = int(cpu_nicestr)
    #         cpu_sys = int(cpu_sysstr)
    #         cpu_idle = int(cpu_idlestr)
    # f.close()
    # prev_idle = 0
    # prev_time = 0
    # prevdict = {}
    # prevdict = statictime(prev_idle, prev_time)
    # prev_idle = prevdict[0][0]
    # prev_time = prevdict[1][0]
    # itime = cpu_idle - prev_idle
    # prev_idle = cpu_idle
    # ttime = cpu_user + cpu_nice + cpu_sys + cpu_idle
    # etime = ttime - prev_time
    # prev_time = ttime
    # prevdict = statictime(prev_idle, prev_time)
    # if etime == 0:
    #     etime = 1
    # cpus = psutil.cpu_count(logical=False)
    # cores = psutil.cpu_count(logical=True)
    # if cores is None:
    #     cores = 1
    # if cpus is None:
    #     cpus = cores

    # kz_h = 100.0
    # etime /= kz_h
    # etime /= cpus
    # cputimedic = {}
    # cputimedic["itime"] = itime
    # cputimedic["etime"] = etime
    # return cputimedic


    # cputime = psutil.cpu_times()
    # itime = cputime.idle*100
    # etime = (cputime.idle+cputime.system+cputime.user)/100/psutil.cpu_count(logical=False)*100
    # # cpus = psutil.cpu_count(logical=False)

print _getPage(True)