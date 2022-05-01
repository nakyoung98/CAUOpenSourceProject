from constant import HEIGHT, WIDTH, BLACK, WHITE, RED, GREEN
from random import randint 

from save import getBestScores

class Menu:
    def __init__(self, pygame, screen, score):
        self.pygame = pygame
        self.screen = screen
        self.score = score
        self.font = self.pygame.font.SysFont('Time New Roman', 60)

    def displayStartMenu(self):
        self.screen.fill(BLACK)
        #bestScore = getBestScores()

        #Title Text
        title = self.font.render('SNAKE', False, GREEN)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2 , HEIGHT - HEIGHT//6)
        self.screen.blit(title, titleRect)
        
        #High Score Text
        #First test with any score
        high = self.font.render('High Score: ' + str(8), False, RED)
        highRect = high.get_rect()
        highRect.center = (WIDTH//2, HEIGHT - 2*(HEIGHT//6))
        self.screen.blit(high, highRect)
        
        #Load Text
        load = self.font.render('l - Load Game', False, WHITE)
        loadRect = load.get_rect()
        loadRect.center = (WIDTH//2 , HEIGHT - 4*(HEIGHT//6))
        self.screen.blit(load, loadRect)

        #Quit Text
        quit = self.font.render('q - Quit Game', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2 , HEIGHT - 5*(HEIGHT//6))
        self.screen.blit(quit, quitRect)

        #Start Text
        start = self.font.render('Space - Start Game', False, ((randint(0,255),randint(0,255),randint(0,255))))
        startRect = start.get_rect()
        startRect.center = (WIDTH//2 , HEIGHT - 6*(HEIGHT//6))
        self.screen.blit(start, startRect)

    def displayPauseMenu(self):
        self.screen.fill(BLACK)

        #Pause Text
        pause = self.font.render('- Pause -', False, WHITE)
        pauseRect = pause.get_rect()
        pauseRect.center = (WIDTH//2 , HEIGHT - HEIGHT//6)
        self.screen.blit(pause, pauseRect)
        
        #Score Text
        currentScore = self.font.render('Your Score: ' + str(self.score), False, RED)
        scoreRect = currentScore.get_rect()
        scoreRect.center = (WIDTH//2 , HEIGHT - 2*(HEIGHT//6))
        self.screen.blit(currentScore, scoreRect)

        #Resume Text
        resume = self.font.render('r - Resume Game', False, WHITE)
        resumeRect = resume.get_rect()
        resumeRect.center = (WIDTH//2 , HEIGHT - 4*(HEIGHT//6))
        self.screen.blit(resume, resumeRect)

        #Save Text
        save = self.font.render('s - Save Game', False, WHITE)
        saveRect = save.get_rect()
        saveRect.center = (WIDTH//2 , HEIGHT - 5*(HEIGHT//6))
        self.screen.blit(save, saveRect)

        #Quit Text
        quit = self.font.render('q - Quit Game', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2 , HEIGHT - 6*(HEIGHT//6))
        self.screen.blit(quit, quitRect)
