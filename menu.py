from constant import HEIGHT, WIDTH, BLACK, WHITE, RED, GREEN, PURPLE

from save import getBestScores

class Menu:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.font = self.pygame.font.SysFont('Time New Roman', 60)

    def displayStartMenu(self):
        self.screen.fill(BLACK)
        #bestScore = getBestScores()

        #Title Text
        title = self.font.render('SNAKE', False, GREEN)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2 , HEIGHT//8)
        self.screen.blit(title, titleRect)
        
        #High Score Text
        #First test with any score
        high = self.font.render('High Score: ' + str(0), False, RED)
        highRect = high.get_rect()
        highRect.center = (WIDTH//2, 2*(HEIGHT//8))
        self.screen.blit(high, highRect)
        
        #Load Text
        load = self.font.render('l - Load Game', False, WHITE)
        loadRect = load.get_rect()
        loadRect.center = (WIDTH//2 , 4*(HEIGHT//8))
        self.screen.blit(load, loadRect)

        #Quit Text
        quit = self.font.render('q - Quit Game', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2 , 5*(HEIGHT//8))
        self.screen.blit(quit, quitRect)

        #Start Text
        start = self.font.render('Space - Start Game', False, PURPLE)
        startRect = start.get_rect()
        startRect.center = (WIDTH//2 , 6*(HEIGHT//8))
        self.screen.blit(start, startRect)

        self.pygame.display.update()

    def displayPauseMenu(self, score):
        self.screen.fill(BLACK)

        #Pause Text
        pause = self.font.render('- Pause -', False, WHITE)
        pauseRect = pause.get_rect()
        pauseRect.center = (WIDTH//2 , HEIGHT//8)
        self.screen.blit(pause, pauseRect)
        
        #Score Text
        currentScore = self.font.render('Your Score: ' + str(score), False, RED)
        scoreRect = currentScore.get_rect()
        scoreRect.center = (WIDTH//2 , 2*(HEIGHT//8))
        self.screen.blit(currentScore, scoreRect)

        #Resume Text
        resume = self.font.render('r - Resume Game', False, WHITE)
        resumeRect = resume.get_rect()
        resumeRect.center = (WIDTH//2 , 4*(HEIGHT//8))
        self.screen.blit(resume, resumeRect)

        #Save Text
        save = self.font.render('s - Save Game', False, WHITE)
        saveRect = save.get_rect()
        saveRect.center = (WIDTH//2 , 5*(HEIGHT//8))
        self.screen.blit(save, saveRect)

        #Quit Text
        quit = self.font.render('q - Quit Game', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2 , 6*(HEIGHT//8))
        self.screen.blit(quit, quitRect)

        self.pygame.display.update()
