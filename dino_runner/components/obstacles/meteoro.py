import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Meteoro(Obstacle):
    def __init__(self, image):
        super().__init__(image) #iniciando com uma imagem inicial
        
        self.images = image 
        self.rect.y = 50
            