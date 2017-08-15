#!/usr/bin/python

jobid = [1, 2, 3, 4]
arrjobid = [2, 5, 6, 7]
jobarryidx = [2, 9, 10, 11]

if (i for i in jobid if i not in arrjobid):
    unexistJobid = [
        i for i in jobid if i not in arrjobid and i not in jobarryidx]

print unexistJobid
