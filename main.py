#!/usr/bin/env python3

import sys, pygame
from src.brick import brick_main
from src.window import Window
from src.class_brick import Briks


def brick_breaker():
    red = 255, 0, 0
    blue = 0, 0, 255
    violet = 255, 0, 255
    pygame.init()
    bricks = Briks()
    bricks.push_front(pygame.Rect(20, 30, 50, 30), red)
    bricks.push_front(pygame.Rect(90, 30, 50, 30), blue)
    bricks.push_front(pygame.Rect(160, 30, 50, 30), violet)
    bricks.push_front(pygame.Rect(230, 30, 50, 30), red)
    bricks.push_front(pygame.Rect(300, 30, 50, 30), blue)
    bricks.push_front(pygame.Rect(370, 30, 50, 30), violet)
    bricks.push_front(pygame.Rect(440, 30, 50, 30), red)
    bricks.push_front(pygame.Rect(510, 30, 50, 30), blue)
    bricks.push_front(pygame.Rect(580, 30, 50, 30), violet)
    bricks.push_front(pygame.Rect(650, 30, 50, 30), red)
    bricks.push_front(pygame.Rect(720, 30, 50, 30), blue)
    bricks.push_front(pygame.Rect(790, 30, 50, 30), violet)
    bricks.push_front(pygame.Rect(860, 30, 50, 30), red)
    bricks.push_front(pygame.Rect(930, 30, 50, 30), blue)
    window = Window((1000, 600))
    while window.loop:
        brick_main(window, bricks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.loop = False
        if bricks.size_visible() == 0:
            print("You Win!")
            window.loop = False
        pygame.time.Clock().tick(60)


def main():
    brick_breaker()


if __name__ == "__main__":
    main()
