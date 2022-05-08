import random
import sys

from constant import HEIGHT, WIDTH, BLACK, WHITE, RED, GREEN, RestartGameSingle
from save import getBestScores, saveGame


class Menu:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.font = self.pygame.font.SysFont('Time New Roman', 60)

    def displayStartMenu(self):
        self.screen.fill(BLACK)

        # Title Text
        title = self.font.render('SNAKE', False, GREEN)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2, 2*(HEIGHT//7))
        self.screen.blit(title, titleRect)

        # Play Text
        play = self.font.render('p - PLAY', False, WHITE)
        playRect = play.get_rect()
        playRect.center = (WIDTH//2, 3*(HEIGHT//7) + 50)
        self.screen.blit(play, playRect)

        # Load Text
        load = self.font.render('l - LOAD', False, WHITE)
        loadRect = load.get_rect()
        loadRect.center = (WIDTH//2, 3*(HEIGHT//7) + 100)
        self.screen.blit(load, loadRect)

        # Ranking Text
        rank = self.font.render('r - RANKING', False, WHITE)
        rankRect = rank.get_rect()
        rankRect.center = (WIDTH//2, 3*(HEIGHT//7) + 150)
        self.screen.blit(rank, rankRect)

        # Exit Text
        quit = self.font.render('e - EXIT', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2, 6*(HEIGHT//7))
        self.screen.blit(quit, quitRect)

        self.pygame.display.update()

    def displayRanking(self):
        self.screen.fill(BLACK)

        bestScores = getBestScores()
        distance = 0

        # Title Text
        title = self.font.render('HIGH SCORES:', False, RED)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2, HEIGHT//8)
        self.screen.blit(title, titleRect)

        # All Rankings Text
        for entry in bestScores.scores:
            score = self.font.render(
                str(entry.username) + str(entry.score), False, WHITE)
            scoreRect = score.get_rect()
            scoreRect.center = (WIDTH//2, 2*(HEIGHT//8) + distance)
            self.screen.blit(score, scoreRect)
            distance += 50

        self.pygame.display.update()

    def displayPauseMenu(self):
        self.screen.fill(BLACK)

        # Pause Text
        pause = self.font.render('- Pause -', False, WHITE)
        pauseRect = pause.get_rect()
        pauseRect.center = (WIDTH//2, 2*(HEIGHT//7))
        self.screen.blit(pause, pauseRect)

        # Resume Text
        resume = self.font.render('c - RESUME', False, WHITE)
        resumeRect = resume.get_rect()
        resumeRect.center = (WIDTH//2, 3*(HEIGHT//7) + 50)
        self.screen.blit(resume, resumeRect)

        # Restart Text
        restart = self.font.render('r - RESTART', False, WHITE)
        restartRect = restart.get_rect()
        restartRect.center = (WIDTH//2, 3*(HEIGHT//7) + 100)
        self.screen.blit(restart, restartRect)

        # Save Text
        save = self.font.render('s - SAVE', False, WHITE)
        saveRect = save.get_rect()
        saveRect.center = (WIDTH//2, 3*(HEIGHT//7) + 150)
        self.screen.blit(save, saveRect)

        # Exit Text
        quit = self.font.render('e - EXIT', False, WHITE)
        quitRect = quit.get_rect()
        quitRect.center = (WIDTH//2, 6*(HEIGHT//7))
        self.screen.blit(quit, quitRect)

        self.pygame.display.update()

    def displayGameOver(self, score):
        self.screen.fill(BLACK)

        # GameOver Text
        gameOver = self.font.render('GAME OVER', False, RED)
        gameOverRect = gameOver.get_rect()
        gameOverRect.center = (WIDTH//2, (HEIGHT//2) - 25)
        self.screen.blit(gameOver, gameOverRect)

        # Final Score Text
        currentScore = self.font.render(
            'Your Score: ' + str(score), False, RED)
        scoreRect = currentScore.get_rect()
        scoreRect.center = (WIDTH//2, (HEIGHT//2) + 25)
        self.screen.blit(currentScore, scoreRect)

        self.pygame.display.update()

    def pauseMenuSinglePlayer(self, pygame, player, apple, menu):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        return False # False = Not restart game
                    # kills the snake but does not show death screen for resume and save
                    if event.key == pygame.K_r:
                        return True # True = Restart game
                    if event.key == pygame.K_s:
                        saveGame(player.size, player.state,
                                    apple.x, apple.y)
                        player.state[0]['x'] = -5 # Kill player
                        return False
                    if event.key == pygame.K_e:
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
            menu.displayPauseMenu()

    ##! Tim HERE need change "displayPauseMenu()"
    def pauseMenuDualPlayer(self, pygame, menu):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        return False # False = Not restart game
                    #  does not show death screen for resume and save
                    if event.key == pygame.K_r:
                        return True # True = Restart game
                    if event.key == pygame.K_e:
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
            menu.displayPauseMenu()

