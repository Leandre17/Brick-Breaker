import pygame
from src.window import Window


def key_down_event(window: Window, event) -> (Window):
    if event.unicode == "b":
        if window.bar_color == True:
            window.bar_color = False
        else:
            window.bar_color = True
    if event.unicode == "q":
        window.loop = False
    if event.key == 27:
        if window.status == 1:
            window.status = 4
        elif window.status == 4:
            window.status = 1
    return window


def all_event(window: Window) -> (Window):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.loop = False
        if event.type == pygame.KEYDOWN:
            window = key_down_event(window, event)
    return window
