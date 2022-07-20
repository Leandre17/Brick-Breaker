#!/usr/bin/env python3

import sys, pygame
from src.brick import brick_main
from src.window import Window
from src.class_brick import Briks
from src.file_read import read_data


def brick_breaker() -> (None):
    pygame.init()
    bricks = Briks()
    window = read_data(bricks)

    while window.loop:
        brick_main(window, bricks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.loop = False
        if bricks.size_visible() == 0:
            print("You Win!")
            window.loop = False
        pygame.time.Clock().tick(60)


def main() -> (None):
    brick_breaker()


if __name__ == "__main__":
    main()
