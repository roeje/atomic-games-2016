#!/usr/bin/python

from c4_lib import c4_ai, c4_engine, c4_ai2
import getopt
import sys
import re
import json


def main(argv):
    boardString = ""
    timeout = 0
    height = 6
    width = 7
    win_len = 4
    player = 0

    try:
		# h = height, w = width, r = length to win, l is flag for automatic load
        opts, args = getopt.getopt(argv[1:], "b:p:t")
        print opts
        print args
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

    print player
    if player == "player-one":
        player = 1
    else:
        player = 2
    # print "Board is: "
    # print boardString
    print "player is: " + str(player)
    # print "time: " + str(timeout)

    boardconvert = json.loads(boardString)

    newboard = []

    for i in reversed(boardconvert):
        newboard.append(i)
    # print "New Board"
    # print newboard

    # game = c4_engine.Game(height, width, 4, boardconvert)
    game = c4_ai2.AI(player, newboard, 1500);

    result = game.scoring()
    # game.place_token(1,2)

    # aiEngine = c4_ai.AI([1, 2], 1, boardconvert)
    # aiEngine.main()

    sys.exit(result)

main(sys.argv)
