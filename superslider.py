# Super Slider
# by Huy Vu
#
# http://github.com/Super-Slider

# GAME MEMO
# created on February 21, 2014
# level design on February 22, 2014
# Arcade Mode established on February 24, 2014
# graphics enhanced on February 25, 2014
# Freestyle Mode added on February 26, 2014
# Timer fixed and Classic Mode added on February 27, 2014
# Win and Lose screen added on February 28, 2014

__author__ = 'Huy Vu'

import pygame, sys, random
from pygame.locals import *
from gamedef import *
from backgrounddef import *
from buttondef import *
from gameutil import *
from colordef import *

def main():
    """
        Main activity of the game, handle all of major game logics
    """

    global FPSCLOCK, SCREEN, FONT, LEVELMODE,IMGSIZE,IMGPARTS, IMG, TILESIZE
    global moveCount, startTime, updateTime, timeElapsed, timeMaxClassic
    global CurState, GameMode, blinking

    GameMode = None
    CurState = MENU_STATE
    justEnter = True
    updateTime = False
    blinking = False

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('SuperSlider by Huy Vu')
    moveCount = 0
    startTime = 0
    timeElapsed = startTime
    timeMaxClassic = 0
    FONT = pygame.font.Font('freesansbold.ttf', FONTSIZE*2)
    #BackToMenuButton = makeMenuText('Back to Menu',FONT,TEXTCOLOR, WINDOWWIDTH - INGAMEBUTTONOFFSET, WINDOWHEIGHT - INGAMEBUTTONGAP,True)
    
    GAMETITLE.convert_alpha()

    # set up an initial game board of the easiest level
    #mainBoard, solutionSeq = generateNewPuzzle(LEVELMODE,False)
    #SOLVEDBOARD = getStartingBoard(LEVELMODE)
    allMoves = []

    setupButtonText()


    ############################
    # BEGIN THE MAIN GAME LOOP #
    ############################
    while True:
        checkForQuit()

        #############################################################
        # MENU STATE                                                #
        #############################################################
        #                                                           #
        # This is the main menu of the game, allow players to play  #
        # new game, check hiscore or quit                           #
        #                                                           #
        #############################################################
        if CurState == MENU_STATE:
            SCREEN.fill(MENUBG)
            
            for event in pygame.event.get():
                # handle each button
                if event.type == MOUSEBUTTONUP:
                    if MENUBUTTONS['newgame'][RECT_PROP].collidepoint(event.pos):
                        CurState = SUB_STATE
                    elif MENUBUTTONS['hiscore'][RECT_PROP].collidepoint(event.pos):
                        CurState = HISCORE_STATE
                    elif MENUBUTTONS['quit'][RECT_PROP].collidepoint(event.pos):
                        terminate()

            drawBackgroundFacility(MENUBGIMG,MENUBUTTONS)


        #############################################################
        # SUBMENU STATE                                             #
        #############################################################
        #                                                           #
        # Show different game play options (Arcade, Classic, and    #
        # Freestyle)                                                #
        #                                                           #
        # Also include a back button to main menu                   #
        #                                                           #
        #############################################################
        elif CurState == SUB_STATE:
            SCREEN.fill(CYAN)
            timeElapsed = 0
            for event in pygame.event.get():
                # handle each button
                if event.type == MOUSEBUTTONUP:
                    if SUBBUTTONS['arcade'][RECT_PROP].collidepoint(event.pos):
                        CurState = PLAY_STATE
                        GameMode = ARCADE
                        LEVELMODE = BABY_SLIDER
                        IMG = nextImage()
                        mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)
                    elif SUBBUTTONS['classic'][RECT_PROP].collidepoint(event.pos):
                        CurState = MODE_STATE
                        GameMode = CLASSIC
                    elif SUBBUTTONS['freestyle'][RECT_PROP].collidepoint(event.pos):
                        CurState = PLAY_STATE
                        GameMode = FREESTYLE
                        LEVELMODE = REGULAR_SLIDER
                        IMG = nextImage()
                        mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)
                    elif SUBBUTTONS['back'][RECT_PROP].collidepoint(event.pos):
                        CurState = MENU_STATE
                        
            drawBackgroundFacility(SUBMENUBGIMG,SUBBUTTONS)
            
        #############################################################
        # MODE STATE                                                #
        #############################################################
        #                                                           #
        # Classic Mode only, allow players to choose game level     #
        #                                                           #
        #############################################################
        elif CurState == MODE_STATE:
            SCREEN.fill(CYAN)
            
            for event in pygame.event.get():
                # handle each button
                if event.type == MOUSEBUTTONUP:
                    CurState = PLAY_STATE
                    if MODEBUTTONS['baby'][RECT_PROP].collidepoint(event.pos):
                        LEVELMODE = BABY_SLIDER
                        timeMaxClassic = BABY_TIME
                    elif MODEBUTTONS['regular'][RECT_PROP].collidepoint(event.pos):
                        LEVELMODE = REGULAR_SLIDER
                        timeMaxClassic = REGULAR_TIME
                    elif MODEBUTTONS['premier'][RECT_PROP].collidepoint(event.pos):
                        LEVELMODE = PREMIER_SLIDER
                        timeMaxClassic = PREMIER_TIME
                    elif MODEBUTTONS['extreme'][RECT_PROP].collidepoint(event.pos):
                        LEVELMODE = EXTREME_SLIDER
                        timeMaxClassic = EXTREME_TIME
                    elif MODEBUTTONS['back'][RECT_PROP].collidepoint(event.pos):
                        CurState = SUB_STATE
                    IMG = nextImage()
                    mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)
                    startTime = pygame.time.get_ticks()
                        
            drawBackgroundFacility(SUBMENUBGIMG,MODEBUTTONS)

        #############################################################
        # LOSE STATE                                                #
        #############################################################
        #                                                           #
        # Classic Mode only, this show the losing screen when time  #
        # runs out before the puzzle is solved                      #
        #                                                           #
        #############################################################
        elif CurState == LOSE_STATE:
            SCREEN.fill(getBackgroundColor())
            justEnter = True
            drawBoard(None,"You have lost")
            loseleft, losetop = getLeftTopOfTile(0, 0, LEVELMODE)
            SCREEN.blit(GAMEWINIMG,(loseleft+2,losetop+2))
            drawButtons(CLASSICWINBUTTONS)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if CLASSICWINBUTTONS['replay'][RECT_PROP].collidepoint(event.pos):
                        timeElapsed = 0
                        CurState = PLAY_STATE
                        mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)
                    elif CLASSICWINBUTTONS['backtomenu'][RECT_PROP].collidepoint(event.pos):
                        CurState = MENU_STATE
                    elif CLASSICWINBUTTONS['chooselevel'][RECT_PROP].collidepoint(event.pos):
                        CurState = MODE_STATE
                    elif CLASSICWINBUTTONS['choosepic'][RECT_PROP].collidepoint(event.pos):
                        CurState = PLAY_STATE
                        IMG = nextImage()
                        mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)

            pygame.display.update()

        #############################################################
        # WIN STATE                                                 #
        #############################################################
        #                                                           #
        # In Arcade Mode , this show the winning screen when player #
        # has successfully achieved the highest level               #
        #                                                           #
        # In Classic Mode , this show the winning screen when player#
        # has successfully solved the puzzle before time runs out   #
        #                                                           #
        #############################################################
        elif CurState == WIN_STATE:
            SCREEN.fill(getBackgroundColor())
            justEnter = True
            drawBoard(None,"You have won")
            winleft, wintop = getLeftTopOfTile(0, 0, LEVELMODE)
            SCREEN.blit(GAMEWINIMG,(winleft+2,wintop+2))
            if GameMode == ARCADE:
                drawButtons(ARCADEWINBUTTONS)
            elif GameMode == CLASSIC:
                drawButtons(CLASSICWINBUTTONS)
            for event in pygame.event.get(): 
                if event.type == MOUSEBUTTONUP:

                    if GameMode == ARCADE:
                        if ARCADEWINBUTTONS['replay'][RECT_PROP].collidepoint(event.pos):
                            CurState = PLAY_STATE
                            IMG = nextImage()
                            mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(BABY_SLIDER)
                        elif ARCADEWINBUTTONS['backtomenu'][RECT_PROP].collidepoint(event.pos):
                            CurState = MENU_STATE

                    if GameMode == CLASSIC:
                        if CLASSICWINBUTTONS['replay'][RECT_PROP].collidepoint(event.pos):
                            timeElapsed = 0
                            CurState = PLAY_STATE
                            mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)
                        elif CLASSICWINBUTTONS['backtomenu'][RECT_PROP].collidepoint(event.pos):
                            CurState = MENU_STATE
                        elif CLASSICWINBUTTONS['chooselevel'][RECT_PROP].collidepoint(event.pos):
                            CurState = MODE_STATE
                        elif CLASSICWINBUTTONS['choosepic'][RECT_PROP].collidepoint(event.pos):
                            CurState = PLAY_STATE
                            IMG = nextImage()
                            mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)

            pygame.display.update()

        #############################################################
        # PLAY STATE                                                #
        #############################################################
        #                                                           #
        # This is where the game is played                          #
        # Screen is drawn depending on Game Mode and Level Mode     #
        #                                                           #
        # Arcade Mode:                                              #
        # Game starts with easiest level. When player completes the #
        # puzzle, the game will move to the next level. The ultimate#
        # goal is to achieve the highest level                      #
        #                                                           #
        # Classic Mode:                                             #
        # A classic time challenge, play chooses a difficulty level #
        # and tries to complete it before time runs out             #
        #                                                           #
        # Freestyle Mode:                                           #
        # A practice mode where player can try to complete any      #
        # level of the same puzzle in fewest time and moves         #
        #                                                           #
        #############################################################
        elif CurState == PLAY_STATE:
            if justEnter:
                if GameMode == ARCADE:
                    LEVELMODE = BABY_SLIDER
                startTime = pygame.time.get_ticks()
                moveCount = 0
                justEnter = False

            if GameMode == FREESTYLE and moveCount >= 1:
                updateTime = True
            elif GameMode == ARCADE or GameMode == CLASSIC:
                updateTime = True
            else:
                updateTime = False

            slideTo = None
            msg = 'Click on tile to move'
            if mainBoard is not None and mainBoard == SOLVEDBOARD:
                msg = 'Solved!'
                updateTime = False
                drawBorderSolved(mainBoard)
                if GameMode == ARCADE:
                    allMoves = []
                    if LEVELMODE == EXTREME_SLIDER:
                        CurState = WIN_STATE
                    else:
                        IMG = nextImage()
                        LEVELMODE += 1
                        mainBoard, solutionSeq, SOLVEDBOARD = moveToLevel(LEVELMODE)
                elif GameMode == CLASSIC:
                        CurState = WIN_STATE
            else:
                drawBoard(mainBoard, msg)

            
            for event in pygame.event.get():
                
                if event.type == MOUSEBUTTONUP:
                    spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])
                    if (spotx, spoty) == (None, None):


                        if INGAMEBUTTONS['quit'][RECT_PROP].collidepoint(event.pos):
                            CurState = SUB_STATE
                            justEnter = True
                            moveCount = 0

                        elif INGAMEBUTTONS['solve'][RECT_PROP].collidepoint(event.pos):
                            resetAnimation(mainBoard, solutionSeq + allMoves)
                            allMoves = []


                        if GameMode == FREESTYLE:
                            if BUTTONS['reset'][RECT_PROP].collidepoint(event.pos):
                                resetAnimation(mainBoard, allMoves)
                                allMoves = []
                            elif BUTTONS['newgame'][RECT_PROP].collidepoint(event.pos):
                                IMG = pygame.image.load('res/pic'+str(randint(1,NUMOFFILES))+'.png')
                                mainBoard, solutionSeq = generateNewPuzzle(LEVELMODE,True)
                                moveCount = 0
                                allMoves = []
                            else:
                                if BUTTONS['easy'][RECT_PROP].collidepoint(event.pos):
                                    LEVELMODE = 3
                                elif BUTTONS['medium'][RECT_PROP].collidepoint(event.pos):
                                    LEVELMODE = 4
                                elif BUTTONS['hard'][RECT_PROP].collidepoint(event.pos):
                                    LEVELMODE = 5
                                elif BUTTONS['extreme'][RECT_PROP].collidepoint(event.pos):
                                    LEVELMODE = 6
                                else:
                                    break

                                TILESIZE = int(IMGSIZE/LEVELMODE)
                                mainBoard, solutionSeq = generateNewPuzzle(LEVELMODE,True)
                                SOLVEDBOARD = getStartingBoard(LEVELMODE) # a solved board is the same as the board in a start state.
                                timeElapsed = 0
                                SCREEN.blit(*makeMenuText('Time: 00:00', FONT, MESSAGECOLOR, WINDOWWIDTH - 200, 60, True))
                                pygame.display.update()
                                moveCount = 0
                                allMoves = []

                    else:
                        # check if the clicked tile was next to the blank spot

                        blankx, blanky = getBlankPosition(mainBoard)

                        if spotx == blankx + 1 and spoty == blanky:
                            slideTo = LEFT
                        elif spotx == blankx - 1 and spoty == blanky:
                            slideTo = RIGHT
                        elif spotx == blankx and spoty == blanky + 1:
                            slideTo = UP
                        elif spotx == blankx and spoty == blanky - 1:
                            slideTo = DOWN
           

            if slideTo:
                moveCount += 1
                if moveCount == 1 and (GameMode == FREESTYLE):
                    startTime = pygame.time.get_ticks()
                slideAnimation(mainBoard, slideTo, 'Click on tile to move', 8)
                makeMove(mainBoard, slideTo)
                allMoves.append(slideTo)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    #
    # END THE MAIN GAME LOOP
    #


