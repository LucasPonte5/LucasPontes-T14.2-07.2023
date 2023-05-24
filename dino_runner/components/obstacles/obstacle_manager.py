import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        figure = random.randint(0,2)
        if len(self.obstacles) == 0:
            if figure == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS[random.randint(0, 2)]))
            elif figure == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0, 2)]))
            elif figure == 2:
                self.obstacles.append(Bird(BIRD[random.randint(0,1)]) )

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
            

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        