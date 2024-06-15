##MAP
TILE_SIZE = 32
SCREEN_HEIGHT = 32*11 #480
SCREEN_WIDTH = 32*19
BACKGROUND_COLOUR = (255,0,255)

SCREEN_SIZE_X = 17 ##The size in tiles of the map on screen
SCREEN_SIZE_Y = 13 ##The size in tiles of the map on screen

WATER = 0
GROUND = 0
COLLIDERS = 1
FOLAGE = 2
PLR_BUILD = 3
PLR_SPAWN = 4

LAYER_LIST =[GROUND, COLLIDERS, FOLAGE, PLR_BUILD]
LAYER_NAMES = ["Ground", "Collider", "Resources", "Plr_build"]

##MAIN LOOP
INTRO = 0
MENU = 1
PLAY = 2
DEAD = 3

##PLAYER
SPEED = 2