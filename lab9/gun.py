import math
import random
from random import choice

import pygame
from pygame.draw import *


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
ORANGE = (255, 100, 0)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
grav = 3

class Floor:
    def __init__(self, screen):
        """рисует пол"""
        global HEIGHT
        self.screen = screen
        self.height = HEIGHT - 80

    def draw(self):
        pygame.draw.line(self.screen, BLACK, (0, self.height), (WIDTH, self.height), 1)


class Ball:
    def __init__(self, screen):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 40
        self.y = 450
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        global HEIGHT

        self.x += self.vx
        self.y -= self.vy
        self.vy -= grav

        if self.y > -self.r + floor.height:
            self.vy = -self.vy * 0.5
            self.vx = self.vx * 0.6
            if self.y > -self.r + floor.height:
                self.y = -self.r + floor.height
            if self.vy < 5:
                self.vy = 0

        if self.x > WIDTH - self.r:
            self.vx = -self.vx

        if self.y == floor.height - self.r:
            self.live -= 1
        if self.live == 0:
            self.color = WHITE

    def draw(self):
        """рисует шарик"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        a = obj.x - self.x
        b = obj.y - self.y
        if ((b**2 + a**2) <= (self.r + target.r)**2) :
            return True
        else:
            return False





class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK
        self.x = 10
        self.y = 500
        self.l = 10

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet, len, shoots
        bullet += 1

        self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        new_ball = Ball(self.screen)
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        new_ball.x = self.x
        new_ball.y = self.y
        self.f2_on = 0
        self.f2_power = 10
        balls.append(new_ball)
        shoots += 1

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        y = event.pos[1]
        x = event.pos[0]
        if x - 20 <= 0:
            x = 20.00000000000001
        self.an = math.atan((y-450) / (x-20))
        if self.f2_on:
            self.color = ORANGE
        else:
            self.color = BLACK

    def draw(self):
        """рисует пушку"""
        len = 20 + self.f2_power

        coss = math.cos(self.an)
        sinn = math.sin(self.an)

        if math.sin(self.an) >= 0:
            sinn = 0
            coss = 1

        line(screen, self.color, (self.x, self.y), (self.x + len * coss, self.y + len * sinn), 7)

    def power_up(self):
        """увеличивает силу выстрела"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = ORANGE
        else:
            self.color = BLACK


class Target:

    def __init__(self, screen):
        self.screen = screen
        self.r = random.randint(10, 100)
        self.color = choice(GAME_COLORS)
        self.x = random.randint(400, 700)
        self.y = random.randint(200, 400)
        self.vx = random.randint(-50, 50)
        self.vy = random.randint(-50, 50)
        self.live = 1
        self.points = 0

    def new_target(self):
        """инициализирует новую мишень"""
        global shoots
        shoots = 0
        self.r = random.randint(10, 100)
        self.color = choice(GAME_COLORS)
        self.x = random.randint(400, 700)
        self.y = random.randint(200, 400)
        self.vx = random.randint(-20,20)
        self.vy = random.randint(-20,20)
        self.live = 1

    def draw(self):
        """рисует мишень"""
        circle(self.screen, self.color, (self.x, self.y), self.r)

    def hit(self):
        """Попадание шарика в цель."""
        self.points += 1

    def move(self):
        """движение мишени"""
        self.x += self.vx
        self.y += self.vy

        if (self.x + self.r >= WIDTH) or (self.x - self.r <= 0):
            self.vx = -self.vx
        if (self.y - self.r <= 0) or (self.y + self.r >= floor.height):
            self.vy = -self.vy


class Text:

    def __init__(self):
        self.live = 0

    def write_points(self):
        text_p = font.render('Oчки: ' + str(target.points), False, BLACK)
        screen.blit(text_p, (10, 10))

    #def write_shoots(self):
     #   global shoots
      #  text_s = font.render('Вы уничтожили цель за ' + str(shoots) + ' выстрела(-ов)', False, BLACK)
       # screen.blit(text_s, (10, 50))




pygame.init()
pygame.font.init()
bullet = 0
shoots = 1
balls = []

font = pygame.font.SysFont(None, 40)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
floor = Floor(screen)
text = Text()
finished = False

while not finished:
    screen.fill(WHITE)
    floor.draw()
    gun.draw()
    target.draw()
    text.write_points()
    text.live -= 1
    target.move()

    #if text.live >= 0:
        #text.write_shoots()

    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            gun.fire2_start()
        elif (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            #text.write_shoots()
            text.live = 60
            target.new_target()
    gun.power_up()

pygame.quit()
