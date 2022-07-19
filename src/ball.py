import pygame


def ball(window):
    window.ballrect = window.ballrect.move(window.ball_speed)
    if window.ballrect.left < 0 or window.ballrect.right > window.width:
        window.ball_speed[0] = -window.ball_speed[0]
    if window.ballrect.top < 0 or window.ballrect.colliderect(
        pygame.mouse.get_pos()[0] - 50, window.height - 75, 100, 3
    ):
        window.ball_speed[1] = -window.ball_speed[1]
    if window.ballrect.bottom > window.height:
        print("You loose!")
        window.loop = False
    window.screen.blit(window.ball, window.ballrect)
