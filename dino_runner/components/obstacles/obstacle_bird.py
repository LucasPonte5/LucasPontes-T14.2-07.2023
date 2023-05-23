
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Obstacle_air:
    def __init__(self, image1):
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 100
        


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        self.rect.y -= 2

        if self.rect.x <-self.rect.width:
            obstacles.pop()
    
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

