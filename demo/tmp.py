# #!/usr/bin/python


# from argparse import ArgumentParser


# parser = ArgumentParser(
#     prog='jjobs',
#     description='description: displays information about jobs')

# parser.add_argument('-m',
#                     type=str,
#                     help='only displays jobs in the specified hosts',
#                     metavar='host_name')


# args = parser.parse_args()
# print args.m


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--mode', required=True, type=str)
# parser.add_argument('--mode')
p = parser.parse_args()
print 'p.mode= <%s>' % p.mode.split()
