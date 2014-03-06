
# source code taken from open source game Slide Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

# modified by Huy Vu

import pygame, sys, random
from gamedef import *

def isValidMove(board, move):
    # check if the current move is valid
    blankx, blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)

def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == BLANK:
                return (x, y)

def getStartingBoard(level):
    tSize = int(IMGSIZE/level)
    IMGPARTS = []
    for i in range(level):
        col = [];
        for j in range(level):
            col.append((tSize*i,tSize*j))
        IMGPARTS.append(col)
    IMGPARTS[level-1][level-1] = BLANK
    return IMGPARTS

def makeMove(board, move):
    # This function does not check if the move is valid.
    blankx, blanky = getBlankPosition(board)
    if move == UP:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]

def resetAnimation(board, allMoves):
    # make all of the moves in allMoves in reverse.
    revAllMoves = allMoves[:]
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        makeMove(board, oppositeMove)

def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY, len(board))
            tileRect = pygame.Rect(left, top, int(IMGSIZE/len(board)), int(IMGSIZE/len(board)))
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)

def getLeftTopOfTile(tileX, tileY, level):
    tileSize = int(IMGSIZE/level)
    left = XMARGIN + (tileX * tileSize) + (tileX - 1)
    top = YMARGIN + (tileY * tileSize) + (tileY - 1)
    return (left, top)

def getRandomMove(board, lastMove=None):
    # start with a full list of all four moves
    validMoves = [UP, DOWN, LEFT, RIGHT]

    # remove moves from the list as they are disqualified
    if lastMove == UP or not isValidMove(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)

    # return a random move from the list of remaining moves
    return random.choice(validMoves)

def formatTime(time):
    mm = int(time/60)
    ss = int(time - mm*60)
    return str(mm).zfill(2)+':'+str(ss).zfill(2)
