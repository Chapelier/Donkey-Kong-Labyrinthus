
from pygame.locals import *

# images
DK_UP = r"sprites\up.png"
DK_DOWN = r"sprites\down.png"
DK_LEFT = r"sprites\left.png"
DK_RIGHT = r"sprites\right.png"
HOME_SCREEN = r"sprites\accueil.png"
BG_LEVEL = r"sprites\background.jpg"
WALL = r"sprites\wall.png"
START = r"sprites\start.png"
BANANA = r"sprites\banana.png"

# window
TITLE_WINDOW = "Donkey Kong Labyrinthus"
SPRITES_PER_LINES = 15
WIDTH_SPRITES = 30
WIDTH_WINDOW = SPRITES_PER_LINES * WIDTH_SPRITES

# game
state_of_game = "menu" # should be "menu", "playing" or "quit"
playing = True

# events
LIST_OF_F_KEYS = [K_F1, K_F2, K_F3, K_F4, K_F5, K_F6, 
                K_F7, K_F8, K_F9, K_F10, K_F11, K_F12]