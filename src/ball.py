import pygame
from src.window import Window


def check_ball_bar_colide(window: Window) -> (None):
    moose = pygame.mouse.get_pos()[0]
    if moose > window.width - 100:
        moose = window.width - 100
    if moose <= 50:
        moose = 50
    # For the left
    if window.ballrect.colliderect((moose - 50, window.height - 74, 35, 3)):
        window.ball_speed[1] = -window.ball_speed[1]
        window.ball_speed[0] = -3
    # For the midle
    if window.ballrect.colliderect((moose - 15, window.height - 75, 30, 3)):
        window.ball_speed[1] = -window.ball_speed[1]
        window.ball_speed[0] = window.ball_speed[0] // 3
    # For the right
    if window.ballrect.colliderect((moose + 15, window.height - 74, 35, 3)):
        window.ball_speed[1] = -window.ball_speed[1]
        window.ball_speed[0] = 3


def ball(window: Window) -> (None):
    window.ballrect = window.ballrect.move(window.ball_speed)
    if window.ballrect.left < 0 or window.ballrect.right > window.width:
        window.ball_speed[0] = -window.ball_speed[0]
    if window.ballrect.top < 0:
        window.ball_speed[1] = -window.ball_speed[1]
    if window.ballrect.bottom > window.height:
        print("You loose!")
        window.loop = False
    check_ball_bar_colide(window)
    window.screen.blit(window.ball, window.ballrect)
