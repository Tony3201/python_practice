#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('bar', nargs='?')
print parser.parse_args(['--foo', '1', 'BAR'])
print parser.parse_args([])
print parser.parse_args([])
