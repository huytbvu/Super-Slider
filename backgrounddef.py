import pygame, sys, random
from pygame.locals import *
from random import randint

MENUBGIMG = pygame.image.load('res/menubg.png')
SUBMENUBGIMG = pygame.image.load('res/submenubg.png')
GAMETITLE = pygame.image.load('res/gametitle.png')
BGIMGSIZE = 540
MENUTILESIZE = 90
MENUTILEPART = int(BGIMGSIZE/MENUTILESIZE)
MENUTILEGAP = 5

MENUOFFSETX = 30
MENUOFFSETY = 15

TITLEOFFSETX = 300
TITLEOFFSETY = 50

MENUBUTTONOFFSET = 150

MENUPARTS = []


for i in range(MENUTILEPART):
	col = []
	for j in range(MENUTILEPART):
		col.append((MENUTILESIZE*i,MENUTILESIZE*j))
	MENUPARTS.append(col)
	
