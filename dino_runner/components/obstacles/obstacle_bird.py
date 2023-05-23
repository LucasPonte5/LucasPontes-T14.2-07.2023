
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Obstacle_air:
    def __init__(self, image1):
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 100
        if self.rect.y == 94:
            self.rect.y +=2
        elif self.rect.y == 100:
            self.rect.y -= 2


        

        


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        self.rect.y -= 2
        if self.rect.y <-self.rect.height:
            self.rect.y -= 2
        else:
            self.rect.y += 2
        if self.rect.x <-self.rect.width:
            obstacles.pop()
    
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def movimento(self):
        if self.rect.y <= 94:
            self.rect.y = Y_POS + 5
        elif self.rect.y >= 104:
            self.rect.y = Y_POS - 5
