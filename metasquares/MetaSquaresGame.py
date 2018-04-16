from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from.MetaSquaresLogic import Board
import numpy as np

class MetaSquaresGame(Game):
    def __init__(self, n = 8):
        self.n = n

    def getInitBoard(self):
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        return (self.n, self.n)

    def getNextState(self, board, player, action):
        if action == self.n * self.n:
            return (board, -player)
        b = Board(self.n)
        b.pieces = np.copy(board)
        move = (int(action / self.n), action % self.n)
        b.execute_move(move, player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        valids = [0] * (self.n * self.n + 1)
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves = b.get_legal_moves(player)
        if len(legalMoves) == 0:
            valids[-1] = 1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.n * x + y] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):
        b = Board(self.n)
        b.pieces = np.copy(board)
        if b.has_legal_moves():
            return 0
        if b.count_score(player) > b.count_score(-player):
            return 1
        if b.count_score(player) < b.count_score(-player):
            return -1
        return 1e-4

    def getCanonicalForm(self, board, player):
        return player * board

    def getSymmetries(self, board, pi):
        # mirror, rotational
        assert (len(pi) == self.n ** 2 + 1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        # 8x8 numpy array (canonical board)
        return board.tostring()

    def getScore(self, board, player):
        b = Board(self.n)
        b.pieces = np.copy(board)
        return b.count_score(player) - b.count_score(-player)

def display(board):
    n = board.shape[0]

    for y in range(n):
        print(y, "|", end="")
    print("")
    print(" -----------------------")
    for y in range(n):
        print(y, "|", end="")    # print the row #
        for x in range(n):
            piece = board[y][x]    # get the piece to print
            if piece == -1:
                print("b ", end="")
            elif piece == 1:
                print("W ", end="")
            else:
                if x == n:
                    print("-", end="")
                else:
                    print("- ", end="")
        print("|")

    print("   -----------------------")