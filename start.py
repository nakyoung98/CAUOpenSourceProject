import sys
import pygame

from constant import WIDTH, HEIGHT
from gameplay import gameplay

pygame.init()

speed = [2, 2]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snacke')

start = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    gameplay(pygame, screen, start)
