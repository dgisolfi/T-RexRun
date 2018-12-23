# !/usr/bin/python3
# 2018-12-23

from settings import *

class Obstacle:
    def __init__(self, name, ver, color, x, y, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.player_startx = 1000
        self.player_starty = (game_height/2)
        self.X = self.player_startx
        self.Y = (game_height/2)
        self.speed = 3
        self.name = name
        self.ver = ver
    
    def draw(self):
        if self.name == 'cactus':
            if self.ver == 'normal':
                screen.blit(cactusIMG_normal, (self.X, self.Y))

            elif self.ver == 'flipped':
                 screen.blit(cactusIMG_flipped, (self.X, self.Y))
        #  pygame.draw.rect(screen, self.color, pygame.Rect([self.X, self.Y, self.width, self.height]))
    
    def update(self, player):
        if self.X < 0:
            self.X = self.player_startx
        else:
            self.X -= self.speed

        self.draw()

    def detectCollsion(self, obj, player):
        print(f'objX {obj.X} playerX {player.Xpos}')
        print(f'objY {obj.Y} playerY {player.Ypos}')
        if player.Xpos >= obj.X and player.Xpos <= (obj.X + obj.width):
            if player.Ypos >= obj.Y and player.Ypos <= (obj.Y + obj.height):
                return True
