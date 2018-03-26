#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import *
from BASECLASS import *
from text_editing import *
import random


def Intersect(
    s1_x,
    s1_y,
    s2_x,
    s2_y,
    ):
    if s1_x > s2_x - 32 and s1_x < s2_x + 32 and s1_y > s2_y - 32 \
        and s1_y < s2_y + 32:
        return 1
    else:
        return 0


start_time = time.get_ticks()

init()
screen = display.set_mode((400, 400))
key.set_repeat(1, 1)
display.set_caption('PyInvaders')
backdrop = image.load('data/backdrop.png')

enemies = []
enemies_time = []
num = []
x = 0

for count in range(0, 8):
    no = random.randint(0, 16)
    while no in num:
        no = random.randint(0, 15)
    num.append(no)
    enemies.append(base_class(no % 8 * 50, no / 8 * 50,
                   'data/baddie.bmp'))
    enemies_time.append(time.get_ticks() / 1000)
    x += 1

hero = base_class(0, 368, 'data/hero.bmp')
ourmissile = base_class(0, 400, 'data/heromissile.bmp')

quit = 0
enemyspeed = 1
count_strikes = 0
check = 0
while quit == 0:
    screen.blit(backdrop, (0, 0))

    seconds = (time.get_ticks() - start_time) / 1000
    mil = (time.get_ticks() - start_time) % 1000

    if (seconds + 1) % 10 == 0:
        check = 1

    if seconds % 10 == 0 and check == 1:
        no = random.randint(0, 15)
        enemies.append(base_class(no % 8 * 50, no / 8 * 50,
                       'data/baddie.bmp'))
        enemies_time.append(time.get_ticks() / 1000)
        check = 0

    for count in range(0, len(enemies)):
        enemies[count].render()

    if ourmissile.y < 399 and ourmissile.y > 0:
        ourmissile.render()
        time.delay(10)
        if ourevent.key == K_SPACE:
            ourmissile.y -= 5
        if ourevent.key == K_s:
            ourmissile.y -= 10

    for count in range(0, len(enemies)):
        if Intersect(ourmissile.x, ourmissile.y, enemies[count].x,
                     enemies[count].y):
            if ourevent.key == K_SPACE:
                del enemies[count]
                del enemies_time[count]
                count_strikes += 1
            if ourevent.key == K_s:
                enemies[count] = base_class(enemies[count].x,
                        enemies[count].y, 'data/alien_small.png')
                enemies_time[count] = seconds - 5
            break

    i = 0
    temp = []
    temp_time = []
    while i < len(enemies):
        if seconds - enemies_time[i] < 10:
            temp.append(enemies[i])
            temp_time.append(enemies_time[i])
        i += 1

    enemies = temp
    enemies_time = temp_time

    hero.render()

    display.update()
    time.delay(5)

    for ourevent in event.get():
        if ourevent.type == KEYDOWN:
            if ourevent.key == K_q:
                screen.fill((0, 0, 0))
                message_display('SCORE: ' + str(count_strikes))
                time.delay(1000)
                quit = 1
            if ourevent.key == K_d and hero.x < 370:
                hero.x += 5
            if ourevent.key == K_a and hero.x > 10:
                hero.x -= 5
            if ourevent.key == K_SPACE:
                ourmissile = base_class(0, 400, 'data/heromissile.bmp')
                ourmissile.x = hero.x
                ourmissile.y = hero.y
            if ourevent.key == K_s:
                ourmissile = base_class(0, 400, 'data/s_image1.png')
                ourmissile.x = hero.x - 16
                ourmissile.y = hero.y + 5


			
