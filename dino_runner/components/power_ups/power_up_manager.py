import random
import pygame

from dino_runner.utils.constants import HAMMER_TYPE
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []        
        
    def update(self, game):
        player = game.player
        
        self.generate_power_up(game.score)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()#associando o tempo atual 
                player.has_power_up = True
                #verificando o tipo de power_up
                if isinstance(power_up, Shield):
                    player.type = SHIELD_TYPE
                elif isinstance(power_up, Hammer):
                    player.type = HAMMER_TYPE
                    
                player.power_up_time_up = power_up.start_time + (power_up.duration*1000)
                
                self.power_ups.remove(power_up)
    
    def generate_power_up(self, time_to_show):
        poder = random.randint(0,1)
#2(score % 100 == 0)
        if len(self.power_ups) == 0 and time_to_show == 0:
            if poder == 0:
                self.power_ups.append(Shield())
            elif poder == 1:
                self.power_ups.append(Hammer())
    
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)    
    
    def reset_power_ups(self):
        self.power_ups.clear()