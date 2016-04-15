#!/usr/bin/env python
# coding=utf8

import getopt
import sys


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        print "error"
        sys.exit(2)
    output = None
    verbose = False
    print opts, args
    for o, a in opts:
        if o == "-v":
            verbose = True
            print verbose
        elif o in ("-h", "--help"):
            print "help"
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
            print output
        else:
            assert False, "unhandled option"
    # ...


if __name__ == "__main__":
    main()
