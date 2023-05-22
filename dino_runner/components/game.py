import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud1 = 1000
        self.y_pos_cloud1 = 100
        self.x_pos_cloud2 = 670
        self.y_pos_cloud2 = 50
        self.x_pos_cloud3 = 100
        self.y_pos_cloud3 = 100

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        self.screen.blit(CLOUD, (self.x_pos_cloud1,self.y_pos_cloud1))
        self.screen.blit(CLOUD, (self.x_pos_cloud2,self.y_pos_cloud2))
        self.screen.blit(CLOUD, (self.x_pos_cloud3,self.y_pos_cloud3))
        self.x_pos_cloud1 -= self.game_speed
        self.x_pos_cloud2 -= self.game_speed
        self.x_pos_cloud3 -= self.game_speed
        if self.x_pos_cloud1 <= -50:
            self.x_pos_cloud1 = 1300
        if self.x_pos_cloud2 <= -50:
            self.x_pos_cloud2 = 1300
        if self.x_pos_cloud3 <= -50:
            self.x_pos_cloud3 = 1300
        
    