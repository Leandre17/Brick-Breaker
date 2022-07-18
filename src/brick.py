import sys, pygame


speed = [-2, -2]

def bick_main(ball, screen, ballrect):
    size = width, height = 1000, 600
    black = 0, 0, 0
    color = (255,0,0)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.colliderect(pygame.mouse.get_pos()[0], height - 75, 100, 3):
        speed[1] = -speed[1]
    if ballrect.bottom > height:
        print("You loose!")
        sys.exit(0)
    screen.fill(black)
    if not ballrect.colliderect(pygame.Rect(30, 30, 60, 60)):
        pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(screen, color, pygame.Rect(pygame.mouse.get_pos()[0], height - 75, 100, 3))
    screen.blit(ball, ballrect)
    pygame.display.flip()
    return ballrect