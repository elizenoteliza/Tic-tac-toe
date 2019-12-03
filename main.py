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
class Tile():
    def __init__(self, pos_x, pos_y, dim, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dim = dim
        self.color = color
        self.isDefault = True
    
    def drawRectangle(self, wnd):
        pg.draw.rect(wnd, self.color, (self.pos_x, self.pos_y, self.dim, self.dim))

white = (255, 255, 255)
green = (0, 255, 0)

game_area = [Tile(0, 50 ,60 , white), Tile(20, 50 ,60 , green), Tile(40, 50 ,60 , white),
             Tile(0, 70 ,60 , green), Tile(20, 70 ,60 , white), Tile(40, 70 ,60 , green),
             Tile(0, 90 ,60 , white), Tile(20, 90 ,60 , green), Tile(40, 90 ,60 , white),]

########################################################################
#Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop#
########################################################################
run = True
while run:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            isClicked = pg.mouse.get_pressed()
        if event.type == pg.MOUSEBUTTONUP:
            isClicked = pg.mouse.get_pressed()

        for tile in game_area:
            tile.drawRectangle(wnd)
        
        pg.display.update()
