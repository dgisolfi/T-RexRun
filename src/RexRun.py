# !/usr/bin/python3
# 2018-12-23

from settings import *
from PlayerClass import Player
from ObstacleClass import Obstacle

# Initialize all Objects
player = Player(black, player_width, player_height, 0, 0)
cactus = Obstacle('cactus', 'normal', black, 0, 0, 11, 27)
cactus_flipped = Obstacle('cactus', 'flipped', black, 0, 0, 11, 27)
cactus.X -= 200




def gameOver():
    gameRunning = False

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
        gameOver()
    elif detectCollsion(cactus_flipped, player):
        gameOver()

    screen.fill(white)
    pygame.draw.line(
        screen, 
        black, 
        (0, (game_height/2 + player_height)), 
        (game_width, 
        (game_height/2 + player_height))
    )

    # Update Score
    score = game_font.render('Score {0}'.format(player.score), 1, black)
    screen.blit(score, (5, 10))
    player.score += 1

    # Update Objects
    player.update()
    cactus.update()
    cactus_flipped.update()
    # Update Display
    pygame.display.update()
    clock.tick(60)
