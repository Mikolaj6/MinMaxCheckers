from Checker import *
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)
GOLD     = (255, 215,   0)
HIGH     = (160, 190, 255)


class Field:
    def __init__(self, _black, position, control_type):
        self.color = WHITE if not _black else BLACK
        self.checker = None if control_type == NONE else Checker(control_type, position)

    def remove_checker(self):
        self.checker = None
