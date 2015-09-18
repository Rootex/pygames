import pygame
import sys
from pygame.locals import *

#Window Conf
WIDTH = 640
HEIGHT = 480
BEGIN = 10
SPEED = 4
#Initialization
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cycloid')

#Settings
FPS = 30
fpsClock = pygame.time.Clock()

#Colors
BLACK = pygame.Color(0, 0, 0)
PINK = pygame.Color(255, 192, 192)
WHITE = pygame.Color(255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

DISPLAYSURF.fill(BLACK)

x = 10
y = 10
ball = pygame.image.load('ball.png')
bar = pygame.image.load('bar.jpg')
direction = 'right'
hor = True
vert = True

#Write Text
fontObj = pygame.font.Font('freesansbold.ttf', 20)
textSurfaceObj = fontObj.render('Cycloid Game', True, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (320, 20)

#pygame.draw.circle(DISPLAYSURF, PINK, (x, y), 10)
while True:
    DISPLAYSURF.fill(BLACK)
    if hor is True:
        x += SPEED
        if x == WIDTH - 30:
            hor = False

    if vert is True:
        y += SPEED
        if y == HEIGHT - 70:
            vert = False

    if hor is False:
        x -= SPEED
        if x == BEGIN:
            hor = True

    if vert is False:
        y -= SPEED
        if y == BEGIN:
            vert = True

    DISPLAYSURF.blit(ball, (x, y))
    DISPLAYSURF.blit(bar, (400, 400))
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()

    pygame.display.update()
    fpsClock.tick(FPS)
