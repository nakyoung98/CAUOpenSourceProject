from constant import HEIGHT, WIDTH, BLACK, WHITE, RED, GREEN
from random import randint 

class Menu:
    def __init__(self, pygame, screen, score):
        self.pygame = pygame
        self.screen = screen
        self.score = score
        self.font = self.pygame.font.SysFont('Time New Roman', 60)

    def start(self):
        self.screen.fill(BLACK)
        
        #Title Text
        title = self.font.render('SNAKE', False, GREEN)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2 , HEIGHT - HEIGHT//5)
        self.screen.blit(title, titleRect)
        
        #High Score Text
        high = self.font.render('High Score: ' + str(self.score), False, RED)
        highRect = high.get_rect()
        highRect.center = (WIDTH//2, HEIGHT - 2*(HEIGHT//5))
        self.screen.blit(high, highRect)
        
        #Load Text
        load = self.font.render('l - Load Game', False, WHITE)
        loadRect = load.get_rect()
        loadRect.center = (WIDTH//2 , HEIGHT - 3*(HEIGHT//5))
        self.screen.blit(load, loadRect)

        #Start Text
        start = self.font.render('Space - Start Game', False, ((randint(0,255),randint(0,255),randint(0,255))))
        startRect = start.get_rect()
        startRect.center = (WIDTH//2 , HEIGHT - 4*(HEIGHT//5))
        self.screen.blit(start, startRect)

    def pause(self):
        self.screen.fill(BLACK)
        
        #Title Text
        title = self.font.render('SNAKE', False, GREEN)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2 , HEIGHT - HEIGHT//5)
        self.screen.blit(title, titleRect)

        #Pause Text
        pause = self.font.render('- Pause -', False, WHITE)
        pauseRect = pause.get_rect()
        pauseRect.center = (WIDTH//2 , HEIGHT - 3*(HEIGHT//5))
        self.screen.blit(pause, pauseRect)

        #Resume Text
        resume = self.font.render('r - Resume Game', False, WHITE)
        resumeRect = resume.get_rect()
        resumeRect.center = (WIDTH//2 , HEIGHT - 4*(HEIGHT//5))
        self.screen.blit(resume, resumeRect)
