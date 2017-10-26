#!/usr/bin/env python
# coding=utf8

import re
# import fileinput

# file = fileinput.FileInput('./args.txt', inplace=True)
# pattern = re.compile(r'^\s*master\s*.*$')
# for line in file:
#     result = pattern.match(line)
#     if result is not None:
#         print(line.replace(line, '# ' + line)),
#     else:
#         print(line),

pattern = re.compile(r'^\s*master\s*.*$')
line = 'master       !       ()'
result = pattern.match(line)
print result.group()
