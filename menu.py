from constant import HEIGHT, WIDTH, BLACK, RED, GREEN
from random import randint 

class menu:
    def __init__(self, pygame, screen, player):
        self.pygame = pygame
        self.screen = screen
        self.player = player

    def inGameMenu(self):
        self.screen.fill(BLACK)
        
        font = self.pygame.font.SysFont('Time New Roman', 60)
        #Title Text
        title = font.render('SNAKE', False, GREEN)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2 , 100)
        self.screen.blit(title, titleRect)
        
        #High Score Text
        high = font.render('High Score: ' + str(self.player.size), False, RED)
        highRect = high.get_rect()
        highRect.center = (WIDTH//2, HEIGHT//2)
        self.screen.blit(high, highRect)
        
        #Start Text
        start = font.render('Press Space to Start', False, ((randint(0,255),randint(0,255),randint(0,255))))
        startRect = start.get_rect()
        startRect.center = (WIDTH//2 , HEIGHT - 50)
        self.screen.blit(start, startRect)

