import pytmx
from Globals import *
import pygame


class map():
    def __init__(self, scrn, map_nom):
        self.screen = scrn
        self.all_maps = ["./Maps/Test1.tmx"]
        self.tmxdata = pytmx.load_pygame(self.all_maps[map_nom]) #map_nom is for which map to play
        self.HEIGHT = self.tmxdata.height
        self.WIDTH = self.tmxdata.width

        #This is the pixel offset between the map origen(top-left) and the screen origen(0,0)
        self.offset_x = TILE_SIZE
        self.offset_y = TILE_SIZE

        # self.Break([0,0], Layer_nom=0)

    


    def render(self):
        for y in range(SCREEN_SIZE_Y):
            for x in range(SCREEN_SIZE_X):
                x_off_mod = (self.offset_x%TILE_SIZE)
                y_off_mod = int(self.offset_y%TILE_SIZE)
                tile_x = int(x+self.offset_x/TILE_SIZE)
                tile_y = int(y+self.offset_y//TILE_SIZE)
                    
                ##GROUND
                tile_img = self.tmxdata.get_tile_image(tile_x,
                                                       tile_y,
                                                       GROUND)
                if tile_img != None:
                    self.screen.blit(tile_img, 
                                    (x*TILE_SIZE-x_off_mod, 
                                    y*TILE_SIZE-y_off_mod))
                
                ##FOLAGE
                tile_img = self.tmxdata.get_tile_image(tile_x,
                                                       tile_y,
                                                       FOLAGE)
                if tile_img != None:
                    self.screen.blit(tile_img, 
                                    (x*TILE_SIZE-x_off_mod, 
                                    y*TILE_SIZE-y_off_mod))
                
                ##PLR_BUILD_LAYER
                tile_img = self.tmxdata.get_tile_image(tile_x,
                                                       tile_y,
                                                       PLR_BUILD)
                if tile_img != None:
                    self.screen.blit(tile_img, 
                                    (x*TILE_SIZE-x_off_mod, 
                                    y*TILE_SIZE-y_off_mod))

    def calculate_scrn_pos(self, pos):
        ##pos = (x,y)
        x = pos[0]-self.offset_x
        y = pos[1]-self.offset_y
        return (x,y)
    
    def Pan(self, plr_pos):
        ##plr_pos = (x,y): screen pos
        Play_A_x = (self.WIDTH-2)*TILE_SIZE ##PLAYABLE_AREA_X
        Play_A_y = (self.HEIGHT-2)*TILE_SIZE ##PLAYABLE_AREA_Y
        centre_off = [plr_pos[0]-(SCREEN_SIZE_X/2)*TILE_SIZE
                    ,plr_pos[1]-(SCREEN_SIZE_Y/2)*TILE_SIZE] #Centre offset of the player(screen offset)

        Move_per_x = (centre_off[0]/(TILE_SIZE*15))*100 #Calculates per. for x-axesses movement
        # Move_per_x = ((centre_off[0]*centre_off[0])/(TILE_SIZE*225))*25 #Calculates per. for x-axesses movementw
        Move_per_x = abs(Move_per_x)
        if Move_per_x > 100: #Caps it at 100%
            Move_per_x = 100
        elif Move_per_x < 1:
            Move_per_x = 0
        
        Move_per_y = (centre_off[1]/(TILE_SIZE*15))*100 #Calculates per. for y-axesses movement
        # Move_per_y = ((centre_off[1]*centre_off[1])/(TILE_SIZE*225))*25 #Calculates per. for y-axesses movement
        Move_per_y = abs(Move_per_y)
        if Move_per_y > 100: #Caps it at 100%
            Move_per_y = 100
        elif Move_per_y < 1:
            Move_per_y = 0

        ## X
        if self.offset_x >= TILE_SIZE and self.offset_x <= Play_A_x:
            self.offset_x += centre_off[0]/100*Move_per_x
        if self.offset_x < TILE_SIZE: #Left Map Boundry
            self.offset_x = TILE_SIZE
        elif self.offset_x+(SCREEN_SIZE_X)*32 > Play_A_x: #Right Map Boundry
            self.offset_x = Play_A_x-(SCREEN_SIZE_X)*32

        ## Y        
        if self.offset_y >= TILE_SIZE and self.offset_y <= Play_A_y:
            self.offset_y += centre_off[1]/100*Move_per_y
        if self.offset_y < TILE_SIZE: #Top Map Boundry
            self.offset_y = TILE_SIZE
        elif self.offset_y+(SCREEN_SIZE_Y)*32 > Play_A_y: #Bottom Map Boundry
            self.offset_y = Play_A_y-(SCREEN_SIZE_Y)*32
    
    def collide(self, rect, pos):
        #rect = (sprite_x_width, sprite_y_width)
        #pos = (sprite_map_x, sprite_map_y)

        pos = (int(pos[0]), int(pos[1]))

        ##SPRITE COLLIDE BOX
        TL_collide = (pos[0], pos[1])  #Top Left of collide box
        BL_collide = (pos[0], pos[1]+rect[1])  #Bottom Left of collide box
        TR_collide = (pos[0]+rect[0], pos[1])  #Top Right pf collide box
        BR_collide = (pos[0]+rect[0], pos[1]+rect[1])  #Bottom Right of collide box
        collide_points = [TL_collide, BL_collide, TR_collide, BR_collide]

        ##CHECK TILES
        TL_tile_pos = (int(TL_collide[0]/TILE_SIZE), int(TL_collide[1]/TILE_SIZE))
        BL_tile_pos = (int(BL_collide[0]/TILE_SIZE), int(BL_collide[1]/TILE_SIZE))
        TR_tile_pos = (int(TR_collide[0]/TILE_SIZE), int(TR_collide[1]/TILE_SIZE))
        BR_tile_pos = (int(BR_collide[0]/TILE_SIZE), int(BR_collide[1]/TILE_SIZE))
        collide_tiles = [TL_tile_pos, BL_tile_pos, TR_tile_pos, BR_tile_pos]

        for index in range(4): #For each of the 4 corners and their tiles
            point = collide_points[index]
            tile = collide_tiles[index]
            for layer in LAYER_LIST:
                collider = self.tmxdata.get_tile_properties(tile[0],   #GETS TILE
                                                            tile[1], 
                                                            layer)
                if collider != None:
                    if "colliders" in collider:
                        collider = collider['colliders']  #GETS COLLISION BOX
                        for c in collider:
                            box_TL = (c.x+ tile[0]*TILE_SIZE,
                                      c.y+ tile[1]*TILE_SIZE)  #Top Left of tile collision box
                            box_BR = (box_TL[0]+c.width,
                                      box_TL[1]+c.height)  #Bottom Right of the collision box
                            if point[0] >= box_TL[0] and point[1] >= box_TL[1]:
                                if point[0] <= box_BR[0] and point[1] <= box_BR[1]:
                                    return True
    


    def Break(self, pos, Layer_nom):
        #pos = (x,y) of tile want to break
        layer = self.tmxdata.get_layer_by_name(LAYER_NAMES[Layer_nom])
        layer.data[pos[1]][pos[0]] = 0
                            
                

        

