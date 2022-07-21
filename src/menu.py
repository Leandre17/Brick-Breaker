import pygame
from src.window import Window


def set_text():
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    text00 = my_font.render("Start", True, (0, 0, 0))
    text01 = my_font.render("Start", True, (0, 0, 255))
    text10 = my_font.render("Option", True, (0, 0, 0))
    text11 = my_font.render("Option", True, (0, 0, 255))
    return (text00, text01, text10, text11)

def quit_button(window: Window):
    blue = 0, 0, 255
    red = 255, 0, 0
    width_by_6 = window.width // 6
    height_by_8 = window.height // 8
    moose = pygame.mouse.get_pos()
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    text1 = my_font.render("Quit", True, (0, 0, 0))
    text2 = my_font.render("Quit", True, (0, 0, 255))
    rect = pygame.Rect(width_by_6 * 1.5, height_by_8 * 5, width_by_6 * 3, height_by_8)
    if rect.collidepoint(moose[0], moose[1]):
        if pygame.mouse.get_pressed()[0]:
            window.loop = False
        pygame.draw.rect(window.screen, red, rect)
        window.screen.blit(text2, (width_by_6 * 2.75, height_by_8 * 5.25))
    else:
        pygame.draw.rect(window.screen, blue, rect)
        window.screen.blit(text1, (width_by_6 * 2.75, height_by_8 * 5.25))


def retry_buttun(window: Window) -> (None):
    blue = 0, 0, 255
    yellow = 255, 255, 0
    width_by_6 = window.width // 6
    height_by_8 = window.height // 8
    moose = pygame.mouse.get_pos()
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    text10 = my_font.render("Retry", True, (0, 0, 0))
    text11 = my_font.render("Retry", True, (0, 0, 255))
    rect = pygame.Rect(width_by_6 * 1.5, height_by_8 * 3, width_by_6 * 3, height_by_8)
    if rect.collidepoint(moose[0], moose[1]):
        if pygame.mouse.get_pressed()[0]:
            window.status = 1
            window.ballrect = pygame.Rect(500, 400, 30, 30)
            window.ball_speed = [0, 2]
            tmp = window.bricks.head
            while tmp != None:
                tmp.visible = True
                tmp = tmp.next
        pygame.draw.rect(window.screen, yellow, rect)
        window.screen.blit(text11, (width_by_6 * 2.615, height_by_8 * 3.25))
    else:
        pygame.draw.rect(window.screen, blue, rect)
        window.screen.blit(text10, (width_by_6 * 2.615, height_by_8 * 3.25))



def main_menu(window: Window) -> (None):
    blue = 0, 0, 255
    green = 0, 255, 0
    yellow = 255, 255, 0
    width_by_6 = window.width // 6
    height_by_8 = window.height // 8
    moose = pygame.mouse.get_pos()
    rect1 = pygame.Rect(width_by_6 * 1.5, height_by_8, width_by_6 * 3, height_by_8)
    rect2 = pygame.Rect(width_by_6 * 1.5, height_by_8 * 3, width_by_6 * 3, height_by_8)

    window.screen.fill((0, 0, 0))
    text00, text01, text10, text11 = set_text()
    if rect1.collidepoint(moose[0], moose[1]):
        if pygame.mouse.get_pressed()[0]:
            window.status = 1
        pygame.draw.rect(window.screen, green, rect1)
        window.screen.blit(text01, (width_by_6 * 2.75, height_by_8 * 1.25))
    else:
        pygame.draw.rect(window.screen, blue, rect1)
        window.screen.blit(text00, (width_by_6 * 2.75, height_by_8 * 1.25))
    if rect2.collidepoint(moose[0], moose[1]):
        pygame.draw.rect(window.screen, yellow, rect2)
        window.screen.blit(text11, (width_by_6 * 2.615, height_by_8 * 3.25))
    else:
        pygame.draw.rect(window.screen, blue, rect2)
        window.screen.blit(text10, (width_by_6 * 2.615, height_by_8 * 3.25))
    quit_button(window)
    pygame.display.flip()
