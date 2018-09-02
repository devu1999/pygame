#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import *
init()
screen = display.set_mode((400,400))
def text_objects(text, font):
    textSurface = font.render(text, True, (57,255,20))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = font.Font('freesansbold.ttf',36)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (200,200)
    screen.blit(TextSurf, TextRect)
    display.update()

def show_time(text):
	largeText = font.Font('freesansbold.ttf',18)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (350,350)
	screen.blit(TextSurf, TextRect)
	display.update()

            
