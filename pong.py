#on importe pygame et on l'initialise
import pygame
pygame.init()

#on definit les couleurs utilisées(blanc et noir)
NOIR = (0,0,0)
BLANC = (255,255,255)

#on ouvre une fenetre
taille_de_la_fenetre = (400, 300)
ecran = pygame.display.set_mode(taille_de_la_fenetre)
pygame.display.set_caption("Pong")