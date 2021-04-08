#on importe pygame et on l'initialise
import pygame
pygame.init()

#on definit les couleurs utilisées(blanc et noir)
NOIR = (0,0,0)
BLANC = (255,255,255)

#on crée la classe de la raquette
class Raquette(pygame.sprite.Sprite):
    #c'est un dérivé de la classe sprite de pygame
    
    def __init__(self, color, largeur, hauteur):
        # on appelle le cnstructeur de la super class
        super().__init__()
        
        # on donne la couleur de la raquette et sa taille
        # on met le fond d'écran en noir
        self.image = pygame.Surface([largeur, hauteur])
        self.image.fill(NOIR)
        self.image.set_colorkey(NOIR)
 
        # on dessinne le rectangle
        pygame.draw.rect(self.image, color, [0, 0, largeur, hauteur])
        
        # on fait iun rectangle image
        self.rect = self.image.get_rect()

#on ouvre une fenetre
taille_de_la_fenetre = (400, 300)
ecran = pygame.display.set_mode(taille_de_la_fenetre)
pygame.display.set_caption("Pong")

# on dit si il faut verifier que l'on quittes
attention_sur_la_fermeture = True
 
# fps
clock = pygame.time.Clock()
 
#boucle principale du programme
while attention_sur_la_fermeture:
    # boucle principale d'évènements
    for event in pygame.event.get(): # l'utilisateur fait quelquechose
        if event.type == pygame.QUIT: # si l'utilisateur a fermé la fenetre
              attention_sur_la_fermeture = False on finit la boucle
 
    # --- logique du jeu
 

 
    # --- design du jeu
    # premièrement on met l'ecran au noir 
    screen.fill(BLACK)
    # --- on dessine le grillage
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
    # --- on dessine ce que l'on a dessiné
    pygame.display.flip()
     
    # --- on limite à 60 images par secondes
    clock.tick(60)
 
#on quittes le programmes sur l'&ction de fermeture
pygame.quit()