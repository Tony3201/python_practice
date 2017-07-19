#!/usr/bin/python


f = open("/apps/users/jhadmin/job_ids")
line = f.readline()
job_id = 1
while line:
    if int(line) != job_id:
        print job_id
        job_id += 2
    else:
        job_id += 1

    line = f.readline()

f.close()

# job_id_list.sort()


# f = open("/apps/users/jhadmin/job_id_list", 'w+')
# for job_id in job_id_list:
#     f.write(str(job_id) + '\n')
