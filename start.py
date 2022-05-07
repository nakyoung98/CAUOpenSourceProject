import sys
import pygame
import time

from constant import WIDTH, HEIGHT, RestartGame
from gameplay import gameplay
from menu import Menu

pygame.init()

speed = [2, 2]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snacke')

start = True

# Create Menu
menu = Menu(pygame, screen)

while True:
    if RestartGame:
        RestartGame = gameplay(pygame, screen, menu, False)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                RestartGame = gameplay(pygame, screen, menu, False)
            if event.key == pygame.K_l:
                RestartGame = gameplay(pygame, screen, menu, True)
            if event.key == pygame.K_r:
                menu.displayRanking()
                time.sleep(2)
            if event.key == pygame.K_e or event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
    menu.displayStartMenu()
