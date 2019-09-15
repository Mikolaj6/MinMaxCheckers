AI       = -1
PLAYER   = 1
NONE     = 0


class Checker:
    def __init__(self, _ai, _position, is_king=False):
        self.ai = True if _ai == AI else False
        self.king = is_king
        self.position = _position

    def is_ai(self):
        return self.ai

    def pos(self):
        return self.position

    def __hash__(self):
        return hash((self.ai, self.king, self.position))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.ai == other.ai and self.king == other.king and self.position == other.position
