import pygame as pg
import random
######################################################################
#START##START##START##START##START##START##START##START##START##START#
######################################################################
pg.init()
###
scr_width = 500
scr_height = 500
wnd = pg.display.set_mode((scr_width, scr_height))
pg.display.set_caption("PONG by Laazaarus")
############################################################
#VARIABLES##CLASSES##VARIABLES##CLASSES##VARIABLES##CLASSES#
############################################################
###Images
tile_clear = pg.image.load("sprites/nic.bmp")
tile_clear_hover = pg.image.load("sprites/nic_hover.bmp")
tile_o = pg.image.load("sprites/o.bmp")
tile_x = pg.image.load("sprites/x.bmp")
menu_o = pg.image.load("sprites/osmall.bmp")
menu_x = pg.image.load("sprites/xsmall.bmp")
winscreen_o = pg.image.load("sprites/win_o.png")
winscreen_x = pg.image.load("sprites/win_x.png")
no_winner_scr = pg.image.load("sprites/win_no1.png")
turn_scr = pg.image.load("sprites/turn_scr.png")
point_scr = [pg.image.load("sprites/point_numbers/p0.png"), pg.image.load("sprites/point_numbers/p1.png"),
             pg.image.load("sprites/point_numbers/p2.png"), pg.image.load("sprites/point_numbers/p3.png"),
             pg.image.load("sprites/point_numbers/p4.png"), pg.image.load("sprites/point_numbers/p5.png")]
###
class Tile():
    def __init__(self, pos_x, pos_y, value):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.value = value
        self.isDefault = True
        self.isX = False
        self.hoverOver = False
        self.dim = 100


    def drawTile(self, wnd):
        if self.isDefault:

            if self.hoverOver:
                wnd.blit(tile_clear_hover, (self.pos_x, self.pos_y))

            else:
                 wnd.blit(tile_clear, (self.pos_x, self.pos_y))

        else:
            if self.isX:
                wnd.blit(tile_x, (self.pos_x, self.pos_y))
                self.value = 666
            else:
                wnd.blit(tile_o, (self.pos_x, self.pos_y))
                self.value = 999

class Player():
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.points = 0
        
game_area = [Tile(20, 70, 1), Tile(150, 70, 2), Tile(280, 70, 3),
             Tile(20, 200, 4), Tile(150, 200, 5), Tile(280, 200, 6),
             Tile(20, 330, 7), Tile(150, 330, 8), Tile(280, 330, 9)]

player = [Player("First's Name", "X"), Player("Second's Name", "O")]

whoWins = ''

def restartGame():
    global whoWins
    if not(whoWins == '') and doRestart:

            index = 1

            for tile in game_area:

                tile.isDefault = True
                tile.isX = False
                tile.value = index

                index += 1

            whoWins = ''

#Define who starts the game
if random.randint(0,1) == 0:
    xTurn = True

else:
    xTurn = False
###########################

########################################################################
#Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop#
########################################################################
def drawFrame():
    pg.Surface.fill(wnd, (100, 100, 100))
    

    #What to draw if a game is running / there's no winner
    if whoWins == '':

        #Game area
        for tile in game_area:
            tile.drawTile(wnd)
        #Whoose turn
        wnd.blit(turn_scr, (390, 60))
        if xTurn:
            wnd.blit(menu_x, (425, 115))
        else:
            wnd.blit(menu_o, (425, 115))
        #Points
        #xPlayer
        wnd.blit(point_scr[player[0].points], (390, 190))
        wnd.blit(menu_x, (405, 225))
        #yPlayer
        wnd.blit(point_scr[player[1].points], (390, 320))
        wnd.blit(menu_o, (405, 355))

    elif whoWins == 'O':
        wnd.blit(winscreen_o, (0, 0))
    elif whoWins == 'X':
        wnd.blit(winscreen_x, (0, 0))
    elif whoWins == '/':
        #if no one wins and the game is stuck
        wnd.blit(no_winner_scr, (0, 0))


    pg.display.update()
#####################################
run = True
while run:
    ###
    mousePos = pg.mouse.get_pos()  
    isClicked = pg.mouse.get_pressed() 
    isClicked = pg.mouse.get_pressed()
    doRestart = pg.key.get_pressed()[pg.K_r]
    ###
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            isClicked = pg.mouse.get_pressed()
        if event.type == pg.MOUSEBUTTONUP:
            isClicked = pg.mouse.get_pressed()
        if event.type == pg.KEYDOWN:
            doRestart = pg.key.get_pressed()[pg.K_r] 
        ############################################################
        #Change color/texture of a tile if hover over and on-click.#
        ############################################################
        for tile in game_area:

            if whoWins == '':
                if tile.isDefault:
                    if ((mousePos[0] > tile.pos_x) and (mousePos[0] < tile.pos_x + tile.dim) and
                        (mousePos[1] > tile.pos_y) and (mousePos[1] < tile.pos_y +tile.dim)):

                        if isClicked[0] == 1:
                            if xTurn:
                                tile.isX = True
                                xTurn = False
                            else:
                                tile.isX = False
                                xTurn = True

                            tile.isDefault = False
                        else:
                            tile.hoverOver = True
                    else:
                        tile.hoverOver = False


        #### Finding winner ####

            #Horizontal
        if  ((game_area[0].value == game_area[1].value) and (game_area[1].value == game_area[2].value)  or
            ((game_area[3].value == game_area[4].value) and (game_area[4].value == game_area[5].value)) or
            ((game_area[6].value == game_area[7].value) and (game_area[7].value == game_area[8].value)) or
            #Vertical
            ((game_area[0].value == game_area[3].value) and (game_area[3].value == game_area[6].value)) or
            ((game_area[1].value == game_area[4].value) and (game_area[4].value == game_area[7].value)) or
            ((game_area[2].value == game_area[5].value) and (game_area[5].value == game_area[8].value)) or
            #Diagonal
            ((game_area[0].value == game_area[4].value) and (game_area[4].value == game_area[8].value)) or
            ((game_area[2].value == game_area[4].value) and (game_area[4].value == game_area[6].value))):

            if whoWins == '':
                if xTurn == False:
                    player[0].points += 1
                    whoWins = 'X'
                else:
                    player[1].points += 1
                    whoWins = 'O'

            restartGame()

        elif ((not(game_area[0].isDefault)) and (not(game_area[1].isDefault)) and (not(game_area[2].isDefault)) and 
              (not(game_area[3].isDefault)) and (not(game_area[4].isDefault)) and (not(game_area[5].isDefault)) and
              (not(game_area[6].isDefault)) and (not(game_area[7].isDefault)) and (not(game_area[8].isDefault))):

              whoWins = '/'
              restartGame()

        drawFrame()
     
pg.quit()