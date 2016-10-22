from easyAI import TwoPlayersGame, AI_Player, Negamax
import numpy

# AI logic class for determining the optimal col selection for a passed state

class AI(TwoPlayersGame):

    def __init__ (self, players, player, game):

        self.board = game.board
        self.players = players
        self.nplayer = player
        # print "HI"

        print self.players
        print "Nplayer: " + str(self.nplayer)


    def possible_moves(self):
        print "Moves"
    def make_move(self, move):
        print "make Move"
    def is_over(self):
        print "is over"
    def scoring(self):
        print "Scoring"
