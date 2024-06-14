import pygame
from Globals import *
import Player
import World
import Cycle_timer


##Pygame Setup
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN | pygame.RESIZABLE)
fps = 60
clock = pygame.time.Clock()
full_screen = True

Timer = Cycle_timer.timer(screen)

##KEYFLAGS
K_enter_down = False
K_alt_down = False

state = INTRO
Running = True
Full_screen = True

##WORLD SETUP
Map = World.map(screen, 0)

##PLAYER
player = Player.Player(screen, Map)

##SPRITE GROUPS
S_GROUP = pygame.sprite.Group()
S_GROUP.add(player)

while Running:
    clock.tick(fps)
    key_down_event = None
    key_up_event = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

        if event.type == pygame.KEYDOWN:
            ##TO GO FULLSCREEN
            if event.key == pygame.K_RETURN:
                K_enter_down = True
            elif event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                K_alt_down = True
            else:
                key_down_event = event

        if event.type == pygame.KEYUP:
            ##TO EXIT FULLSCREEN
            if event.key == pygame.K_RETURN:
                K_enter_down = False
            elif event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                K_alt_down = False
            else:
                key_up_event = event
                  
    ##CHECK FOR FULL SCREEN
    if K_alt_down and K_enter_down:
        full_screen = not full_screen
        K_alt_down = False
        K_enter_down = False
        if full_screen == False: 
            screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.SCALED)
        else:
            screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)

    if state == INTRO:
        state = PLAY #ADD INTRO LATER

    elif state == PLAY:
        ##INPUTS
        if key_down_event != None:
            player.move(key_down_event)
        if key_up_event != None:
            player.move(key_up_event)

        ##UPDATE
        S_GROUP.update()

        ##DRAW
        screen.fill(BACKGROUND_COLOUR)
        Map.render()
        S_GROUP.draw(screen)
        Timer.stop()
        pygame.display.update()
        