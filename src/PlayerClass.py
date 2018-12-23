# !/usr/bin/python3
# 2018-12-23

from settings import *

class Player:

    def __init__(self, color, player_width, player_height, x_speed, y_speed):
        self.color = color
        self.width = player_width
        self.height = player_height
        self.player_startx = (game_width/5)
        self.player_starty = (game_height/2)
        self.Xpos = self.player_startx
        self.Ypos = self.player_starty
        self.jump_height = 60
        self.isJumping = False
        self.isDucking = False
        self.Foot = 'left'
        self.stepCount = 0
        self.score = 0


    def draw(self):
        if self.isDucking == True:
            pass
        else:
            if self.Foot == 'left':
                screen.blit(playerIMG_left, (self.Xpos, self.Ypos))
                if self.stepCount == 5:
                    self.Foot = 'right'
                    self.stepCount = 0 
            elif self.Foot == 'right':
                screen.blit(playerIMG_right, (self.Xpos, self.Ypos))
                if self.stepCount == 5:
                    self.Foot = 'left'
                    self.stepCount = 0 
        self.stepCount += 1

    def update(self):

        if self.isJumping:
            if (self.player_starty - self.Ypos) == self.jump_height:
                self.isJumping = False
            
            if self.Ypos > self.jump_height:
                self.Ypos -= 3

        elif self.Ypos < self.player_starty:
            self.Ypos += 3
        
        self.draw()