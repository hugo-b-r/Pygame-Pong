import pygame as pygame
import sys
import const
import time

from pygame.constants import K_UP

#INITIALIZATION OF THE SCREEN

#we define here resolution
DISPLAY = pygame.display.set_mode((720, 480))

#we put here the caption
pygame.display.set_caption('Pong Game')

is_a_game_running = True

#the display
DISPLAY.fill(const.BLACK)
pygame.display.flip()

#player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = const.bat_height
        self.width = const.bat_height



    #how we show the bat
    def show(self, color,):
        
        pygame.draw.rect(DISPLAY, color, (self.x, self.y, const.bat_width, const.bat_height))

        pygame.display.update()

    #how the player move
    def move_up(self):
        self.show(const.BLACK)
        self.y += -20
        self.show(const.WHITE)

    def move_down(self):
        self.show(const.BLACK)
        self.y += 20
        self.show(const.WHITE)

  
#init players
#player 1
Player_1 = Player(40, 240)
 
#player 2
Player_2 = Player(660, 240)


def show_players():
    Player_1.show(const.WHITE)
    Player_2.show(const.WHITE)



def main_loop():
    show_players()
    is_a_game_running = True
    while is_a_game_running:
            #test for events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_a_game_running = False
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #for player 2
                if event.key == pygame.K_UP:
                    Player_2.move_up()
                    

                if event.key == pygame.K_DOWN:
                    Player_2.move_down()


pygame.init()


#new game
main_loop()


pygame.quit()