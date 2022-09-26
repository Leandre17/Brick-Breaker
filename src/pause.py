import pygame
from src.window import Window


def pause_main(window: Window) -> (None):
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    text00 = my_font.render("Pause", True, (255, 255, 255))
    rect = text00.get_rect(center=(window.width // 2, window.height // 3))
    window.screen.blit(text00, rect)
