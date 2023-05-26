import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE, DESENHO, DEFAULT_TYPE

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

musica = pygame.mixer.Sound("dino_runner/assets/Music/Sound.mp3")

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        
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
        if self.death_count == 0:
            self.reset_game()
        elif self.death_count > 0:
            self.continue_game

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
        self.power_up_manager.update(self)
        
    def update_score(self):
        self.score+=1
        
    def update_time(self):
        if self.playing == True:
            self.time += 0.05
        else:
            self.time = 0

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
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        


        pygame.display.flip()


    def display_menu(self):

        if self.death_count == 0:
            self.screen.fill((255, 255, 255))
            x_text_pos = SCREEN_WIDTH//2
            y_text_pos = SCREEN_HEIGHT//2 + 200
            
            
            
            #Start
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Aperte uma tecla pra jogar", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (x_text_pos, y_text_pos)
            

            self.screen.blit(text, text_rect)
            self.screen.blit(DESENHO, (0,0))
            
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

            
            musica.stop()
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
            self.time = 0
            self.run()

        elif self.death_count <= 3 and user_input[pygame.K_c]:
            self.continue_game()
            self.run()
            


        elif user_input[pygame.K_ESCAPE]:
            self.executing = False
            
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000,2)
            
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up Time:{time_to_show}s", True, (255,0,0))
                
                text_rect = text.get_rect()
                text_rect.x = SCREEN_WIDTH//2 - 100
                text_rect.y = SCREEN_HEIGHT//2 - 300
                
                self.screen.blit(text, text_rect)
                
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
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
        
        if self.cloud_x_pos <= -cloud_image_width + 150:
            self.cloud_x_pos = SCREEN_WIDTH + random.randint(0,50)
            self.cloud_y_pos = random.randint(100, 250)
            self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        self.cloud_x_pos -=self.game_speed

    def draw_speed(self):
        
        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render(f"Velocidade(Km/h): {round(self.game_speed)}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (950,100)
        
        self.screen.blit(text, text_rect)

    def draw_time(self):
        
        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render(f"Tempo: {(round(self.time,0))}s", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (80,30)
        
        self.screen.blit(text, text_rect)

    def draw_deathscore(self):

        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render(f"Mortes: {self.death_count}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (80,50)
        
        self.screen.blit(text, text_rect)

    def draw_high_score(self):

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"High score: {self.high_score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (100,550)
        
        self.screen.blit(text, text_rect)


    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.player = Dinosaur()
        musica.play()
        self.score = 0
        self.game_speed = 20    

    def continue_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.player = Dinosaur()
        musica.play()
        self.score = self.score
        self.game_speed = 20   