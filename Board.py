from Field import *


class Board:
    def __init__(self):
        self.matrix = []
        self.ai_checkers = set()
        self.player_checkers = set()
        self.get_starting_board()

    def get_starting_board(self):
        self.matrix.clear()
        self.ai_checkers.clear()
        self.player_checkers.clear()

        for idx in range(64):
            _type = NONE
            if self.field_is_black(idx) and idx < 24:
                _type = AI
            if self.field_is_black(idx) and idx >= 40:
                _type = PLAYER
            self.matrix.append(Field(self.field_is_black(idx), idx, _type))

            if self.matrix[idx].checker is not None:
                if self.matrix[idx].checker.is_ai():
                    self.ai_checkers.add(self.matrix[idx].checker)
                else:
                    self.player_checkers.add(self.matrix[idx].checker)

    def get_ai_checkers(self):
        return self.ai_checkers

    def get_player_checkers(self):
        return self.player_checkers

    @staticmethod
    def field_is_black(idx):
        return True if ((idx % 8) + (idx // 8)) % 2 == 0 else False
