import random
import pygame

from dino_runner.components.obstacles.meteoro import Meteoro
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, METEORO
pygame.init()

meteoro_sound = pygame.mixer.Sound("dino_runner/assets/Music/Meteoro.wav")
passaro = pygame.mixer.Sound("dino_runner/assets/Music/Passaro.wav")
gameover = pygame.mixer.Sound("dino_runner/assets/Music/Gameover.wav")
quebrando = pygame.mixer.Sound("dino_runner/assets/Music/Quebrando.mp3")
batida = pygame.mixer.Sound("dino_runner/assets/Music/Batida.wav")


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            figura = random.randint(1,4)
            if figura == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0,2)]))
            elif figura == 2:
                cactus = Cactus(LARGE_CACTUS[random.randint(0,2)])
                cactus.rect.y = 300
                self.obstacles.append(cactus)
            elif figura == 3:
                self.obstacles.append(Bird(BIRD))
                passaro.play()
            elif figura == 4:
                self.obstacles.append(Meteoro(METEORO))
                meteoro_sound.play()
                

                
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up and game.death_count <=3:
                    batida.play()
                    pygame.time.delay(500)
                    gameover.play()
                    self.continue_game = True
                    game.death_count += 1
                    game.playing = False
                    
                    
                
                elif not game.player.has_power_up and game.death_count > 3:
                    pygame.time.delay(500)
                    game.playing = False
                    self.continue_game = False
                    
                
                else:
                    quebrando.play()
                    self.obstacles.remove(obstacle)
                
            
        
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles.clear()