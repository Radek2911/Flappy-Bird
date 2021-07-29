import pygame
import time
import random
from pygame.locals import *
from flappybirdradek import Game
def flappymenu():
    pygame.init()
    screen=pygame.display.set_mode((480,480))
    pygame.display.set_caption('Flappy Bird(Rigged)menu!!')
    background=pygame.image.load("Flap.jpg")
    background=pygame.transform.scale(background,(480,550))
    play=pygame.image.load("play 2.png")
    Quit=pygame.image.load("Quit 2.png")
    while True:
        screen.blit(background,(0,0))

        screen.blit(Quit,(52,140))
        screen.blit(play,(200,140))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if 200< event.pos[0] <344 and 140<event.pos[1]<275:
                    Game()
                if 52< event.pos[0] <200 and 140<event.pos[1]<276:
                    
                    pygame.quit()
                    exit()
flappymenu()

