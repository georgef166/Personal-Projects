from inspect import BoundArguments
from shutil import move
from turtle import Screen, width
from xmlrpc.client import FastParser
import pygame
from config import Config
from lizard import Lizard
from dino import Dino

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
INDIGO = (75,0,130)



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Config["game"]["caption"])
        print(Config["game"]["width"], Config["game"]["height"])
        self.screen = pygame.display.set_mode((Config["game"]["width"] , Config["game"]["height"]))
        self.dino = Dino(self.screen)
        self.lizard = Lizard(self.screen)
        self.font = pygame.font.Font('./Roboto-Regular.ttf',80)
        self.loseFont = pygame.font.Font('./Roboto-Regular.ttf',80)
        self.finalFont = pygame.font.Font('./Roboto-Regular.ttf',20)               
        self.score = 0
        self.text = self.finalFont.render("Score = " + str(self.score), True, BLACK)
        self.lose = self.loseFont.render("" , True, RED)
        self.finalScore = self.finalFont.render("", True, RED)
        self.fpsClock = pygame.time.Clock()
        self.fps = Config["game"]["fps"]
        self.oof = False
        self.background = pygame.image.load("background.png")
        self.scoreFile = open("score.txt", "w")     


        

    def loop(self):
        quitVar = True
        x_change = 0
        y_change = 0

        while quitVar == True:
            self.screen.blit(self.background, (0,0))



            self.dino_rect = self.screen.blit(self.dino.dinoImage, (self.dino.dino_x, self.dino.dino_y))                
            self.lizard_rect = self.screen.blit(self.lizard.lizardImage, (self.lizard.lizard_x, self.lizard.lizard_y))
            self.bird_rect = self.screen.blit(self.lizard.birdImage, (self.lizard.bird_x, self.lizard.bird_y))


            if self.dino.show != True:
               self.screen.fill(Config["colors"]["white"])
                                       
            if self.dino_rect.colliderect(self.lizard_rect) or self.dino_rect.colliderect(self.bird_rect):   
                self.lose = self.font.render("YOU LOSE", True, RED)
                self.lizard.lizard_y =  800
                self.lizard.bird_y =  1000
                self.oof = True
                self.userName = input("What is your name?") 
                self.scoreFile.write("Name: " + str(self.userName) + "\nScore " + str(self.score))

            if self.dino_rect[0] == self.lizard_rect[0] and self.oof == False:
                self.score += 1   
                self.text = self.finalFont.render("Score = " + str(self.score), True, BLACK)
                
                # + str(self.score), True, BLACK)36-


            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    quitVar = False
    
                if event.type == pygame.KEYDOWN and self.dino.show == True:                  

                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE and self.dino.dino_y == 350:
                        print("Key Pressed: UP")                      
                        x_change = 0
                        y_change = -1

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s and self.dino.dino_y == 350:
                        print("Key Pressed: Down")                      
                        self.dino.dino_y = 350
                        y_change = 0
                 
                  # if event.key != pygame.K_DOWN or event.key != pygame.K_s:
                   #     print("Key Pressed: Nothing")                      
                        
                    '''if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        print("Key Pressed: DOWN")
                        x_change = 0
                        y_change = 1
                    '''

            print((self.lizard.lizard_x, self.lizard.lizard_y))
            self.screen.blit(self.text, self.text.get_rect(center = (400,550)))
            self.screen.blit(self.lose, self.lose.get_rect(center = (400,300)))
            self.screen.blit(self.finalScore, self.finalScore.get_rect(center = (400,360)))
            self.screen.blit(self.dino.dinoImage, (self.dino.dino_x, self.dino.dino_y))
            print((self.dino.dino_x, self.dino.dino_y), y_change)
            self.screen.blit(self.lizard.lizardImage, (self.lizard.lizard_x, self.lizard.lizard_y))
            self.screen.blit(self.lizard.birdImage, (self.lizard.bird_x, self.lizard.bird_y))            
            self.dino.move(x_change * Config["dino"]["jump"], y_change * Config["dino"]["jump"])
            self.lizard.moveLizard(-20 * 1, 0 * 1)
            self.lizard.moveBird(-20 * 0.5, 0 * 0.5)

            if self.dino.dino_y <= 200:
                y_change = 0.4
            elif self.dino.dino_y == 350:
                y_change = 0
            

            if self.lizard.lizard_x <= -200:
                self.lizard.lizard_x = 700

            if self.lizard.bird_x <= -200:
                self.lizard.bird_x = 1200


            self.screen.blit(self.text, self.text.get_rect(center = (400,550)))
            self.screen.blit(self.lose, self.lose.get_rect(center = (400,300)))
            self.fpsClock.tick(self.fps)
            self.dino.normal()


            pygame.display.update()
        self.scoreFile.close()
        
        pygame.quit()
