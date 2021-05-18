import pygame as pygame
import sys
import const

from pygame.constants import K_UP

#player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = const.bat_height
        self.width = const.bat_height



    #how we show the bat
    def show(self, color):
        
        pygame.draw.rect(the_game.display, color, (self.x, self.y, const.bat_width, const.bat_height))

    #how the player move
    def move_up(self):
        self.show(const.BLACK)
        self.x += -10
        self.show(const.WHITE)

    def move_down(self):
        self.show(const.BLACK)
        self.x += 1010
        self.show(const.WHITE)


class Game:

    def __init__(self):
        
        #we define here resolution
        self.display = pygame.display.set_mode((700, 500))

        #we put here the caption
        pygame.display.set_caption('Pong Game')

        #we set the game to true
        self.is_the_game_running = True

        #init players
        #player 1
        Player_1 = Player(20, 250)
        Player_1.show(const.WHITE)

        #player 2
        Player_2 = Player(860, 250)
        Player_2.show(const.WHITE)

    def main_loop(self):

        while self.is_the_game_running:
            #test for evnts
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    #for player 2
                    if event.key == pygame.K_UP:
                        self.speed_2_y = -10

                    if event.key == pygame.K_DOWN:
                        self.speed_2_y = 10



            self.display.fill(const.BLACK)
            pygame.display.flip()

if __name__ == '__main__':

    pygame.init()
    the_game = Game

    the_game.main_loop()
    pygame.quit()