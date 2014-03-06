import pygame, sys, random
from random import randint

# size of the image
IMGSIZE = 480

# window size
WINDOWWIDTH = 900
WINDOWHEIGHT = 600

# frames per second
FPS = 30

# blank tile
BLANK = None

# surface and rectangle of button entities
SURF_PROP = 0
RECT_PROP = 1

# game state
MENU_STATE = 'menu'
SUB_STATE = 'submenu'
MODE_STATE = 'gamemode'
PLAY_STATE = 'play'
WIN_STATE = 'win'
LOSE_STATE = 'lose'
HISCORE_STATE = 'hiscore'

# game level
BABY_SLIDER = 3
REGULAR_SLIDER = 4
PREMIER_SLIDER = 5
EXTREME_SLIDER = 6

# menu buttons dimension
MB_WIDTH = 300
MB_HEIGHT = 60
MB_GAP = 50
MB_VERT_OFFSET = 50

INGAMEBUTTONOFFSET = 180
INGAMEBUTTONGAP = 30

# game mode
CLASSIC = 'Classic Mode'
ARCADE = 'Arcade Mode'
FREESTYLE = 'Free Play Mode'

# number of input files
NUMOFFILES = 10

# size of puzzle in terms of tiles per side
LEVELMODE = 3

# size of each tile
TILESIZE = int(IMGSIZE/LEVELMODE)

# margin to draw on screen
XMARGIN = int((WINDOWWIDTH - (TILESIZE * LEVELMODE + (LEVELMODE - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * LEVELMODE + (LEVELMODE - 1))) / 2)

# motion direction
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Level image
BABYPANEL = pygame.image.load('res/panel3.png')
REGULARPANEL = pygame.image.load('res/panel4.png')
PREMIERPANEL = pygame.image.load('res/panel5.png')
EXTREMEPANEL = pygame.image.load('res/panel6.png')

PANELOFFSETX = 0
PANELOFFSETY = YMARGIN

# Classic Mode Time Allocation
BABY_TIME = 120
REGULAR_TIME = 180
PREMIER_TIME = 240
EXTREME_TIME = 300


# Game mode image
ARCADEPANEL = pygame.image.load('res/panelarcade.png')
CLASSICPANEL = pygame.image.load('res/panelclassic.png')
FREESTYLEPANEL = pygame.image.load('res/panelfreestyle.png')

# Game end image
GAMEWINIMG = pygame.image.load('res/gamewin.png')
GAMELOSEIMG = pygame.image.load('res/gamelose.png')

# collections of image parts
IMGPARTS = []

curImgID = randint(1,NUMOFFILES)
IMG = pygame.image.load('res/pic'+str(curImgID)+'.png')

def nextImage():
    return pygame.image.load('res/pic'+str(randint(1,NUMOFFILES))+'.png')
