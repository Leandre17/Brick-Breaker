import pygame
from src.window import Window


def check_ball_bar_colide(window: Window) -> (None):
    moose = pygame.mouse.get_pos()[0]
    if moose > window.width - 50:
        moose = window.width - 50
    if moose <= 50:
        moose = 50
    if window.ballrect.colliderect((moose - 15, window.height - 75, 30, 3)):
        if window.ball_speed[1] < 10:
            window.ball_speed[1] = int(-1.5 * abs(window.ball_speed[1]))
        else:
            window.ball_speed[1] = -1 * abs(window.ball_speed[1])
        window.ball_speed[0] = window.ball_speed[0] // 3
    elif window.ballrect.colliderect((moose - 50, window.height - 75, 35, 3)):
        window.ball_speed[1] = -1 * abs(window.ball_speed[1])
        window.ball_speed[0] = -3
    elif window.ballrect.colliderect((moose + 15, window.height - 75, 35, 3)):
        window.ball_speed[1] = -1 * abs(window.ball_speed[1])
        window.ball_speed[0] = 3


def ball(window: Window) -> (None):
    window.ballrect = window.ballrect.move(window.ball_speed)
    if window.ballrect.left < 0 or window.ballrect.right > window.width:
        window.ball_speed[0] = -window.ball_speed[0]
    if window.ballrect.top < 0:
        window.ball_speed[1] = -window.ball_speed[1]
    if window.ballrect.bottom > window.height:
        print("You loose!")
        window.status = 2
    check_ball_bar_colide(window)
    window.screen.blit(window.ball, window.ballrect)
