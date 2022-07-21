#!/usr/bin/env python3

import pygame
from src.window import Window
from src.brick import brick_main
from src.class_brick import Briks
from src.file_read import read_data
from src.menu import main_menu
from src.win import win_main
from src.loose import loose_main


def brick_breaker() -> (None):
    pygame.init()
    window = read_data()

    fnction = {0: main_menu, 1: brick_main, 2: loose_main, 3: win_main}
    while window.loop:
        fnction[window.status](window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.loop = False
        if window.bricks.size_visible() == 0:
            print("You Win!")
            window.status = 3
        pygame.time.Clock().tick(60)
    pygame.quit()


def main() -> (None):
    brick_breaker()


if __name__ == "__main__":
    main()
