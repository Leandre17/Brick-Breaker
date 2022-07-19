import pygame
from src.ball import ball


def draw_briks(briks, window):
    tmp = briks.head
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


def draw_bar(window):
    red = 255, 0, 0
    left = pygame.mouse.get_pos()[0] - 50
    if left < 0:
        left = 0
    if left > window.width - 100:
        left = window.width - 100
    rect = pygame.Rect(left, window.height - 75, 100, 3)
    pygame.draw.rect(window.screen, red, rect)


def brick_main(window, briks):
    black = (0, 0, 0)

    window.screen.fill(black)
    ball(window)
    draw_briks(briks, window)
    draw_bar(window)
    pygame.display.flip()
