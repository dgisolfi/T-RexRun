# !/usr/bin/python3
# 2018-12-23

from settings import *

class Obstacle:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.player_startx = 780
        self.player_starty = (game_height/2)
        self.X = self.player_startx
        self.Y = (game_height/2)
        self.speed = 3
    
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect([self.X, self.Y, self.width, self.height]))
    
    def update(self):
        if self.X < 0:
            self.X = self.player_startx
        else:
            self.X -= self.speed

        self.draw()
