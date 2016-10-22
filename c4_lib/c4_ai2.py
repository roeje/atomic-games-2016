import numpy as np

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


    def possible_moves(self):
        results = []
        for i in range(0, self.width):
            if self.board[0][i] == 0:
                results.append(i)

        print results
        return results

    # def make_move(self, move):
    #     row = np.argmin(board[:, move] != 0)
    #     board[row][move] = nplayer
    #
    # def is_over(self):
    #     return (self.board.min() > 0) or self.lose();
    #
    # def lose():
    #     check_winner()
    #     if self.winner == self.nopponent:
    #         return True
    #     else:
    #         return False

    def scoring(self):
        valid = []

        vaild = self.possible_moves()
        resultCurrentPlayer = []
        resultCurrentOpp = []
        for i in valid:
            self.board = self.oldBoard
            place_token(player2)
            self.row_len = 4
            check_winner()
            if self.winner == player2:
                return i

            self.board = self.oldBoard
            place_token(player)
            for j in [4,3,2]:
                self.row_len = j
                check_winner()
                if self.winner == player:
                    return i
        return 3;



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

# if __name__ == '__main__':
#
#     neg = Negamax(7, win_score=80)
#     game = ConnectFour()
