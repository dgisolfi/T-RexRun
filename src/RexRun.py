# !/usr/bin/python3
# 2018-12-23

from settings import *
from PlayerClass import Player
from ObstacleClass import Obstacle

player = Player(black, player_width, player_height, 0, 0)
player.draw()

cactus = Obstacle(black, 0, 0, 20, 40)
player.draw()


def detectCollsion(obj, player):
    print(f'objX {obj.X} playerX {player.Xpos}')
    print(f'objY {obj.Y} playerY {player.Ypos}')
    if player.Xpos >= obj.X and player.Xpos <= (obj.X + obj.width):
        if player.Ypos >= obj.Y and player.Ypos <= (obj.Y + obj.height):
            return True



gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT")
            pygame.quit()
            gameRunning = False
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.Ypos == player.player_starty:
                    player.isJumping = True
            elif event.key == pygame.K_DOWN:
                if not player.isDucking:
                    player.isJumping = True
        
    if detectCollsion(cactus, player):
        gameRunning = False

    screen.fill(white)
    pygame.draw.line(
        screen, 
        black, 
        (0, (game_height/2 + player_height)), 
        (game_width, 
        (game_height/2 + player_height))
    )
    player.update()
    cactus.update()
    pygame.display.update()
    clock.tick(60)
