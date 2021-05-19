import pygame as pygame
import sys
import const
import time

from pygame.constants import K_DOWN, K_UP, K_z, K_s


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

keys = pygame.key.get_pressed()


#------------------------------------------------------------------------------------------------------


#player class
class Player:
    def __init__(self, x, y, key_to_go_up, key_to_go_down):
        self.x = x
        self.y = y
        self.key_to_go_up = key_to_go_up
        self.key_to_go_down = key_to_go_down
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
        if (self.speed < 0 and self.y != 0) or (self.speed > 0 and self.y != 400):

            self.show(const.BLACK)
        
            self.y += self.speed

            self.show(const.WHITE)

    def getting_speed_from_keys(self):
            if keys[self.key_to_go_up] == 1:
                self.speed = -4

            elif keys[self.key_to_go_down] == 1:
                self.speed = 4
            
            else:
                self.speed = 0
            

#------------------------------------------------------------------------------------------------------

  
#init players
#player 1
Player_1 = Player(80, 200, K_z, K_s)
 
#player 2
Player_2 = Player(620, 200, K_UP, K_DOWN)


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

        Player_2.getting_speed_from_keys()

        Player_1.getting_speed_from_keys()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_a_game_running = False
                sys.exit()

         
           

            
        



#------------------------------------------------------------------------------------------------------



pygame.init()


#new game
main_loop()


pygame.quit()