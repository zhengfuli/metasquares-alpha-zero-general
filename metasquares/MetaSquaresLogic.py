# Author: Zhengfu Li
# Date: Mar. 28, 2018
import chess
import numpy as np

class Board(object):
        # Input:
        #    int width
        #    int homeBorder
        # Output:
        #    list[list]

        # width(diagonal length))
        # 0 0 0 0 1 1 1
        # 0 0 0 0 0 1 1
        # 0 0 0 0 0 0 1 homeBorder
        # 0 0 0 0 0 0 0
        #-1 0 0 0 0 0 0
        #-1-1 0 0 0 0 0
        #-1-1-1 0 0 0 0

        # 1 = white, -1 = black, 0 = empty
        # default: 7, 3; standard: 9, 4

    def __init__(self, width, homeBorder):
        self.w = width
        self.hb = homeBorder
        self.pieces = [[0]*self.w for i in xrange(self.w)]
        self.directions = ((-1,0),(0,1),(1,1),(1,0),(0,-1),(-1,-1))

        for i in xrange(self.w):
            for j in xrange(self.w):
                if i<self.hb and j>=(self.w-self.hb+i):
                    self.pieces[i][j] = 1
                elif i>=(self.w-self.hb) and j<=(self.hb+i-self.w):
                    self.pieces[i][j] = -1

        def __getitem__(self, index):
            return self.pieces[index]

    # return all legal moves for a given color
    # input:
    #    int color = -1 for black, 1 for white
    # output:
    #    list moves [list[int from_row, from_col, to_row, to_row]]
    def get_legal_moves(self, color):
        moves = set()

        # find current positions of checkers in this color
        for row in xrange(len(self.pieces)):
            for col in xrange(len(self.pieces[row])):
                if self.pieces[row][col] == color:






# def bb2array(b):  # board to vector of len 64
#     x = np.zeros(64, dtype=np.int8)
#     # print('Flipping: ', flip)
#     for pos in range(64):
#         piece = b.piece_type_at(pos)  # Gets the piece type at the given square. 0==>blank,1,2,3,4,5,6
#         if piece:
#             color = int(bool(b.occupied_co[chess.BLACK] & chess.BB_SQUARES[pos]))  # to check if piece is black or white
#             # print ('piece: ', piece, 'b.occupied_co[chess.BLACK]: ', b.occupied_co[chess.BLACK], 'chess.BB_SQUARES[pos]: ', chess.BB_SQUARES[pos], 'color: ', color, 'pos: ', pos, '\t', b.occupied_co[chess.BLACK] & chess.BB_SQUARES[pos])
#             col = int(pos % 8)
#             row = int(pos / 8)
#             #		if flip:
#             #		row = 7-row
#             #		color = 1 - color
#             x[row * 8 + col] = -piece if color else piece
#     t = b.turn
#     c = b.castling_rights
#     e = b.ep_square
#     h = b.halfmove_clock
#     f = b.fullmove_number
#     return x
#
#
# def vector2matrix(x):
#     y = np.reshape(x, (8, 8))
#     return y

if __name__ == '__main__':
    b = Board(7,3)
    b.get_legal_moves(-1)
#     print b.pieces
#     board = chess.Board()
#     X = np.array([bb2array(board)])
#     pieces = vector2matrix(X[0])
#     chessboard = board
#     print pieces, chessboard

