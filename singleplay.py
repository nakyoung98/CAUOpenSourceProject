from msilib.schema import Font
import sys
import random
import time

from constant import BLACK, HEIGHT, RestartGameSingle, WIDTH, GAMETICK, MODULO_SCREEN, Orientation, WHITE, FontSize
from save import Score, addNewScore, loadingGame, saveGame


#! Class use to handle Apple behavior
class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ? Allow to make respawn a new apple
    def respawn(self, state):
        xApple, yApple = -1, -1
        for c in range(0, 8):
            xApple, yApple = random.randint(0, 39), random.randint(0, 39)
            for el in state:
                if el['x'] == xApple and el['y'] == yApple:
                    xApple, yApple = -1, -1
                    continue
            break
        if xApple == -1 and yApple == -1:
            for xApple in range(0, 39):
                for yApple in range(0, 39):
                    for el in state:
                        if el['x'] == xApple and el['y'] == yApple:
                            continue
                    self.x = xApple
                    self.y = yApple
                    return
        self.x = xApple
        self.y = yApple


#! Class use to handle Player behavior
class Player:
    #!Class Constructor
    #! Size is the snacke lenght (use to calculate the score)
    #! State is a list contain the snake's part (exemple: [{'x': 19, 'y': 19, 'look': 'up'}, {'x': 19, 'y': 18, 'look': 'left'}])
    def __init__(self, size, state):
        self.size = size
        self.state = state

    #! move forward
    def move(self):
        save = self.state[0]['look']
        for i in range(len(self.state)):
            if (self.state[i]['look'] == 'up'):
                self.state[i]['y'] -= 1
            if (self.state[i]['look'] == 'down'):
                self.state[i]['y'] += 1
            if (self.state[i]['look'] == 'left'):
                self.state[i]['x'] -= 1
            if (self.state[i]['look'] == 'right'):
                self.state[i]['x'] += 1
            if i != 0:
                tmp = self.state[i]['look']
                self.state[i]['look'] = save
                save = tmp

    #! Change The direction of the Snacke
    def changeOrientation(self, newOrientation):
        # print('go ', newOrientation)
        if (newOrientation == 'up' and (self.size == 1 or self.state[0]['look'] != 'down')):
            self.state[0]['look'] = 'up'
        if (newOrientation == 'down' and (self.size == 1 or self.state[0]['look'] != 'up')):
            self.state[0]['look'] = 'down'
        if (newOrientation == 'left' and (self.size == 1 or self.state[0]['look'] != 'right')):
            self.state[0]['look'] = 'left'
        if (newOrientation == 'right' and (self.size == 1 or self.state[0]['look'] != 'left')):
            self.state[0]['look'] = 'right'

    #! Check If the Snacke Head can eat the Apple
    def CheckEatApple(self, apple, lastX, lastY, lastLook):
        if apple.x == self.state[0]['x'] and apple.y == self.state[0]['y']:
            apple.respawn(self.state)
            self.state.append({'x': lastX, 'y': lastY, 'look': lastLook})
            self.size += 1

    #! Check If the Snacke is alive (return True) or Dead (return False)
    def isAlive(self):
        if self.state[0]['x'] < 0 or self.state[0]['y'] < 0 or self.state[0]['x'] > 39 or self.state[0]['y'] > 39:
            return False
        for i in range(len(self.state)):
            for i2 in range(len(self.state)):
                if i != i2 and self.state[i]['x'] == self.state[i2]['x'] and self.state[i]['y'] == self.state[i2]['y']:
                    return False
        return True


#! Handle All Display part (and a little more)
def displayGame(pygame, screen, player, apple, font):
    lastX, lastY, lastLook = player.state[len(player.state) - 1]['x'], player.state[len(
        player.state) - 1]['y'], player.state[len(player.state) - 1]['look']
    player.move()
    for i in range(len(player.state)):
        z = pygame.image.load("textures/snackeBody.png")
        if i == 0:
            z = pygame.image.load("textures/snackeHead.png")
        if i == len(player.state) - 1 and i != 0:
            z = pygame.image.load("textures/snackeTail.png")
        z = pygame.transform.rotate(z, Orientation[player.state[i]['look']])
        screen.blit(
            z, (player.state[i]['x']*MODULO_SCREEN, player.state[i]['y']*MODULO_SCREEN))
    player.CheckEatApple(apple, lastX, lastY, lastLook)
    a = pygame.image.load("textures/Apple.png")
    screen.blit(a, (apple.x*MODULO_SCREEN, apple.y*MODULO_SCREEN))

            # Play bot Text
    play = font.render(str(player.size-1), False, BLACK)
    playRect = play.get_rect()
    playRect.center = (WIDTH//2, HEIGHT +FontSize['score']/2)
    screen.blit(play, playRect)

    play = font.render(str(player.size), False, WHITE)
    playRect = play.get_rect()
    playRect.center = (WIDTH//2, HEIGHT +FontSize['score']/2)
    screen.blit(play, playRect)

    pygame.display.update()
    pass


#! singlePlay function is use to handle the snacke game
#! pygame => lib
#! screen => pygame window
#! loadSave => bool for knowing if loading Save Or not
def singlePlay(pygame, screen, menu, loadSave):
    # screen = pygame.display.set_mode((WIDTH, HEIGHT+FontSize['score']))

    clock = pygame.time.Clock()
    size = 1  # default Value
    xApple, yApple = random.randint(
        0, 39), random.randint(0, 39)  # default Value
    state = [{'x': 19, 'y': 19, 'look': 'up'}]  # default Value
    RestartGameSingle = False

    bg = pygame.image.load("textures/GameBackground.jpg")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    font = pygame.font.SysFont('Time New Roman', 60)


    # Use saved game data
    if loadSave:
        size, state, xApple, yApple = loadingGame()

    # Create Resource
    player = Player(size, state)
    apple = Apple(xApple, yApple)

    while player.isAlive() and not RestartGameSingle:
        pygame.display.update()
        clock.tick(GAMETICK)
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changeOrientation('left')
                if event.key == pygame.K_DOWN:
                    player.changeOrientation('down')
                if event.key == pygame.K_UP:
                    player.changeOrientation('up')
                if event.key == pygame.K_RIGHT:
                    player.changeOrientation('right')
                if event.key == pygame.K_ESCAPE:
                    RestartGameSingle = menu.pauseMenuSinglePlayer(
                        pygame, player, apple, menu)
        displayGame(pygame, screen, player, apple, font)

    # End the game
    if not RestartGameSingle and player.state[0]['x'] != -5:
        menu.displayGameOver(player.size)
        addNewScore(Score("Solo Player", player.size))
        time.sleep(2)

    return RestartGameSingle
