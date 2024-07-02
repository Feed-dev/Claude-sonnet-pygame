import pygame
from utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_SPEED, PLAYER_JUMP_STRENGTH, GRAVITY, NEON_BLUE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(NEON_BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False

    def update(self, platforms):
        self.apply_gravity()
        self.handle_movement()
        self.handle_collisions(platforms)

    def apply_gravity(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        self.velocity_x = 0
        if keys[pygame.K_LEFT]:
            self.velocity_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.velocity_x = PLAYER_SPEED
        self.rect.x += self.velocity_x

    def handle_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:  # Jumping
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

    def jump(self):
        if self.on_ground:
            self.velocity_y = -PLAYER_JUMP_STRENGTH

    def draw(self, surface):
        surface.blit(self.image, self.rect)
