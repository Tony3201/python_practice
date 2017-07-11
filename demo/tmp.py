#!/usr/bin/python


def check_job_name(job_name):
    left_bracket_index = job_name.find('[')
    right_bracket_index = job_name.find(']')
    hyphen_index = job_name.find('-')

    if left_bracket_index < 0 and \
            right_bracket_index < 0 and \
            hyphen_index < 0:

        return True

    if left_bracket_index < right_bracket_index and \
            left_bracket_index < hyphen_index and \
            hyphen_index < right_bracket_index:

        array_index_start = job_name[
            left_bracket_index + 1:hyphen_index].strip()

        array_index_end = job_name[
            hyphen_index + 1:right_bracket_index].strip()

        if array_index_start.isdigit() and array_index_end.isdigit():
            if int(array_index_start) < int(array_index_end):
                return True

    return False


print check_job_name('aa[14]')
print check_job_name('aa[11-4]')
print check_job_name('bb[1-aa]')
print check_job_name('33[1a-2]')
