
"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, sprites, levels
"""
import pygame
from os.path import exists

from classes import *
from constantes import *

# initialize window
pygame.init()
window = pygame.display.set_mode((WIDTH_WINDOW, WIDTH_WINDOW))
pygame.display.set_caption(TITLE_WINDOW)
background = pygame.image.load(BG_LEVEL).convert()
icone = pygame.image.load(DK_DOWN)
pygame.display.set_icon(icone)

# initialize sounds
WIN_SOUND = pygame.mixer.Sound(WIN_SOUND_FILE)
LEVEL_SOUND = pygame.mixer.Sound(LEVEL_SOUND_FILE)

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
                        LEVEL_SOUND.play()
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
                
                pygame.display.flip()

                if win is True:
                    WIN_SOUND.play()

                    # waiting for menu
                    not_escape_pressed = True
                    while not_escape_pressed:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN \
                                    and event.key == K_ESCAPE:
                                not_escape_pressed = False

                    pygame.mixer.fadeout(300)
                    menu()
                    state_of_game = "menu"

        pygame.time.Clock().tick(30)