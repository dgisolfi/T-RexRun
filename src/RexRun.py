# !/usr/bin/python3
# 2018-12-23

from settings import *
from BirdClass import Bird
from PlayerClass import Player
from ObstacleClass import Obstacle

class RexRun:
    def __init__(self):
        self.isRunning = True
        self.difficulty = 0
        self.FPS = 60
        self.GameOver = False
        # Initialize all Objects
        self.player = Player(black, player_width, player_height, 0, 0)
        self.cactus = Obstacle('cactus', 'normal', black, 0, 0, 11, 27, 800)
        self.cactus_flipped = Obstacle('cactus', 'flipped', black, 0, 0, 11, 27, 1200)
        self.bird_low = Bird('bird', 'normal', black, 0, 0, 20, 14, 1000, y_val=(game_height/1.70))
        self.bird_high = Bird('bird', 'normal', black, 0, 0, 20, 14, 1400, y_val=(game_height/1.69))


    def upDifficulty(self):
        self.cactus.speed += self.difficulty
        self.cactus_flipped.speed += self.difficulty
        self.bird_low.speed += self.difficulty
        self.bird_high.speed += self.difficulty

    def gameOver(self):
        screen.fill(white)
        text = font.render('Game Over', True, black)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

        text = font.render('Press Up or Down Key to Play Again', True, black)
        text_rect = text.get_rect()
        text_x = screen.get_width() /2 - text_rect.width/2
        text_y = screen.get_height() / 1.5 - text_rect.height / 1.5
        screen.blit(text, [text_x, text_y])
        pygame.display.update()
        waiting = True
        while waiting:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("QUIT")
                    pygame.quit()
                    self.isRunning = False
                    quit()

                if event.type == pygame.KEYUP:
                    waiting = False
                    self.__init__()

    def draw(self):
        screen.fill(white)
        pygame.draw.line(
            screen, 
            black, 
            (0, (game_height/2 + player_height)), 
            (game_width, 
            (game_height/2 + player_height))
        )

        # Update Score
        score = font.render(f'Score {self.player.score}', 1, black)
        screen.blit(score, (5, 10))
        self.player.score += (1/2)

        # Update Objects
        self.player.update()
        if self.cactus.update(self.player):
            self.GameOver = True

        if self.cactus_flipped.update(self.player):
            self.GameOver = True

        if self.bird_low.update(self.player):
            self.GameOver = True
        
        if self.bird_high.update(self.player):
            self.GameOver = True

        if self.player.score % 500 == 0:
            print(self.player.score)
            self.upDifficulty()
            self.difficulty += 1
        # Update Display
        pygame.display.update()
        clock.tick(self.FPS)

    def main(self):
        while self.isRunning:
            if self.GameOver:
                self.gameOver()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("QUIT")
                    pygame.quit()
                    self.isRunning = False
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.player.Ypos == self.player.player_starty:
                            self.player.isJumping = True
                    elif event.key == pygame.K_DOWN:
                        if not self.player.isDucking:
                            # self.player.isJumping = True
                            pass
                
            self.draw()

if __name__ == "__main__":
    game = RexRun()
    game.main()