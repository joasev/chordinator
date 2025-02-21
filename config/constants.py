import pygame

key_width = 18
key_intersp = 2
key_height = 100
total_piano_width = (3 + 7 * 7) * (key_width + key_intersp) - key_intersp

BLACK = [  0,   0,   0]
WHITE = [255, 255, 255]
RED = [255,0,0]
SIZE = [total_piano_width, 380]


def get_font():
    if not pygame.get_init():
        raise RuntimeError("Pygame must be initialized before using fonts.")
    return pygame.font.SysFont("Arial", 30)