import sys, pygame
from typing import Tuple, Any
from pygame import Surface

class Window:
    def __init__(self: Any, size: Tuple[int, int]) -> (None):
        self.ball_init("intro_ball.gif", (30, 30))
        self.size = self.width, self.height = size
        self.screen = pygame.display.set_mode(size)
        self.ball_speed = [0, 2]
        self.loop = True

    def ball_init(self: Any, path: str, ball_size: Tuple[int, int]) -> (None):
        self.ball = pygame.image.load(path)
        self.ball = pygame.transform.scale(self.ball, ball_size)
        self.ballrect = self.ball.get_rect()
        self.ballrect = self.ballrect.move((500, 400))
