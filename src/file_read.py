import pygame
from random import choice
from src.class_brick import Briks
from typing import Tuple
from src.window import Window


def read_data() -> (Window):
    window = Window((1000, 600))
    bricks = Briks()
    try:
        all_file: list[str] = open("level1.txt", "r").read().split("@")
        if len(all_file) < 2:
            print("Error wrong file")
            window.loop = False
            return window
    except:
        print("Error no file")
        window.loop = False
        return window
    color: list[str] = all_file[0].split("\n")
    brique: list[str] = all_file[1].split("\n")
    color.pop(-1)
    brique.pop(0)
    colors: dict[str, Tuple[int, int, int]] = {}
    for i in color:
        tmp = i.split(" ")
        try:
            colors[tmp[0]] = (int(tmp[1]), int(tmp[2]), int(tmp[3]))
        except:
            print("a bad one")
    for i in brique:
        tmp = i.split(", ")
        try:
            rect = pygame.Rect((int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])))
            bricks.push_front(rect, colors[tmp[4]])
        except IndexError:
            bricks.push_front(rect, choice(list(colors.values())))
        except:
            print("a bad one")
    window.bricks = bricks
    return window
