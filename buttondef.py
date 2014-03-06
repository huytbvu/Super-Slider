import pygame, sys, random
from gamedef import *
from backgrounddef import *
from colordef import *

# dictionary of buttons and info panels
BUTTONS = {}
INFOPANELS = {}
MENUBUTTONS = {}	    # main menu buttons
SUBBUTTONS = {}		    # sub menu buttons
MODEBUTTONS = {}	    # mode menu buttons
INGAMEBUTTONS = {}	    # in-game logistics
ARCADEWINBUTTONS = {}   # win screen buttons
CLASSICWINBUTTONS = {}  # win screen buttons

FONTSIZE = 15


def setupButtonText():
    global FONT
    FONT = pygame.font.Font('freesansbold.ttf', FONTSIZE*2)
    MENUBUTTONS['newgame'] = makeMenuText('New Game',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 3*MB_GAP)
    MENUBUTTONS['hiscore'] = makeMenuText('Hall of Fame',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 2*MB_GAP)
    MENUBUTTONS['quit'] = makeMenuText('Quit',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 1*MB_GAP)

    SUBBUTTONS['arcade'] = makeMenuText('Arcade',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 4*MB_GAP)
    SUBBUTTONS['classic'] = makeMenuText('Classic',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 3*MB_GAP)
    SUBBUTTONS['freestyle'] = makeMenuText('Freestyle',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 2*MB_GAP)
    SUBBUTTONS['back'] = makeMenuText('Back',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 1*MB_GAP)

    MODEBUTTONS['baby'] = makeMenuText('Baby Slider',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 5*MB_GAP)
    MODEBUTTONS['regular'] = makeMenuText('Regular Slider',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 4*MB_GAP)
    MODEBUTTONS['premier'] = makeMenuText('Premier Slider',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 3*MB_GAP)
    MODEBUTTONS['extreme'] = makeMenuText('Extreme Slider',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 2*MB_GAP)
    MODEBUTTONS['back'] = makeMenuText('Back',FONT,MENUBUTTONTEXTCOLOR, WINDOWWIDTH-MENUBUTTONOFFSET, WINDOWHEIGHT - 1*MB_GAP)
    

    FONT = pygame.font.Font('freesansbold.ttf', FONTSIZE+5)
    BUTTONS['easy'] = makeButtonText('Baby Slider',9,True)
    BUTTONS['medium']=makeButtonText('Regular Slider',8,True)
    BUTTONS['hard'] = makeButtonText('Premier Slider',7,True)
    BUTTONS['extreme'] = makeButtonText('Extreme Slider',6,True)
    BUTTONS['reset'] = makeButtonText('Reset',4,True)
    BUTTONS['newgame'] = makeButtonText('New Puzzle',3,True)


    INGAMEBUTTONS['quit'] = makeButtonText('Quit',1,True)
    INGAMEBUTTONS['solve'] = makeButtonText('Solve',2,True)

    ARCADEWINBUTTONS['replay'] = makeButtonText('Replay Game',2,True)
    ARCADEWINBUTTONS['backtomenu'] = makeButtonText('Back to Menu',1,True)

    CLASSICWINBUTTONS['chooselevel'] = makeButtonText('Choose Level',4,True)
    CLASSICWINBUTTONS['choosepic'] = makeButtonText('New Puzzle',3,True)
    CLASSICWINBUTTONS['replay'] = makeButtonText('Replay Puzzle',2,True)
    CLASSICWINBUTTONS['backtomenu'] = makeButtonText('Back to Menu',1,True)


def makeButtonText(text,gapmultiplier,drawTopLeft = False):
    return makeMenuText(text,FONT,TEXTCOLOR, WINDOWWIDTH - INGAMEBUTTONOFFSET, WINDOWHEIGHT - gapmultiplier*INGAMEBUTTONGAP,drawTopLeft)

def makeMenuText(text, font, color, x, y, drawTopLeft = False):
    # create the Surface and Rect objects for some text.
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    if drawTopLeft is True:
        textRect.left = x
        textRect.top = y
    else:
        textRect.centerx = x
        textRect.centery = y
    return (textSurf, textRect)
