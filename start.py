

import random
import os

import sys
import pygame

from constant import WIDTH, HEIGHT
from gameplay import gameplay

pygame.init()

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snacke')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    gameplay(pygame, screen, 'FileNameOfTheLoadSave')