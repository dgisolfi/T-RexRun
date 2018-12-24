# !/usr/bin/python3
# 2018-12-23

from settings import *

class Obstacle:
    def __init__(self, name, ver, color, x, y, width, height, startx):
        self.color = color
        self.width = width
        self.height = height
        self.player_startx = startx
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

        elif self.name == 'bird':
                screen.blit(birdIMG_Down, (self.X, self.Y))
        
        # pygame.draw.rect(screen, self.color, pygame.Rect([self.X, self.Y, self.width, self.height]))
    
    def update(self, player):
        if self.detectCollsion(player):
            return True
        if self.X < 0:
            self.X = self.player_startx
        else:
            self.X -= self.speed
        self.draw()

    def detectCollsion(self, player):
        # print(f'objX {self.X} playerX {player.Xpos}')
        # print(f'objY {self.Y} playerY {player.Ypos}')
        if player.Xpos >= self.X and player.Xpos <= (self.X + self.width):
            if player.Ypos >= self.Y and player.Ypos <= (self.Y + self.height):
                return True
