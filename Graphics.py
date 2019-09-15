from Board import *
import pygame


class Graphics:
    def __init__(self):
        self.window_size = [600, 600]
        self.square_size = self.window_size[0] // 8
        self.piece_size = self.square_size // 2
        self.screen = pygame.display.set_mode((self.window_size[0], self.window_size[1]))
        self.background = pygame.image.load('resources/board.png')

    def update_graphics(self, board):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background.get_rect())
        self.draw_board(board)
        pygame.display.update()

    def draw_board(self, board):
        for checker in board.get_ai_checkers():
            pygame.draw.circle(self.screen, RED, self.get_pixel_pos(checker.pos()), self.piece_size)
        for checker in board.get_player_checkers():
            pygame.draw.circle(self.screen, BLUE, self.get_pixel_pos(checker.pos()), self.piece_size)

    def get_pixel_pos(self, idx):
        return self.square_size * (idx % 8) + self.piece_size, self.square_size * (idx // 8) + self.piece_size
