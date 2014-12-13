import pygame
import random
from pygame.locals import *

class Glove(object):

    def __init__(self, pos):
        (self.x, self.y) = pos
        
        self.image = pygame.image.load("glove.png")

    def getX(self):
        return int(self.x)

    def getY(self):
        return int(self.y)

    def move_left(self):
        self.x -= 10
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += 10
        if self.x > 750:
            self.x = 750
   
    
    def render(self, surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.image,pos)

class Ball(object):
    

    def __init__(self, pos):
        (self.x, self.y) = pos
        self.random = random
        self.image = pygame.image.load("ball.png")

    def movement(self):
        self.y += random.randrange(3,5,1)


    def render(self, surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.image,pos)
        

