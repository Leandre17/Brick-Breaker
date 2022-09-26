import pygame
from src.window import Window
from src.menu import quit_button, retry_buttun
from src.file_read import read_file, read_color, get_brick


def next_lvl_buttun(window: Window) -> (None):
    blue = 0, 0, 255
    green = 0, 255, 0
    width_by_6 = window.width // 6
    height_by_8 = window.height // 8
    moose = pygame.mouse.get_pos()
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    if len(window.next_level) > 0:
        text10 = my_font.render("Next Level", True, (0, 0, 0))
        text11 = my_font.render("Next Level", True, (0, 0, 255))
    else:
        text10 = my_font.render("    Restart", True, (0, 0, 0))
        text11 = my_font.render("    Restart", True, (0, 0, 255))
    rect = pygame.Rect(width_by_6 * 1.5, height_by_8 * 3, width_by_6 * 3, height_by_8)
    if rect.collidepoint(moose[0], moose[1]):
        if pygame.mouse.get_pressed()[0]:
            window.status = 1
            window.ballrect = pygame.Rect(500, 400, 30, 30)
            window.ball_speed = [0, 2]
            if len(window.next_level) > 0:
                window.old_level.append(window.level)
                window.level = window.next_level.pop(0)
            elif len(window.old_level) > 0:
                window.old_level.append(window.level)
                window.level = window.old_level.pop(0)
                window.next_level = window.old_level
                window.old_level = []
            else:
                window.level = window.level
            color, brique = read_file(window.level)
            if color == None or brique == None or window == None:
                return window
            colors: dict[str, Tuple[int, int, int]] = read_color(color)
            window.bricks = get_brick(brique, colors, window)
        pygame.draw.rect(window.screen, green, rect)
        window.screen.blit(text11, (width_by_6 * 2.3, height_by_8 * 3.25))
    else:
        pygame.draw.rect(window.screen, blue, rect)
        window.screen.blit(text10, (width_by_6 * 2.3, height_by_8 * 3.25))


def win_main(window: Window) -> (None):
    window.screen.fill((0, 0, 0))
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    text00 = my_font.render("You Win", True, (255, 255, 255))
    rect = text00.get_rect(center=(window.width // 2, window.height // 8))
    window.screen.blit(text00, rect)
    quit_button(window)
    next_lvl_buttun(window)
