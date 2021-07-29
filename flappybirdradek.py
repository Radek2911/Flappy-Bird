import pygame
import time
import random

from pygame.locals import *
def Game():
    pygame.init()
    screen=pygame.display.set_mode((480,480))
    pygame.display.set_caption('Flappy Bird(Rigged)!!')
    Bird=pygame.image.load("Bird.png")
    tube=pygame.image.load("tube.png")
    tube=pygame.transform.rotozoom(tube,0,0.5)
    tube2=pygame.image.load("tube.png")
    tube2=pygame.transform.rotozoom(tube2,180,0.5)
    background=pygame.image.load("Flap.jpg")
    background=pygame.transform.scale(background,(480,550))
    ##coordinates for images
    y=240
    x=240
    y2=320
    x2=1000
    y3=-500

    white=(255,255,255)
    somecolor=(255,0,255)
    screen.fill(white)
    clock=pygame.time.Clock()
    score=0
    def show_text(msg,x,y,color):

        fontobj= pygame.font.SysFont('freesans',30)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    while True:
        screen.fill(white)

        screen.blit(background,(0,0))
        clock.tick(20)
        screen.blit(tube,(x2,y2))
        x2=x2-20
        show_text("score="+str(score),30,30,somecolor)

        if x2 == -120:
            x2=480
            score=score+1
            
    ##randomizes the coordinates of the top of the top pipe        
            y3=random.randint(-680,-400)
    ## sets a 180 pixel gap between the top and bottom pipes       
            y2=y3+880
        screen.blit(Bird,(x,y))
        y=y+9
        screen.blit(tube2,(x2+5,y3))
    ##    
        if x >=x2 and x<=x2+105 and y>0 and y<y3+700:
            show_text('game over',240,275, somecolor)
            pygame.display.update()
            time.sleep(2)
            return
        if x >=x2 and x<=x2+105 and y>y3+880 and y<480:
            
            show_text('game over',240,275, somecolor)
            pygame.display.update()
            time.sleep(2)
            return
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    screen.fill(white)
                    y=y-75


