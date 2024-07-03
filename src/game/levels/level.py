import pygame
from game.entities.platform import Platform
from utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, GROUND_HEIGHT


class Level:
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.width = WINDOW_WIDTH * 3
        self.height = WINDOW_HEIGHT * 2
        self.create_level()

    def create_level(self):
        # Create ground
        ground = Platform(0, self.height - GROUND_HEIGHT, self.width, GROUND_HEIGHT)
        self.platforms.add(ground)

        # Create some platforms
        platform1 = Platform(100, 400, 200, 20)
        platform2 = Platform(400, 300, 200, 20)
        platform3 = Platform(700, 200, 200, 20)
        platform4 = Platform(1000, 400, 200, 20)
        platform5 = Platform(1300, 300, 200, 20)
        platform6 = Platform(1600, 200, 200, 20)
        platform7 = Platform(1900, 400, 200, 20)

        self.platforms.add(platform1, platform2, platform3, platform4, platform5, platform6, platform7)

    def update(self):
        # We can add moving platforms or other dynamic elements here in the future
        pass

    def draw(self, surface, camera):
        for platform in self.platforms:
            surface.blit(platform.image, camera.apply(platform))
