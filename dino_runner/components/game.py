import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE, DINODEAD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        
        self.executing = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.high_score = 0
        self.death_count = 0
        self.time = 0

        self.cloud_y_pos = random.randint(100, 250)
        self.cloud_x_pos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        
    def execute(self):
        self.executing = True
        while self.executing:
            if self.playing == False:
                self.display_menu()
            
        
        pygame.quit()    
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.display_menu()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.update_speed()
        self.update_time()
        self.obstacle_manager.update(self)
        
    def update_score(self):
        self.score+=1
        

    def update_time(self):
        self.time += 0.1

    def update_speed(self):
        if self.score % 100 == 0:
            self.game_speed += 5    

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_simple_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_high_score()
        self.draw_speed()
        self.draw_time()
        self.draw_deathscore()

        pygame.display.flip()


    def display_menu(self):

        if self.death_count == 0:
            self.screen.fill((255, 255, 255))
            x_text_pos = SCREEN_WIDTH//2
            y_text_pos = SCREEN_HEIGHT//2
            
            image_width = DINODEAD.get_width()
            
            #Start
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Aperte uma tecla pra jogar", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (x_text_pos, y_text_pos)
            

            self.screen.blit(text, text_rect)
            self.screen.blit(DINODEAD, (SCREEN_WIDTH//2 - image_width + 40, SCREEN_HEIGHT//2 - 120))
            
            self.menu_events_handler()
            pygame.display.flip()
        
        else:
                
            self.screen.fill((255, 255, 255))
            x_text_pos = 300
            y_text_pos = 400
            x_text_pos1 = 800
            y_text_pos1 = 400
            x_text_pos2 = SCREEN_WIDTH//2 + 100
            y_text_pos2 = SCREEN_HEIGHT//2
            x_text_pos3 = SCREEN_WIDTH//2 - 50
            y_text_pos3 = SCREEN_HEIGHT//2 - 200

            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Aperte C para Continuar", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (x_text_pos, y_text_pos)

            font = pygame.font.Font(FONT_STYLE, 22)
            text1 = font.render("Aperte R para Resetar", True, (0,0,0))
            text_rect1 = text.get_rect()
            text_rect1.center = (x_text_pos1, y_text_pos1)


            font = pygame.font.Font(FONT_STYLE, 22)
            text2 = font.render(f"Mortes: {self.death_count}", True, (0,0,0))
            text_rect2 = text.get_rect()
            text_rect2.center = (x_text_pos2, y_text_pos2)

            font = pygame.font.Font(FONT_STYLE, 22)
            text3 = font.render("Você pode continuar até morrer 3 vezes!", True, (0,0,0))
            text_rect3 = text.get_rect()
            text_rect3.center = (x_text_pos3, y_text_pos3)

            self.screen.blit(text, text_rect)
            self.screen.blit(text1, text_rect1)
            self.screen.blit(text2, text_rect2)
            self.screen.blit(text3, text_rect3)

            self.menu_events_handler()
            pygame.display.flip()

        if self.score >= self.high_score:
            self.high_score = self.score

    def menu_events_handler(self):

        user_input = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif self.death_count == 0 and event.type == pygame.KEYDOWN:
                self.run()
        if user_input[pygame.K_r]:
            self.score = 0
            self.death_count = 0
            self.high_score = 0
            self.run()

        elif self.death_count <= 3 and user_input[pygame.K_c]:
            self.run()
            

            

    
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        
        self.screen.blit(text, text_rect)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_simple_cloud(self):
        cloud_image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        if self.cloud_x_pos <= -cloud_image_width:
            self.cloud_x_pos = SCREEN_WIDTH + random.randint(0,50)
            self.cloud_y_pos = random.randint(100, 250)
            self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        self.cloud_x_pos -=self.game_speed

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20


    def draw_speed(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Velocidade(Km/h): {round(self.game_speed)}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (900,100)
        
        self.screen.blit(text, text_rect)

    def draw_time(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Tempo: {round(self.time)}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (100,50)
        
        self.screen.blit(text, text_rect)

    def draw_deathscore(self):

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Mortes: {self.death_count}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (100,100)
        
        self.screen.blit(text, text_rect)

    def draw_high_score(self):

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"High score: {self.high_score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (100,150)
        
        self.screen.blit(text, text_rect)

        