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
        self.hp = 5
        self.score = 0
        self.game_over = False

        for i in range(0,5):
            ball = Ball((i*160,random.randrange(-500,-100,100)))
            self.balls.append(ball)
    
    def init(self):
        super(SaveTheTeamGame, self).init()
        self.render_score()
        self.render_hp()
        
    def update(self):
        if not self.game_over: 
            if self.is_key_pressed(K_LEFT):
                self.glove.move_left()
            elif self.is_key_pressed(K_RIGHT):
                self.glove.move_right()
            for ball in self.balls:
                ball.movement()
                if ball.y > 610:
                    ball.y = random.randrange(-600,-400,150)
                    self.hp -= 1
                    self.render_hp() 
                
                if ((ball.y+30 > self.glove.y-30) and (self.glove.y+30 > ball.y-30) and (self.glove.x-40 < ball.x < self.glove.x+40 )):   
                        ball.y = random.randrange(-800,-600,150)
                        self.score += 1
                        self.render_score()        
                    
        if self.hp == 0:
            self.game_over = True
      
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, SaveTheTeamGame.WHITE)
    
    def  render_hp(self):
        self.hp_image = self.font.render("HP = %d" % self.hp, 0, SaveTheTeamGame.WHITE)

    def render(self, surface):
        surface.blit(self.bg,(0,0))
        self.glove.render(surface)
        for ball in self.balls:
            ball.render(surface)
        surface.blit(self.score_image, (10,10))
        surface.blit(self.hp_image, (680,10))

def main():
    game = SaveTheTeamGame()
    game.run()

if __name__ == '__main__':
    main()
    
