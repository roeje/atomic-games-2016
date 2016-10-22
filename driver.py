#!/usr/bin/python

from c4_lib import c4_ai, c4_engine
import getopt
import sys
import re


def main(argv):
    boardString = ""
    timeout = 0
    height = 6
    width = 7
    win_len = 4
    player = 0

    try:
		# h = height, w = width, r = length to win, l is flag for automatic load
	    opts, args = getopt.getopt(argv, "b:p:t")
    except getopt.GetoptError:
	    # print "Parameters were missing. Please provide: -h height, -w width, -r row length. Add -l if you would like to load a saved game"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-b':
            boardString = arg
        elif opt == "-p":
            player = arg
        elif opt == "-t":
            timeout = arg

    print "Board is: " + boardString
    print "player is: " + str(player)
    print "time: " + str(timeout)

    sys.exit(5)

main(sys.argv)
