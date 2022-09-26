import pygame
from src.ball import ball
from src.window import Window
from src.class_brick import Briks, Node


def draw_briks(briks: Briks, window: Window) -> (None):
    tmp: Node = briks.head
    while tmp != None:
        if window.ballrect.colliderect(tmp.rect) and tmp.visible:
            if window.ballrect.collidepoint(tmp.rect.right, tmp.rect.bottom):
                window.ball_speed[1] = -window.ball_speed[1]
            else:
                window.ball_speed[0] = -window.ball_speed[0]
            tmp.visible = False
        if tmp.visible:
            pygame.draw.rect(window.screen, tmp.color, tmp.rect)
        tmp = tmp.next


def draw_bar(window: Window) -> (None):
    red = 255, 0, 0
    left = pygame.mouse.get_pos()[0] - 50
    if left < 0:
        left = 0
    if left > window.width - 100:
        left = window.width - 100
    rect = pygame.Rect(left, window.height - 75, 100, 3)
    pygame.draw.rect(window.screen, red, rect)


def draw_bar_color(window: Window) -> (None):
    moose = pygame.mouse.get_pos()[0]
    if moose > window.width - 50:
        moose = window.width - 50
    if moose <= 50:
        moose = 50
    pygame.draw.rect(
        window.screen, (255, 255, 0), (moose - 50, window.height - 75, 35, 3)
    )
    pygame.draw.rect(
        window.screen, (0, 255, 0), (moose - 15, window.height - 75, 30, 3)
    )
    pygame.draw.rect(
        window.screen, (0, 255, 255), (moose + 15, window.height - 75, 35, 3)
    )


def brick_main(window: Window) -> (None):
    black = (0, 0, 0)
    briks = window.bricks
    window.screen.fill(black)
    ball(window)
    draw_briks(briks, window)
    draw_bar(window)
    if window.bar_color == True:
        draw_bar_color(window)

    if window.bricks.size_visible() == 0:
        print("You Win!")
        window.status = 3
