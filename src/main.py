import pygame
import sys
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, GAME_TITLE, BLACK
from src.game.entities.player import Player
from src.game.levels.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.level = Level()
        self.player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.all_sprites = pygame.sprite.Group(self.player)

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

    def render(self):
        self.screen.fill(BLACK)
        self.level.draw(self.screen)
        self.all_sprites.draw(self.screen)
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
