import pygame


FLOOR = pygame.image.load('map.png')
GRIDSIZE = 16 #grid size of the map, eg. map will be 16 * 16, when GRIDSIZE = 16
BRIGHTBLUE = (0, 170, 255)
BGCOLOR = BRIGHTBLUE
FPS = 40 #frames per second, the speed rate of the prgram
WINDOWWIDTH = 1000 #window's width in pixel
WINDOWHEIGHT = 800 #window's height in pixel
BG = pygame.image.load("backgroundLevel1.png")

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

def Main():
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    mousex = 0
    mousey = 0
    mouseClicked = False

    while True:
        # draw borad map, all towers, enemies, and dead enemies
        drawBoard()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        gridx, gridy = getGridAtPixel(mousex, mousey)


        pygame.display.update()
        FPSCLOCK.tick(FPS)


#initialize the map
def initialMap():
    map = []
    for i in range(5):
        column = []
        for j in range(9):
            column.append(' ')
        map.append(column)
    return map

#draw the board and auxiliary settings
def drawBoard():
    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(BG, (0, 0))
    floory = 100
    for i in range(5):
        floorx =95
        DISPLAYSURF.blit(FLOOR, (floorx, floory))
        for j in range (9):
            DISPLAYSURF.blit(FLOOR, (floorx, floory))
            floorx += 95
        floory += 100

def getGridAtPixel(mouseX,mouseY):
    gridX = (mouseX-40)/50
    gridY = (mouseY-60)/40
    if gridX>= 0 and gridX<=15 and gridY>=0 and gridY <= 15:
        return gridX,gridY
    else:
        return None,None



Main()



