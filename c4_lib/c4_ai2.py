import numpy as np
import random as rnd


# AI logic class for determining the optimal col selection for a passed state

class AI():

    def __init__ (self, player, gameboard, timeout):

        self.height = 6
        self.width = 7
        self.row_len = 4
        self.winner = -1
        self.player = player

        if self.player == 1:
            self.player2 = 2
        else:
            self.player2 = 1

        self.board = gameboard
        self.oldBoard = gameboard
        # self.players = players
        # self.nplayer = player
        # print "HI"

        # print self.players
        # print "Nplayer: " + str(self.nplayer)


    def possible_moves (self):
        results = []
        for i in range(0, self.width):
            if self.board[5][i] == 0:
                results.append(i)

        print results
        return results

    # Check if board is full
    def check_full_board (self):
        for row in self.board:
            for cell in row:
                if (cell == -1):
                    return False
        return True

    # Given col, check for first open cell
    def check_for_col_height (self, col):
        for row in range(0, self.height):
            if (self.board[row][col] == -1):
                return row
        return -1

    # Insert a token into board for specific player if conditions are met.
    def place_token (self, player, col):
        if (col > (self.width - 1) or col < 0 or player > 1 or player < 0):
            return False
        open_row = self.check_for_col_height(col)
        if (open_row == -1):
            return False
        else:
            self.board[open_row][col] = player
            return True

    # Directional logic check functions
    def check_hor (self):
        for row in range(0, self.height):
            for cell in range(0, self.width - (self.row_len - 1)):
                series = 0
                for i in range(1, self.row_len):
                    if (self.board[row][cell] != -1 and self.board[row][cell] == self.board[row][cell + i]):
                         series += 1
                    else:
                        break
                if (series == (self.row_len - 1)):
                    self.winner = self.board[row][cell]
                    return True
        return False

    def check_ver (self):
        for row in range(0, self.height - (self.row_len - 1)):
            for cell in range(0, self.width):
                series = 0
                for i in range(1, self.row_len):
                    if (self.board[row][cell] != -1 and self.board[row][cell] == self.board[row + i][cell]):
                         series += 1
                    else:
                        break
                if (series == (self.row_len - 1)):
                    self.winner = self.board[row][cell]
                    return True

        return False

    def check_diag_right (self):
        for row in range(self.height - (self.row_len - 1)):
            for cell in range(self.width - (self.row_len - 1)):
                series = 0
                for i in range(1, self.row_len):
                    if (self.board[row][cell] != -1 and self.board[row][cell] == self.board[row + i][cell + i]):
                         series += 1
                    else:
                        break
                if (series == (self.row_len - 1)):
                    self.winner = self.board[row][cell]
                    return True
        return False

    def check_diag_left (self):
        for row in range(0, self.height - (self.row_len - 1)):
            # for cell in reversed(range(self.row_len - 2, self.width - 1)):
            for cell in reversed(range(self.row_len - 1, self.width)):
                series = 0
                for i in range(1, self.row_len):
                    if (self.board[row][cell] != -1 and self.board[row][cell] == self.board[row + i][cell - i]):
                         series += 1
                    else:
                        break
                if (series == (self.row_len - 1)):
                    self.winner = self.board[row][cell]
                    return True
        return False

    # Check winning all winning conditions on entire board.
    def check_winner (self):
        if (self.check_ver() or self.check_hor() or self.check_diag_left() or self.check_diag_right()):
            return self.winner
        if (self.check_full_board()):
            return -5
        return -1

    def scoring (self):
        valid = self.possible_moves()

        resultCurrentPlayer = []
        resultCurrentOpp = []
        for i in valid:
            self.board = self.oldBoard
            self.place_token(self.player2, i)
            self.row_len = 4
            self.check_winner()
            if self.winner == self.player2:
                return i

        for i in valid:
            self.board = self.oldBoard
            self.place_token(self.player, i)
            self.row_len = 4
            for j in [4,3,2]:
                self.row_len = j
                self.check_winner()
                print self.winner
                if self.winner == self.player:
                    # return i
                    print "Winner hit"
                    resultCurrentPlayer.append([i,j])
        print "Result List"
        print resultCurrentPlayer
        currentHight = 0
        bestMove = -1
        for i in resultCurrentPlayer:
            if i[1] > currentHight:
                bestMove = i[0]
        if bestMove == -1:
            bestMove = valid[rnd.randrange(0, len(valid))]

        return bestMove
# if __name__ == '__main__':
#
#     neg = Negamax(7, win_score=80)
#     game = ConnectFour()
