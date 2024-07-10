import pygame
import sys
from utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, GAME_TITLE, BLACK
from game.entities.player import Player
from game.levels.level import Level
from game.camera import Camera
from game.background import Background


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = Background('assets/images/background.png')
        self.level = Level()
        self.player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.all_sprites = pygame.sprite.Group(self.player)

        self.camera = Camera(WINDOW_WIDTH * 3, WINDOW_HEIGHT * 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def update(self):
        self.all_sprites.update(self.level.platforms)
        self.level.update()
        self.camera.update(self.player)
        self.background.update(self.camera.camera.x)

    def render(self):
        self.background.draw(self.screen)

        for platform in self.level.platforms:
            self.screen.blit(platform.image, self.camera.apply(platform))

        self.screen.blit(self.player.image, self.camera.apply(self.player))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
