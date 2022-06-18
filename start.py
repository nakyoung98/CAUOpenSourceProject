import sys
import pygame
import time
from botplay import botPlay

from constant import WIDTH, HEIGHT, RestartGameSingle, RestartGameDual, FontSize
from dualplay import dualPlay
from singleplay import singlePlay
from menu import Menu

pygame.init()

speed = [2, 2]

def setScreenSize(screenMode):
    if screenMode == 'screen':
        return pygame.display.set_mode((WIDTH, HEIGHT))
    elif screenMode == 'singleScreen':
        return pygame.display.set_mode((WIDTH, HEIGHT+FontSize['score']))
    elif screenMode == 'dualScreen':
        return pygame.display.set_mode((WIDTH, HEIGHT))
    elif screenMode == 'botScreen':
        return pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Snacke')

start = True

# Create Menu
menu = Menu(pygame, setScreenSize('screen'))

while True:
    menu = Menu(pygame, setScreenSize('screen'))

    if RestartGameSingle:
        RestartGameSingle = singlePlay(pygame, setScreenSize('singleScreen'), menu, False)
    if RestartGameDual:
        RestartGameDual = dualPlay(pygame, setScreenSize('dualScreen'), menu)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                RestartGameSingle = singlePlay(pygame, setScreenSize('singleScreen'), menu, False)
            if event.key == pygame.K_d: ##! Dual player Mode
                RestartGameDual = dualPlay(pygame, setScreenSize('dualScreen'), menu)
            if event.key == pygame.K_l:
                RestartGameSingle = singlePlay(pygame, setScreenSize('singleScreen'), menu, True)
            if event.key == pygame.K_r:
                menu.displayRanking()
                time.sleep(2)
            if event.key == pygame.K_b:
                RestartBot = botPlay(pygame, setScreenSize('botScreen'), menu)
            if event.key == pygame.K_e or event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
    menu.displayStartMenu()



