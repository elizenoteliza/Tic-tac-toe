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
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.isDefault = True
        self.dim = 120
        self.temp_color = self.color
   
    def drawRectangle(self, wnd):
        pg.draw.rect(wnd, self.color, (self.pos_x, self.pos_y, self.dim, self.dim))

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (119,136,153)

game_area = [Tile(0, 50, white), Tile(130, 50, green), Tile(260, 50, white),
             Tile(0, 180, green), Tile(130, 180, white), Tile(260, 180, green),
             Tile(0, 310, white), Tile(130, 310, green), Tile(260, 310, white),]



########################################################################
#Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop##Loop#
########################################################################
def drawFrame():
    pg.Surface.fill(wnd, grey)
    for tile in game_area:
            tile.drawRectangle(wnd)
    
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
                        tile.color = grey
                        tile.isDefault = False
                    else:
                        tile.color = blue


                    

                else:
                    tile.color = tile.temp_color

        print(isClicked)
        drawFrame()

pg.quit()

