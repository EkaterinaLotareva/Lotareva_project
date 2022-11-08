import pygame
from pygame.draw import*
import random

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 600))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

number_of_balls = 10

x = [None] * number_of_balls
y = [None] * number_of_balls
r = [None] * number_of_balls
V_x = [None] * number_of_balls
V_y = [None] * number_of_balls
color = [None] * number_of_balls

def new_ball():
    '''рисует новый шарик '''
    global x, y, r, V_x, V_y, color
    for i in range(number_of_balls):
        x[i] = random.randint(100, 1100)
        y[i] = random.randint(100, 500)
        r[i] = random.randint(10, 100)
        V_x[i] = random.randint(1, 10)
        V_y[i] = random.randint(1, 10)
        color[i] = COLORS[random.randint(0, 5)]

def draw_balls():
    global x, y, r, V_x, V_y
    '''рисует шарики '''
    screen.fill(BLACK)
    for i in range(number_of_balls):
        circle(screen, color[i], (x[i], y[i]), r[i])
s = 0

def click(event):
    '''проверяет, есть ли попадание'''
    global x, y, r, s
    click_pos = event.pos
    for i in range(number_of_balls):
        if (((click_pos[0] - x[i]) ** 2 + (click_pos[1] - y[i]) ** 2) <= r[i] ** 2 ):
            s += 1

def update_position():
    '''перемещение шариков'''
    global x, y, r, V_x, V_y
    for i in range(number_of_balls):
        x[i] += V_x[i]
        y[i] += V_y[i]
        if (x[i] - r[i] < 0) or (x[i] + r[i] > 1200):
            V_x[i] = -V_x[i]
        if (y[i] - r[i] < 0) or (y[i] + r[i] > 600):
            V_y[i] = -V_y[i]
    screen.fill(BLACK)
    draw_balls()
    pygame.display.update()

new_ball()
draw_balls()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    update_position()
    pygame.display.update()


print(s, 'очков')
pygame.quit()
