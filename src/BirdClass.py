# !/usr/bin/python3
# 2018-12-23

from settings import *
from ObstacleClass import Obstacle

class Bird(Obstacle):
    def __init__(self, *args, **kwargs):
        Obstacle.__init__(self, *args)
        self.player_starty = kwargs['y_val']
        self.state = 'down'
        self.tick = 0

    
    def update(self, player):
        if self.detectCollsion(player):
            return True
        if self.X < 0:
            self.X = self.player_startx
        else:
            self.X -= self.speed


        if self.state == 'down':
            screen.blit(birdIMG_Up, (self.X, self.Y))
            if self.tick == 8:
                self.state = 'up'
                self.tick = 0 

        elif self.state == 'up':
            screen.blit(birdIMG_Down, (self.X, self.Y))
            if self.tick == 8:
                self.state = 'down'
                self.tick = 0 

        self.tick += 1
        self.draw()
