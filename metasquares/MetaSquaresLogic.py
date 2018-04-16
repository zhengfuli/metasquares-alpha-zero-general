# With Reference from https://github.com/suragnair
# /alpha-zero-general/blob/master/othello/OthelloLogic.py
# and gobang/GobangLogic.py

# Board class.
# Board data:
#   1=white, -1=black, 0=empty
#   first dim is column , 2nd is row:
#      pieces[1][7] is the square in column 2,
#      at the opposite end of the board in row 8.
# Squares are stored and manipulated as (x,y) tuples.
# x is the column, y is the row.

import numpy as np

class Board(object):

    def __init__(self, n):
        self.n = n
        self.pieces = [[0]*self.n for i in xrange(self.n)]
        self.squaresMap = [{'points':4,'tiles':[[[x,y],[x,y+1],[x+1,y],[x+1,y+1]]
                                                for x in xrange(self.n-1) for y in xrange(self.n-1)]},
                           {'points':4,'tiles':[[[x,y],[x+1,y+1],[x+2,y],[x+1,y-1]]
                                                for x in xrange(self.n-2) for y in xrange(1,self.n-1)]},
                           {'points':9,'tiles':[[[x,y],[x,y+2],[x+2,y],[x+2,y+2]]
                                                for x in xrange(self.n-2) for y in xrange(self.n-2)]},
                           {'points':9,'tiles':[[[x,y],[x+1,y+2],[x+3,y+1],[x+2,y-1]]
                                                for x in xrange(self.n-3) for y in xrange(1,self.n-2)]},
                           {'points':9,'tiles':[[[x,y],[x+2,y+1],[x+3,y-1],[x+1,y-2]]
                                                for x in xrange(self.n-3) for y in xrange(2,self.n-1)]},
                           {'points':9,'tiles':[[[x,y],[x+2,y+2],[x+4,y],[x-2,y-2]]
                                                for x in xrange(self.n-4) for y in xrange(2,self.n-2)]},
                           {'points':16,'tiles':[[[x,y],[x,y+3],[x+3,y+3],[x+3,y]]
                                                for x in xrange(self.n-3) for y in xrange(self.n-3)]},
                           {'points':16,'tiles':[[[x,y],[x+1,y+3],[x+4,y+2],[x+3,y-1]]
                                                for x in xrange(self.n-4) for y in xrange(1,self.n-3)]},
                           {'points':16,'tiles':[[[x,y],[x+2,y+3],[x+5,y+1],[x+3,y-2]]
                                                for x in xrange(self.n-5) for y in xrange(2,self.n-3)]},
                           {'points':25,'tiles':[[[x,y],[x+3,y+3],[x,y+6],[x+3,y-3]]
                                                for x in xrange(self.n-6) for y in xrange(3,self.n-3)]},
                           {'points':16,'tiles':[[[x,y],[x+3,y+2],[x+5,y-1],[x+2,y-3]]
                                                for x in xrange(self.n-4) for y in xrange(3,self.n-1)]},
                           {'points':16,'tiles':[[[x,y],[x+3,y+1],[x+4,y-2],[x+1,y-3]]
                                                for x in xrange(self.n-4) for y in xrange(3,self.n-1)]},
                           {'points':25,'tiles':[[[x,y],[x,y+4],[x+4,y+4],[x+4,y]]
                                                for x in xrange(self.n-4) for y in xrange(self.n-4)]},
                           {'points':25,'tiles':[[[x,y],[x+4,y+1],[x+5,y+3],[x+4,y-1]]
                                                for x in xrange(self.n-5) for y in xrange(1,self.n-4)]},
                           {'points':25,'tiles':[[[x,y],[x+2,y+4],[x+6,y+2],[x+4,y-2]]
                                                for x in xrange(self.n-6) for y in xrange(2,self.n-4)]},
                           {'points':25,'tiles':[[[x,y],[x+4,y+2],[x+6,y-2],[x+2,y-4]]
                                                for x in xrange(self.n-6) for y in xrange(4,self.n-2)]},
                           {'points':25,'tiles':[[[x,y],[x+4,y+1],[x+5,y-3],[x+1,y-4]]
                                                for x in xrange(self.n-5) for y in xrange(4,self.n-1)]},
                           {'points':36,'tiles':[[[x,y],[x,y+5],[x+5,y+5],[x+5,y]]
                                                for x in xrange(self.n-5) for y in xrange(self.n-5)]},
                           {'points':36,'tiles':[[[x,y],[x+1,y+5],[x+6,y+4],[x+5,y-1]]
                                                for x in xrange(self.n-6) for y in xrange(1,self.n-5)]},
                           {'points':36,'tiles':[[[x,y],[x+2,y+5],[x+7,y+3],[x+5,y-2]]
                                                for x in xrange(self.n-7) for y in xrange(2,self.n-5)]},
                           {'points':36,'tiles':[[[x,y],[x+3,y+4],[x+7,y+1],[x+4,y-3]]
                                                for x in xrange(self.n-7) for y in xrange(3,self.n-4)]},
                           {'points':36,'tiles':[[[x,y],[x+4,y+3],[x+7,y-1],[x+3,y-4]]
                                                for x in xrange(self.n-7) for y in xrange(4,self.n-3)]},
                           {'points':36,'tiles':[[[x,y],[x+5,y+2],[x+7,y-3],[x+2,y-5]]
                                                for x in xrange(self.n-7) for y in xrange(5,self.n-2)]},
                           {'points':36,'tiles':[[[x,y],[x+5,y+1],[x+6,y-4],[x+1,y-5]]
                                                for x in xrange(self.n-6) for y in xrange(5,self.n-1)]},
                           {'points':49,'tiles':[[[x,y],[x,y+6],[x+6,y+6],[x+6,y]]
                                                for x in xrange(self.n-6) for y in xrange(self.n-6)]},
                           {'points':49,'tiles':[[[x,y],[x+1,y+6],[x+7,y+5],[x+6,y-1]]
                                                for x in xrange(self.n-7) for y in xrange(1,self.n-6)]},
                           {'points':49,'tiles':[[[x,y],[x+6,y+1],[x+7,y-5],[x+1,y-6]]
                                                for x in xrange(self.n-7) for y in xrange(6,self.n-1)]},
                           {'points':64,'tiles':[[[x,y],[x,y+7],[x+7,y+7],[x+7,y]]
                                                for x in xrange(self.n-7) for y in xrange(self.n-7)]}]

    def __getitem__(self, index):
        return self.pieces[index]

    def count_score(self, player):
        score = 0
        for squareType in self.squaresMap:
            points = squareType['points']
            for tiles in squareType['tiles']:
                checkFlag = 0
                tileNum = 0
                while tileNum < 4 and checkFlag == 0:
                    if self.pieces[tiles[tileNum][0]][tiles[tileNum][1]] != player:
                        checkFlag = 1
                    tileNum += 1
                if checkFlag == 0:
                    score += points
        return score

    def get_legal_moves(self, color):
        moves = set()
        for y in xrange(self.n):
            for x in xrange(self.n):
                if self[x][y] == 0:
                    moves.add((x,y))
        return list(moves)

    def has_legal_moves(self):
        for y in xrange(self.n):
            for x in xrange(self.n):
                if self[x][y] == 0:
                    return True
        return False

    def execute_move(self, move, color):
        (x,y) = move
        assert self[x][y] == 0
        self[x][y] = color

