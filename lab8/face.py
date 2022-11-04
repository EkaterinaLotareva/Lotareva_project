import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((500,500))
screen.fill((225,225,225))

circle(screen, (225, 225, 0), (250,250), 150)
circle(screen, (0, 0, 0), (250,250), 150, 1)
circle(screen, (225, 0, 0), (190,230), 30)
circle(screen, (0, 0, 0), (190,230), 30, 1)
circle(screen, (0, 0, 0), (190,230), 10)
circle(screen, (225, 0, 0), (320,230), 20)
circle(screen, (0, 0, 0), (320,230), 20, 1)
circle(screen, (0, 0, 0), (320,230), 10)

line(screen, (0,0,0), (150,160), (250,250), 20)
line(screen, (0,0,0), (270,230), (350,170), 20)
line(screen, (0,0,0), (190,320), (310,320), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
