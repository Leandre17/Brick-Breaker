import pygame
from random import choice
from src.class_brick import Briks
from typing import Tuple, Any
from src.window import Window


def read_color(color: list[str]) -> (dict[str, Tuple[int, int, int]]):
    colors: dict[str, Tuple[int, int, int]] = {}
    for i in color:
        tmp = i.split(" ")
        try:
            if (
                int(tmp[1]) >= 0
                and int(tmp[1]) < 256
                and int(tmp[2]) >= 0
                and int(tmp[2]) < 256
                and int(tmp[3]) >= 0
                and int(tmp[3]) < 256
            ):
                colors[tmp[0]] = (int(tmp[1]), int(tmp[2]), int(tmp[3]))
            else:
                print("a bad color number")
        except:
            print("a bad line in the color part")
    return colors


def get_brick(brique: list[str], colors: dict[str, Tuple[int, int, int]]) -> (Briks):
    bricks = Briks()

    for i in brique:
        tmp = i.split(", ")
        try:
            rect = pygame.Rect((int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])))
            bricks.push_front(rect, colors[tmp[4]])
        except IndexError:
            bricks.push_front(rect, choice(list(colors.values())))
        except KeyError:
            bricks.push_front(rect, choice(list(colors.values())))
        except:
            print("a bad one")
    return bricks


def read_file(filename: str) -> (Any):
    try:
        all_file: list[str] = open(filename, "r").read().split("@")
        if len(all_file) < 2:
            print("Error wrong file")
            return None
    except:
        print("Error no file")
        return None
    color: list[str] = all_file[0].split("\n")
    brique: list[str] = all_file[1].split("\n")
    color.pop(-1)
    brique.pop(0)
    return color, brique


def read_data() -> (Window):
    window = Window((1000, 600))
    color, brique = read_file("level1.txt")
    if color == None or brique == None:
        return window
    colors: dict[str, Tuple[int, int, int]] = read_color(color)
    window.bricks = get_brick(brique, colors)
    return window
