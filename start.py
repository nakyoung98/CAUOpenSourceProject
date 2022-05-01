

import random
import os

import sys
import pygame

from constant import WIDTH, HEIGHT
from gameplay import gameplay

pygame.init()

speed = [2, 2]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snacke')

start = True
ingame = False
load = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    if start:
        gameplay(pygame, screen, ingame, load)
    else:
        for event in pygame.event.get():
            if event.type == pygame.key.get_pressed():
                if event.key == pygame.K_l:
                    load = True
                    start = True
                    ingame = True
                if event.key == pygame.K_q:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    start = True 
                    ingame = True 
