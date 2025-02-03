from tkinter import CURRENT
import pygame
from config import Config


class Dino:
    def __init__(self, screen):
        self.screen = screen
        self.dino_x = 40
        self.dino_y = 350
        self.show = True
        self.dinoImage  = pygame.image.load("dino.png")
        self.dinoDuck  = pygame.image.load("dinoDuck.png")
       

        
    
    def move(self, x_change, y_change):
        self.dino_x += x_change
        self.dino_y += y_change
        
    
    #def duck(self, x, y):
    #    self.dinoImage = pygame.image.load("dinoDuck.png")
     #   self.dinoImage.center = (x, y)
    
    def normal(self):
        self.dinoImage = pygame.image.load("dino.png")