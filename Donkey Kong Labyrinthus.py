
"""
écran d'accueil -> choix niveau.
lancement du jeu (possibilité de revenir à l'écran d'accueil)
labyrinthe terminé -> écran d'accueil

Les fonctionnalités du programme
choix du niveau par touche
La structure du niveau (départ, emplacement des murs, arrivée) -> fichier n1, n2...
dk -> touches directionnelles du clavier.
fenêtre -> 15 sprites de côté
à tout moment -> revenir au menu principal
labyrinthe terminé lorsque bananes trouvées
"""

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""
import pygame
from os.path import exists

from classes import *
from constantes import *

pygame.init()
window = pygame.display.set_mode((WIDTH_WINDOW, WIDTH_WINDOW))
pygame.display.set_caption(TITLE_WINDOW)
background = pygame.image.load(BG_LEVEL).convert()

# icone = pygame.image.load(image_icone)
# pygame.display.set_icon(icone)

######################################################################

def open_level(number):
    file = "levels/level %s.txt" % number
    if exists(file):
        window.blit(background, (0,0))
        
        level = Level.openFile(file)
        level.display(window)
        perso = Donkey(DK_UP, DK_DOWN, DK_LEFT, DK_RIGHT, level)
        window.blit(perso.direction, (0, 0))
        
        pygame.display.flip()

        return perso
    else:
        raise FileNotFoundError

def menu():
    background = pygame.image.load(HOME_SCREEN).convert()
    window.blit(background, (0,0))
    pygame.display.flip()

######################################################################

menu()
while playing:
    while state_of_game == "menu":
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in LIST_OF_F_KEYS:
                    number_of_level = LIST_OF_F_KEYS.index(event.key) + 1
                    try:
                        donkey = open_level(number_of_level)
                    except FileNotFoundError:
                        pass
                    else:
                        state_of_game = "playing"
                
                if event.key == K_ESCAPE:
                    playing = False
                    state_of_game = "quit"

        pygame.time.Clock().tick(30)

    while state_of_game == "playing":

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu()
                    state_of_game = "menu"

                if event.key == K_UP:
                    window.blit(background, (0,0))
                    win = donkey.move('up', window)
                if event.key == K_DOWN:
                    window.blit(background, (0,0))
                    win = donkey.move('down', window)
                if event.key == K_LEFT:
                    window.blit(background, (0,0))
                    win = donkey.move('left', window)
                if event.key == K_RIGHT:
                    window.blit(background, (0,0))
                    win = donkey.move('right', window)

                if win is True:
                    menu()
                    state_of_game = "menu"

                pygame.display.flip()
        
        pygame.time.Clock().tick(30)