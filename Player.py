from Globals import *
import pygame
import sprite_sheet
import Inputs


class Player(pygame.sprite.Sprite):
    def __init__(self,scrn,map):
        super(Player, self).__init__()
        ##DIRECTLY PLR
        # self.image = pygame.image.load("./Assets/Plr_temp.png").convert_alpha()
        self.image = pygame.image.load("./Assets/Plr_temp_2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.map = map
        self.spawn_point = map.tmxdata.get_object_by_name("Spawn")
        ##This is the distance from map origen to plr
        self.map_x = self.spawn_point.x
        ##This is the distance from map origen to plr
        self.map_y = self.spawn_point.y
        self.screen_x = 0
        self.screen_y = 0
        self.move_dir = [0,0] #[x_movement, y_movement]
        self.deg_rot = 0 #degrees rotated

        ##NOT DIRECTLY PLR
        self.mouse = Inputs.Mouse()
    
    def update(self):
        if self.mouse.pressed("Left"):
            pos = [int((self.map_x)/TILE_SIZE),
                   int((self.map_y)/TILE_SIZE)]
            self.map.Break(pos,
                           GROUND)

        x_move = 0
        y_move = 0
        if self.move_dir[0] != 0 and self.move_dir[1] != 0:
            x_move = 0.7
            y_move = 0.7
        else:
            x_move = 1
            y_move = 1
        
        self.map_x += int(x_move*2*self.move_dir[0])
        if self.map.collide([28,28], [self.map_x, self.map_y]):
            self.map_x -= int(x_move*2*self.move_dir[0])
        
        self.map_y += int(y_move*2*self.move_dir[1])
        if self.map.collide([28,28], [self.map_x, self.map_y]):
            self.map_y -= int(y_move*2*self.move_dir[1])


        if self.move_dir[0] == -1: #LEFT
            self.image = sprite_sheet.rotate_img(self.image
                                                 ,90*3
                                                 ,self.deg_rot)
            self.deg_rot = 90*3
        if self.move_dir[0] == 1: #RIGHT
            self.image = sprite_sheet.rotate_img(self.image
                                                 ,90
                                                 ,self.deg_rot)
            self.deg_rot = 90
        if self.move_dir[1] == -1: #UP
            self.image = sprite_sheet.rotate_img(self.image
                                                 ,90*2
                                                 ,self.deg_rot)
            self.deg_rot = 90*2
        if self.move_dir[1] == 1: #DOWN
            self.image = sprite_sheet.rotate_img(self.image
                                                 ,0
                                                 ,self.deg_rot)
            self.deg_rot = 0
        
        self.rect = self.image.get_rect()

        
        ##CONVERTS MAP_POS TO SCREEN_POS
        self.screen_x, self.screen_y = self.map.calculate_scrn_pos( (self.map_x,self.map_y) )
        self.map.Pan((self.screen_x,self.screen_y))
        self.screen_x, self.screen_y = self.map.calculate_scrn_pos( (self.map_x,self.map_y) )
        self.rect.x = self.screen_x
        self.rect.y = self.screen_y


    def move(self, event):
            if event.type == pygame.KEYDOWN:
                ## X_MOVEMENT
                if event.key == pygame.K_a:
                    self.move_dir[0] = -1
                if event.key == pygame.K_d:
                    self.move_dir[0] = 1
                ## Y_MOVEMENT
                if event.key == pygame.K_w:
                    self.move_dir[1] = -1
                if event.key == pygame.K_s:
                    self.move_dir[1] = 1
            if event.type == pygame.KEYUP:
                ## X_MOVEMENT
                if event.key == pygame.K_a:
                    self.move_dir[0] = 0
                if event.key == pygame.K_d:
                    self.move_dir[0] = 0
                ## Y_MOVEMENT
                if event.key == pygame.K_w:
                    self.move_dir[1] = 0
                if event.key == pygame.K_s:
                    self.move_dir[1] = 0