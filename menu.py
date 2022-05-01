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
        load = self.font.render('l - LOAD', False, WHITE)
        loadRect = load.get_rect()
        loadRect.center = (WIDTH//2 , 4*(HEIGHT//8))
        self.screen.blit(load, loadRect)

        #Quit Text
        quit = self.font.render('e - EXIT', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2 , 5*(HEIGHT//8))
        self.screen.blit(quit, quitRect)

        #Play Text
        start = self.font.render('Space - Play Game', False, PURPLE)
        startRect = start.get_rect()
        startRect.center = (WIDTH//2 , 6*(HEIGHT//8))
        self.screen.blit(start, startRect)

        self.pygame.display.update()

    def displayPauseMenu(self):
        self.screen.fill(BLACK)

        #Pause Text
        pause = self.font.render('- Pause -', False, WHITE)
        pauseRect = pause.get_rect()
        pauseRect.center = (WIDTH//2 , HEIGHT//8)
        self.screen.blit(pause, pauseRect)

        #Resume Text
        resume = self.font.render('c - RESUME', False, WHITE)
        resumeRect = resume.get_rect()
        resumeRect.center = (WIDTH//2 , 3*(HEIGHT//8))
        self.screen.blit(resume, resumeRect)

        #Restart Text
        restart = self.font.render('r - RESTART', False, WHITE)
        restartRect = restart.get_rect()
        restartRect.center = (WIDTH//2 , 4*(HEIGHT//8))
        self.screen.blit(restart, restartRect)

        #Save Text
        save = self.font.render('s - SAVE', False, WHITE)
        saveRect = save.get_rect()
        saveRect.center = (WIDTH//2 , 5*(HEIGHT//8))
        self.screen.blit(save, saveRect)

        #Exit Text
        quit = self.font.render('e - EXIT', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2 , 6*(HEIGHT//8))
        self.screen.blit(quit, quitRect)

        self.pygame.display.update()

    def displayGameOver(self, score):
        self.screen.fill(BLACK)

        #GameOver Text
        gameOver = self.font.render('Your Score: ' + str(score), False, RED)
        gameOverRect = gameOver.get_rect()
        gameOverRect.center = (WIDTH//2 , (HEIGHT//2) + 50)
        self.screen.blit(gameOver, gameOverRect)

        #Final Score Text
        currentScore = self.font.render('Your Score: ' + str(score), False, RED)
        scoreRect = currentScore.get_rect()
        scoreRect.center = (WIDTH//2 , (HEIGHT//2) - 50)
        self.screen.blit(currentScore, scoreRect)
