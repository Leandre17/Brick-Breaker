import pygame
from typing import Tuple, Any
from pygame import Surface
from src.class_brick import Briks


class Window:
    def __init__(self: Any, size: Tuple[int, int]) -> (None):
        self.size = self.width, self.height = size
        self.screen = pygame.display.set_mode(size)
        self.ball_speed = [0, 2]
        self.loop = True
        self.status = 0
        self.bricks: Briks = None
        self.level = None
        self.next_level = []
        self.old_level = []
        self.bar_color = True

    def ball_init(self: Any, path: str, ball_size: Tuple[int, int]) -> (None):
        self.ball = pygame.image.load(path)
        self.ball = pygame.transform.scale(self.ball, ball_size)
        self.ballrect = self.ball.get_rect()
        self.ballrect = self.ballrect.move((500, 400))
