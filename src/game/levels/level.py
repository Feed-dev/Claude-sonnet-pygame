import pygame
from src.game.entities.platform import Platform
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, GROUND_HEIGHT

class Level:
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.create_level()

    def create_level(self):
        # Create ground
        ground = Platform(0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, GROUND_HEIGHT)
        self.platforms.add(ground)

        # Create some platforms
        platform1 = Platform(100, 400, 200, 20)
        platform2 = Platform(400, 300, 200, 20)
        platform3 = Platform(700, 200, 200, 20)

        self.platforms.add(platform1, platform2, platform3)

    def update(self):
        # We can add moving platforms or other dynamic elements here in the future
        pass

    def draw(self, surface):
        for platform in self.platforms:
            platform.draw(surface)
