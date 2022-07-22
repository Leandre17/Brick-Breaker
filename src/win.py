import pygame
from src.window import Window
from src.menu import quit_button, retry_buttun


def win_main(window: Window) -> (None):
    window.screen.fill((0, 0, 0))
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    text00 = my_font.render("You Win", True, (255, 255, 255))
    rect = text00.get_rect(center=(window.width // 2, window.height // 8))
    window.screen.blit(text00, rect)
    quit_button(window)
    retry_buttun(window)
    pygame.display.flip()