def moveToLevel(level):
    """ go to next level in Arcade Game Mode
    @param current game level"""
    global TILESIZE,LEVELMODE,BGCOLOR
    BGCOLOR = getBackgroundColor()
    LEVELMODE = level
    TILESIZE = int(IMGSIZE/LEVELMODE)
    solution = getStartingBoard(LEVELMODE)
    mBoard, solSeq = generateNewPuzzle(LEVELMODE,True)
    return (mBoard, solSeq, solution)

def drawBackgroundFacility(bgimg,buttons):
    # draw the main screen tile
    for i in range(len(MENUPARTS)):
        for j in range(len(MENUPARTS)):
            SCREEN.blit(bgimg,(i*(MENUTILEGAP+MENUTILESIZE)+MENUOFFSETX,j*(MENUTILEGAP+MENUTILESIZE)+MENUOFFSETY),pygame.Rect(MENUPARTS[i][j][0],MENUPARTS[i][j][1],MENUTILESIZE,MENUTILESIZE))

    SCREEN.blit(GAMETITLE,(WINDOWWIDTH - TITLEOFFSETX,TITLEOFFSETY))

    drawButtons(buttons)

    # update screen
    pygame.display.update() 

def drawButtons(buttons):
    for val in buttons.values():
        SCREEN.blit(val[0],val[1])

