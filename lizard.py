import pygame
import random
from config import Config




class Lizard:
    def __init__(self, screen):
        self.screen = screen
        self.lizard_x = 700
        self.lizard_y = 450
        self.lizardImage  = pygame.image.load("lizard.png")
        self.bird_x = 1100
        self.bird_y = 200        
        self.birdImage  = pygame.image.load("bird.png")        

    def moveLizard(self, x_change, y_change):
        self.lizard_x += x_change
        self.lizard_y += y_change

    def moveBird(self, x_change, y_change):
        self.bird_x += x_change
        self.bird_y += y_change      
          
    
    def draw_apple(self):
        return pygame.draw.rect(self.screen, Config["colors"]["apple-red"], (self.apple_x, self.apple_y,Config["apple"]["width"], Config["apple"]["height"]))
