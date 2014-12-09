import pygame
from pygame.locals import *

from elements import Glove,Ball
import gamelib
import random

class SaveTheTeamGame(gamelib.SimpleGame):
    
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    

    
    
    def __init__(self):
        super(SaveTheTeamGame, self).__init__('Save!!!',SaveTheTeamGame.BLACK)
        self.glove = Glove((320,500))
        self.random = random
        self.bg = pygame.image.load("bg.png")
        self.balls = []

        for i in range(0,5):
            ball = Ball((i*160,random.randrange(-400,-100,10)))
            self.balls.append(ball)
    
    def init(self):
        super(SaveTheTeamGame, self).init()
        
    def update(self):
        if self.is_key_pressed(K_LEFT):
            self.glove.move_left()
        elif self.is_key_pressed(K_RIGHT):
            self.glove.move_right()
        for ball in self.balls:
            ball.movement()
            if ball.y > 620:
                ball.y = random.randrange(-600,-400,10) 
                    
                    
               
      

    def render(self, surface):
        surface.blit(self.bg,(0,0))
        self.glove.render(surface)
        for ball in self.balls:
            ball.render(surface)

def main():
    game = SaveTheTeamGame()
    game.run()

if __name__ == '__main__':
    main()
    