def drawMenuButton(numButtons):
    for i in range(numButtons):
        pygame.draw.rect(SCREEN, MENUBUTTONBGCOLOR, ((WINDOWWIDTH-MB_WIDTH)/2, (WINDOWHEIGHT-MB_HEIGHT)/2 + i*MB_GAP + MB_VERT_OFFSET, MB_WIDTH, MB_HEIGHT))
        pygame.draw.rect(SCREEN, MENUBUTTONBORDERCOLOR, ((WINDOWWIDTH-MB_WIDTH)/2-4, (WINDOWHEIGHT-MB_HEIGHT)/2-4 + i*MB_GAP + MB_VERT_OFFSET, MB_WIDTH + 8, MB_HEIGHT+8),4)

def terminate():
    pygame.quit()
    sys.exit()

def drawBorderSolved(board):
    """
        Show flashing border when puzzle is solved
    """
    color1 = CYAN
    color2 = YELLOW
    color3 = RED
    left, top = getLeftTopOfTile(0, 0, LEVELMODE)
    width = LEVELMODE * TILESIZE
    height = LEVELMODE * TILESIZE
    for i in range(10):
        color1, color2, color3 = color2, color3, color1
        drawBoard(board,'solve!')
        pygame.draw.rect(SCREEN, color1, (left - 5, top - 5, width + 11, height + 11), 4)
        pygame.display.update()
        pygame.time.wait(200)

