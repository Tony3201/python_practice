#!/usr/bin/env  python
# coding=utf8

import re


def is_job_id(job_id):
    # e.g: 100[1]
    pattern = re.compile(r'^(\d+)(\[(\d+)\])?$')
    result = pattern.match(str(job_id))
    if result is not None:
        job_id_str = result.groups()[0]
        index_str = result.groups()[2]
        if index_str is None:
            if job_id_str != '0':
                return True

            print "%s: %s" % (job_id, "bad job id")
            return False

        if index_str != '0' and job_id_str != '0':
            return True

        print "%s: %s" % (job_id, "bad array job id")
        return False

    print "%s: %s" % (job_id, "bad job id")
    return False


def is_valid_job_name(job_name):
        # e.g: 100[1]
    pattern = re.compile(r'^(\w+)(\[([1-9]{1}\d*)\-([1-9]{1}\d*)\])?$')
    result = pattern.match(str(job_name))
    if result is not None:
        # print result.groups()
        if result.groups()[1] is None:
            return True

        start_idx = int(result.groups()[2])
        end_idx = int(result.groups()[3])
        if start_idx < end_idx:
            return True

    return False


if __name__ == '__main__':
    job_id_list = [
        'job_name',
        'job[1-100]',
        'job[1-a]',
        'job[0-1]',
        'job[1-10]',
        'job[100-10]',
    ]

    for job_id in job_id_list:
        is_valid_job_name(job_id)
        # if is_job_id(job_id):
        #     print "job id <%s> is ok" % job_id
        # else:
        #     print "bad job id: <%s>" % job_id
