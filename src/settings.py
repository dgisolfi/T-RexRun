# !/usr/bin/python3
# 2018-12-23

import pygame
import time
import random

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

player_width = 22
player_height = 25

pygame.init()


game_width = 800
game_height = 600


screen = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('T-Rex Run')
clock = pygame.time.Clock()
screen.fill(white)
pygame.draw.line(
            screen, 
            black, 
            (0, (game_height/2 + player_height)), 
            (game_width, 
            (game_height/2 + player_height))
        )
font = pygame.font.Font(None, 36)

playerIMG = pygame.image.load('./imgs/dino.png')
playerIMG_right = pygame.image.load('./imgs/dino_right_foot_up.png')
playerIMG_left = pygame.image.load('./imgs/dino_left_foot_up.png')

cactusIMG_normal = pygame.image.load('./imgs/cactus.png')
cactusIMG_flipped = pygame.image.load('./imgs/cactus_flipped.png')

birdIMG_Down = pygame.image.load('./imgs/bird.png')
birdIMG_Up = pygame.image.load('./imgs/bird_up.png')