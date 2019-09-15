from Graphics import *
from Board import *


class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.board = Board()

    def start(self):
        self.graphics.update_graphics(self.board)
