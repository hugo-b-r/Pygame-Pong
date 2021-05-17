import pygame as pyg
import sys

class Game:

    def __init__(self):
        
        #we define here resolution
        self.display = pyg.display.set_mode((700, 500))

        #we put here the caption
        pyg.display.set_caption('Pong Game')

        #we set the game to true
        self.is_the_game_running = True

    def main_loop(self):

        while self.is_the_game_running:
            #test for evnts
            for event in pyg.event.get():

                if event.type == pyg.QUIT:

                    sys.exit()

            self.display.fill((200, 200, 200))
            pyg.display.flip()

if __name__ == '__main__':

    pyg.init()
    Game().main_loop()
    pyg.quit()