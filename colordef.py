__author__ = 'Huy Vu'

import random

# COLOR           R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
RED =           (255,   0,   0)
BLUE =          (  0,   0, 255)
GREEN =         (  0, 255,   0)
YELLOW =        (255, 255,   0)
MAGENTA =       (255,   0, 255)
CYAN =          (  0, 255, 255)
GRAY =          (128, 128, 128)
CARDINAL =      (128,   0,   0)
NAVY =          (  0,   0, 128)
ORANGE =        (255, 165,   0)
PURPLE =        (128,   0, 128)
GOLD =          (255, 215,   0)


MENUBG = ORANGE
#BGCOLOR = random.choice([NAVY,BLACK,CARDINAL,PURPLE])
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BLUE

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE
MENUBUTTONBORDERCOLOR = YELLOW
MENUBUTTONBGCOLOR = WHITE
MENUBUTTONTEXTCOLOR = NAVY

# Classic Mode Time Color
TIME_ALOT = GREEN
TIME_MED = YELLOW
TIME_LOW = RED

def getBackgroundColor():
    return random.choice([NAVY,BLACK,CARDINAL,PURPLE])