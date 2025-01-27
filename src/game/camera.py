import pygame
from utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(WINDOW_WIDTH / 2)
        y = -target.rect.centery + int(WINDOW_HEIGHT / 2)

        # Limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WINDOW_WIDTH), x)  # right
        y = max(-(self.height - WINDOW_HEIGHT), y)  # bottom

        self.camera = pygame.Rect(x, y, self.width, self.height)
