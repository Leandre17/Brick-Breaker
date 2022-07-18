import sys, pygame
from src.brick import bick_main
pygame.init()

count = 0
size = width, height = 1000, 600




screen = pygame.display.set_mode(size)


ball = pygame.image.load("intro_ball.gif")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
clock = pygame.time.Clock()
ballrect = ballrect.move((500, 400))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    clock.tick(60)
    ballrect = bick_main(ball, screen, ballrect)

