#!/usr/bin/python


def is_valid_job_id(job_id):
    left_bracket_index = job_id.find('[')
    right_bracket_index = job_id.find(']')
    is_job_array = left_bracket_index >= 0 or right_bracket_index >= 0

    if job_id.isdigit() and int(job_id) > 0:
        return True
    elif not is_job_array:
        print "%s: Illegal job id." % job_id
        return False

    # check job array id, for example: 120[1]
    if left_bracket_index <= 0 \
            or right_bracket_index <= 0 \
            or left_bracket_index > right_bracket_index  \
            or left_bracket_index == right_bracket_index - 1 \
            or right_bracket_index != len(job_id) - 1:

        print "%s: Illegal job id." % job_id
        return False

    job_array_id = job_id[:left_bracket_index]
    job_array_index = job_id[
        left_bracket_index + 1:right_bracket_index]

    is_valid_array = False
    is_valid_index = False
    if job_array_id.isdigit() and int(job_array_id) > 0:
        is_valid_array = True
    else:
        print "%s: Illegal job array id." % job_array_id

    if job_array_index.isdigit() and int(job_array_index) >= 0:
        is_valid_index = True
    else:
        print "%s: Illegal job array index." % job_array_index

    if is_valid_array and is_valid_index:
        return True
    else:
        return False


job_id_list = [
    '1',  # 0
    '1111',  # 1
    '1[1111]',  # 2
    '1[0]',  # 3

    '-1',  # 4
    'abc',  # 5
    '12a',  # 6
    '12[ac]',  # 7
    '1a[123]',  # 8
    '1[123]1',  # 9
    '-0',  # 10
    '[123]',  # 11
    '0[123]',  # 12
    '0[0]',  # 13
    '123[]',  # 14
    '123[]12',  # 15
    '[123]4',  # 16
    '12]234[',  # 17
    '[123',  # 18
    '123]',  # 19
    '[]',  # 20
    ']',  # 21
    '[',  # 22
]

job_id_list_len = len(job_id_list)

for i in xrange(0, job_id_list_len):
    if i == 4:
        print ''
    print i, job_id_list[i],
    print is_valid_job_id(job_id_list[i])
