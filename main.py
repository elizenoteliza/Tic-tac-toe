import pygame as pg
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
###
class Tile():
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.isDefault = True
        self.isX = False
        self.isO = False
        self.hoverOver = False
        self.dim = 100
        self.temp_color = self.color
   
    def drawRectangle(self, wnd):
        pg.draw.rect(wnd, self.color, (self.pos_x, self.pos_y, self.dim, self.dim))

    def drawTile(self, wnd):
        if self.isDefault:

            if self.hoverOver:
                wnd.blit(tile_clear_hover, (self.pos_x, self.pos_y))

            else:
                 wnd.blit(tile_clear, (self.pos_x, self.pos_y))

        else:
            wnd.blit(tile_x, (self.pos_x, self.pos_y))

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (119,136,153)

game_area = [Tile(20, 50, white), Tile(150, 50, green), Tile(280, 50, white),
             Tile(20, 180, green), Tile(150, 180, white), Tile(280, 180, green),
             Tile(20, 310, white), Tile(150, 310, green), Tile(280, 310, white),]

########################################################################
#Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop#
########################################################################
def drawFrame():
    pg.Surface.fill(wnd, grey)
    for tile in game_area:
            tile.drawTile(wnd)
    
    pg.display.update()
#####################################
run = True
while run:
    ###
    mousePos = pg.mouse.get_pos()  
    isClicked = pg.mouse.get_pressed() 
    isClicked = pg.mouse.get_pressed() 
    ###
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            isClicked = pg.mouse.get_pressed()
        if event.type == pg.MOUSEBUTTONUP:
            isClicked = pg.mouse.get_pressed()
##############################################
        #Change color/texture of a tile if hover over and on-click.
        for tile in game_area:
            if tile.isDefault:
                if ((mousePos[0] > tile.pos_x) and (mousePos[0] < tile.pos_x + tile.dim) and
                    (mousePos[1] > tile.pos_y) and (mousePos[1] < tile.pos_y +tile.dim)):

                    if isClicked[0] == 1:
                        tile.isDefault = False
                    else:
                        tile.hoverOver = True
                else:
                    tile.hoverOver = False

        drawFrame()

pg.quit()

