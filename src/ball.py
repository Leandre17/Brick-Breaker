import pygame
from src.window import Window


def ball(window: Window) -> (None):
    moose = pygame.mouse.get_pos()[0]
    window.ballrect = window.ballrect.move(window.ball_speed)
    if window.ballrect.left < 0 or window.ballrect.right > window.width:
        window.ball_speed[0] = -window.ball_speed[0]
    if window.ballrect.top < 0:
        window.ball_speed[1] = -window.ball_speed[1]
    if window.ballrect.bottom > window.height:
        print("You loose!")
        window.loop = False
    if window.ballrect.colliderect((moose - 50, window.height - 74, 35, 3)):
        window.ball_speed[1] = -window.ball_speed[1]
        window.ball_speed[0] = -3
    if window.ballrect.colliderect((moose - 15, window.height - 75, 30, 3)):
        window.ball_speed[1] = -window.ball_speed[1]
        window.ball_speed[0] = window.ball_speed[0] // 3
    if window.ballrect.colliderect((moose + 15, window.height - 74, 35, 3)):
        window.ball_speed[1] = -window.ball_speed[1]
        window.ball_speed[0] = 3
    window.screen.blit(window.ball, window.ballrect)