def checkForQuit():
    """
        Check if the player quits the game by hitting quit (X) or escape button
    """
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def drawBoard(board, message):
    SCREEN.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeMenuText(message, FONT, MESSAGECOLOR, 5, 5,True)
        SCREEN.blit(textSurf, textRect)

    if board:
        for tilex in range(len(board)):
            for tiley in range(len(board[0])):
                if board[tilex][tiley]:
                    drawTile(tilex, tiley, board[tilex][tiley])

    left, top = getLeftTopOfTile(0, 0, LEVELMODE)
    width = LEVELMODE * TILESIZE
    height = LEVELMODE * TILESIZE

    # draw the border
    pygame.draw.rect(SCREEN, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

    # display all buttons
    if GameMode == FREESTYLE:
        drawButtons(BUTTONS)
    if CurState == PLAY_STATE:
        drawButtons(INGAMEBUTTONS)

    # display information
    displayMoveInfo()
    displayRegularTimeInfo()
    displayLevelIndicatorPanel()
    displayGameModeIndicatorPanel()

def displayMoveInfo():
    SCREEN.blit(*makeMenuText('Move: '+str(moveCount), FONT, MESSAGECOLOR, WINDOWWIDTH - 200, 30,True))

def displayRegularTimeInfo():
    global timeElapsed, blinking, CurState

    if updateTime is True:
        timeElapsed = (pygame.time.get_ticks() - startTime) / 1000

    if GameMode == CLASSIC:
        timeLeft = timeMaxClassic - timeElapsed
        timeToShow = formatTime(timeLeft)
        if timeLeft < 15:
            if timeLeft <= 0:
                CurState = LOSE_STATE
                SCREEN.blit(*makeMenuText('Time: 00:00', FONT, TIME_LOW, WINDOWWIDTH - 200, 60, True))
            elif blinking:
                SCREEN.blit(*makeMenuText('Time: '+timeToShow, FONT, TIME_LOW, WINDOWWIDTH - 200, 60, True))
                blinking = not blinking
            else:
                blinking = not blinking
        elif timeLeft < timeMaxClassic/2:
            SCREEN.blit(*makeMenuText('Time: '+timeToShow, FONT, TIME_MED, WINDOWWIDTH - 200, 60, True))
        else:
            SCREEN.blit(*makeMenuText('Time: '+timeToShow, FONT, TIME_ALOT, WINDOWWIDTH - 200, 60, True))
    else:
        timeToShow = formatTime(timeElapsed)
        SCREEN.blit(*makeMenuText('Time: '+timeToShow, FONT, MESSAGECOLOR, WINDOWWIDTH - 200, 60, True))

def displayLevelIndicatorPanel():
    curpanel = 0
    if LEVELMODE == BABY_SLIDER:
        curpanel = BABYPANEL
    elif LEVELMODE == REGULAR_SLIDER:
        curpanel = REGULARPANEL
    elif LEVELMODE == PREMIER_SLIDER:
        curpanel = PREMIERPANEL
    elif LEVELMODE == EXTREME_SLIDER:
        curpanel = EXTREMEPANEL

    SCREEN.blit(curpanel,(PANELOFFSETX,PANELOFFSETY*3))

def displayGameModeIndicatorPanel():
    curpanel = 0
    if GameMode == ARCADE:
        curpanel = ARCADEPANEL
    elif GameMode == CLASSIC:
        curpanel = CLASSICPANEL
    elif GameMode == FREESTYLE:
        curpanel = FREESTYLEPANEL

    SCREEN.blit(curpanel,(PANELOFFSETX,PANELOFFSETY))

def drawTile(tilex, tiley, data, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley, LEVELMODE)
    SCREEN.blit(IMG,(left+adjx,top+adjy),pygame.Rect(data[0],data[1],TILESIZE,TILESIZE))

def slideAnimation(board, direction, message, animationSpeed):

    blankx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky

    # prepare the base surface
    drawBoard(board, message)
    baseSurf = SCREEN.copy()
    # draw a blank space over the moving tile on the baseSurf Surface.
    moveLeft, moveTop = getLeftTopOfTile(movex, movey, LEVELMODE)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

    for i in range(0, TILESIZE, animationSpeed):
        # animate the tile sliding over
        checkForQuit()
        SCREEN.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateNewPuzzle(boardsize,drawOrNot):
    # From a starting configuration, make numSlides number of moves (and
    # animate these moves).
    sequence = []
    board = getStartingBoard(boardsize)
    if drawOrNot is True:
        drawBoard(board, 'Generating next puzzle, please wait...')
    pygame.display.update()
    # wait 1s when generating image so that user can see how it looks like
    pygame.time.wait(1000)
    lastMove = None
    for i in range(boardsize*boardsize*5):
        move = getRandomMove(board, lastMove)
        makeMove(board, move)
        sequence.append(move)
        lastMove = move
    return (board, sequence)


if __name__ == '__main__':
    main()
