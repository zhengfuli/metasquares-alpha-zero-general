from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from.ChineseCheckersLogic import Board
import numpy as np

class ChineseCheckersGame(Game):
    def __init__(self, width = 7, homeBorder = 3):
        self.w = width
        self.hb == homeBorder

    def getInitBoard(self):
        b = Board(self.w, self.hb)
        return np.array(b.pieces)