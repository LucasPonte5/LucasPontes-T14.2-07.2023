import random
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
x = random.randint(0,1)

class Obstacle_air:
    def __init__(self, image1):
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        if x == 0:
            self.rect.y = 200
        elif x == 1:
            self.rect.y = 100
        


    def update(self, game_speed, obstacles):
        x = random.randint(0,10)
        self.rect.x -= game_speed
        if x == 0 or x == 9:
            self.rect.y -= 15
        elif x == 1 or x == 10:
            self.rect.y += 15
        elif x != (1 or 2 or 9 or 10):
            pass

        if self.rect.x <-self.rect.width:
            obstacles.pop()
    
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

