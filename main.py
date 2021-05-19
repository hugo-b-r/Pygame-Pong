import pygame as pygame
import sys
import const
import time

from pygame.constants import K_DOWN, K_UP


#------------------------------------------------------------------------------------------------------
#INITIALIZATION OF THE SCREEN

#we define here resolution
DISPLAY = pygame.display.set_mode((720, 480))

#we put here the caption
pygame.display.set_caption('Pong Game')

is_a_game_running = True
clock = pygame.time.Clock()
#the display
DISPLAY.fill(const.BLACK)
pygame.display.flip()



#------------------------------------------------------------------------------------------------------


#player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.height = const.bat_height
        self.width = const.bat_height



    #how we show the bat
    def show(self, color):
        
        pygame.draw.rect(DISPLAY, color, (self.x, self.y, const.bat_width, const.bat_height))

        pygame.display.update()

    #how the player move
    def move(self):
        print(self.y)
        if self.speed < 0:
            if (self.y != 0):

                self.show(const.BLACK)
        
                self.y += self.speed

                self.show(const.WHITE)
        else:
            self.show(const.BLACK)
        
            self.y += self.speed

            self.show(const.WHITE)

#------------------------------------------------------------------------------------------------------

  
#init players
#player 1
Player_1 = Player(40, 200)
 
#player 2
Player_2 = Player(660, 200)


def show_players():
    Player_1.show(const.WHITE)
    Player_2.show(const.WHITE)



#------------------------------------------------------------------------------------------------------


def main_loop():
    show_players()
    is_a_game_running = True
    while is_a_game_running:
        
        time = clock.tick(60)	
        
        if Player_1.speed != 0:
            Player_1.move()
        
        if Player_2.speed != 0:
            Player_2.move()
        
        

        #test for events
        keys = pygame.key.get_pressed()

        if keys[K_UP] == 1:
                Player_2.speed = -5

        elif keys[K_DOWN] == 1:
                Player_2.speed = 5
            
        else:
            Player_2.speed = 0
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_a_game_running = False
                sys.exit()

         
           

            
        



#------------------------------------------------------------------------------------------------------



pygame.init()


#new game
main_loop()


pygame.quit()