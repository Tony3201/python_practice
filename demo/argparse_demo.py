#!/usr/bin/env python
# coding=utf8

import argparse


parent_parser = argparse.ArgumentParser(prog="parent",add_help=False)
parent_parser.add_argument("--parent")

parser = argparse.ArgumentParser(
	prog="demo",
	usage="usage xxx",
	description='''description 1
description 2
	description 3''',
	epilog='''epilog 1
epilog 2
	epilog 3''',
	parents=[parent_parser],
	# formatter_class=argparse.RawDescriptionHelpFormatter,
	formatter_class=argparse.RawTextHelpFormatter,
	# formatter_class=argparse.ArgumentDefaultsHelpFormatter,
	prefix_chars="-+/",
	argument_default=argparse.SUPPRESS,
	conflict_handler='resolve'
	)


parser.add_argument("--demo1")
parser.add_argument("-demo2")
parser.add_argument("++demo3")
parser.add_argument("/demo4")
parser.add_argument("name")
parser.add_argument("--demo1")
# Namespace(demo1='d1', demo2='d2', demo3='d3', demo4='d4', name='leo', parent='d5')
args = parser.parse_args()

print args
