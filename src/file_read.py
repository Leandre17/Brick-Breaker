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


def get_brick(
    brique: list[str], colors: dict[str, Tuple[int, int, int]], window: Window
) -> (Briks):
    bricks = Briks()

    for i in brique:
        tmp = i.split(", ")
        if len(tmp) < 3:
            continue
        try:
            rect = pygame.Rect((int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])))
            if (
                rect.left < 0
                or rect.right > window.width
                or rect.top < 0
                or rect.bottom > window.height
            ):
                print(f"The brick:  {rect} is not in the screen")
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


def read_config(filepath: str) -> (Window):
    try:
        all_file: list[str] = open(filepath, "r").read().split("\n")
        if len(all_file) < 4:
            print("Error wrong file")
            return None
    except:
        print("Error no config file (.config/config.txt)")
        return None
    width = int(all_file[0].split("=")[1])
    height = int(all_file[1].split("=")[1])
    if width < 300 or height < 300:
        print(
            "Please increase the width or the height to have a window a little visible"
        )
        return None
    window = Window((width, height))
    ball_speed = all_file[2].split("=")[1].split(",")
    window.ball_speed = [int(ball_speed[0]), int(ball_speed[1])]
    size = all_file[5].split("=")[1].split(",")
    window.ball_init(all_file[4].split("=")[1], (int(size[0]), int(size[1])))
    all_level = all_file[3].split("=")[1].split(" ")
    window.level = all_level[0]
    window.next_level = all_level[1::]
    return window


def read_data(filepath: str = "./.config/config.txt") -> (Window):
    window = read_config(filepath)
    color, brique = read_file(window.level)
    if color == None or brique == None or window == None:
        return window
    colors: dict[str, Tuple[int, int, int]] = read_color(color)
    window.bricks = get_brick(brique, colors, window)
    return window
