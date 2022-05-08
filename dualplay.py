import sys
import random
import time

from constant import HEIGHT, RestartGameDual, WIDTH, GAMETICK, MODULO_SCREEN_TWO_PLAYER, Orientation


#! Class use to handle Apple behavior
class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ? Allow to make respawn a new apple
    def respawn(self, stateO, stateT, AppleT):
        xApple, yApple = -1, -1
        for c in range(0, 12):
            xApple, yApple = random.randint(0, 79), random.randint(0, 79)
            for el in stateO:
                if el['x'] == xApple and el['y'] == yApple:
                    xApple, yApple = -1, -1
                    continue
            for el in stateT:
                if el['x'] == xApple and el['y'] == yApple:
                    xApple, yApple = -1, -1
                    continue
            if AppleT.x == xApple and AppleT.y == yApple:
                xApple, yApple = -1, -1
                continue
            break
        if xApple == -1 and yApple == -1:
            for xApple in range(0, 79):
                for yApple in range(0, 79):
                    for el in stateO:
                        if el['x'] == xApple and el['y'] == yApple:
                            continue
                    for el in stateT:
                        if el['x'] == xApple and el['y'] == yApple:
                            continue
                    if AppleT.x == xApple and AppleT.y == yApple:
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
        if (newOrientation == 'up' and self.state[0]['look'] != 'down'):
            self.state[0]['look'] = 'up'
        if (newOrientation == 'down' and self.state[0]['look'] != 'up'):
            self.state[0]['look'] = 'down'
        if (newOrientation == 'left' and self.state[0]['look'] != 'right'):
            self.state[0]['look'] = 'left'
        if (newOrientation == 'right' and self.state[0]['look'] != 'left'):
            self.state[0]['look'] = 'right'

    #! Check If the Snacke Head can eat the Apple
    def CheckEatApple(self, appleO, appleT, PlayerT, lastX, lastY, lastLook):
        if appleO.x == self.state[0]['x'] and appleO.y == self.state[0]['y']:
            appleO.respawn(self.state, PlayerT.state, appleT)
            self.state.append({'x': lastX, 'y': lastY, 'look': lastLook})
            self.size += 1
        elif appleT.x == self.state[0]['x'] and appleT.y == self.state[0]['y']:
            appleT.respawn(self.state, PlayerT.state, appleO)
            self.state.append({'x': lastX, 'y': lastY, 'look': lastLook})
            self.size += 1

    #! Check If the Snacke is alive (return True) or Dead (return False)
    def isAlive(self, PlayerT):
        if self.state[0]['x'] < 0 or self.state[0]['y'] < 0 or self.state[0]['x'] > 79 or self.state[0]['y'] > 79:
            return False
        for i in range(len(self.state)):
            for i2 in range(len(self.state)):
                if i != i2 and self.state[i]['x'] == self.state[i2]['x'] and self.state[i]['y'] == self.state[i2]['y']:
                    return False
        for i in range(len(self.state)):
            for i2 in range(len(PlayerT.state)):
                if self.state[i]['x'] == PlayerT.state[i2]['x'] and self.state[i]['y'] == PlayerT.state[i2]['y']:
                    return False
        return True


#! Handle All Display part (and a little more)
def displayGame(pygame, screen, playerO, playerT, appleO, appleT):
    lastXO, lastYO, lastLookO = playerO.state[len(playerO.state) - 1]['x'], playerO.state[len(
        playerO.state) - 1]['y'], playerO.state[len(playerO.state) - 1]['look']

    lastXT, lastYT, lastLookT = playerT.state[len(playerT.state) - 1]['x'], playerT.state[len(
        playerT.state) - 1]['y'], playerT.state[len(playerT.state) - 1]['look']

    playerO.move()
    playerT.move()
    for i in range(len(playerO.state)):
        z = pygame.image.load("textures/snackeBodyDual.png")
        if i == 0:
            z = pygame.image.load("textures/snackeHeadDual.png")
        if i == len(playerO.state) - 1 and i != 0:
            z = pygame.image.load("textures/snackeTailDual.png")
        z = pygame.transform.rotate(z, Orientation[playerO.state[i]['look']])
        screen.blit(
            z, (playerO.state[i]['x']*MODULO_SCREEN_TWO_PLAYER, playerO.state[i]['y']*MODULO_SCREEN_TWO_PLAYER))

    for i in range(len(playerT.state)):
        z = pygame.image.load("textures/snackeBodyDual.png")
        if i == 0:
            z = pygame.image.load("textures/snackeHeadDual.png")
        if i == len(playerT.state) - 1 and i != 0:
            z = pygame.image.load("textures/snackeTailDual.png")
        z = pygame.transform.rotate(z, Orientation[playerT.state[i]['look']])
        screen.blit(
            z, (playerT.state[i]['x']*MODULO_SCREEN_TWO_PLAYER, playerT.state[i]['y']*MODULO_SCREEN_TWO_PLAYER))

    playerO.CheckEatApple(appleO, appleT, playerT, lastXO, lastYO, lastLookO)
    playerT.CheckEatApple(appleT, appleO, playerO, lastXT, lastYT, lastLookT)
    a = pygame.image.load("textures/AppleDual.png")
    screen.blit(a, (appleO.x*MODULO_SCREEN_TWO_PLAYER, appleO.y*MODULO_SCREEN_TWO_PLAYER))
    screen.blit(a, (appleT.x*MODULO_SCREEN_TWO_PLAYER, appleT.y*MODULO_SCREEN_TWO_PLAYER))
    pygame.display.update()
    pass


#! dualPlay function is use to handle the snacke game for 2 people
#! pygame => lib
#! screen => pygame window
#! menu => menu class handle menu function
def dualPlay(pygame, screen, menu):
    clock = pygame.time.Clock()
    size = 1  # default Value
    xAppleOne, yAppleOne = random.randint(
        0, 79), random.randint(0, 79)  # default Value
    xAppleTwo, yAppleTwo = random.randint(
        0, 79), random.randint(0, 79)  # default Value
    state = [{'x': 19, 'y': 19, 'look': 'down'}]  # default Value
    stateT = [{'x': 59, 'y': 59, 'look': 'up'}]  # default Value
    RestartGameDual = False

    bg = pygame.image.load("textures/GameBackground.jpg")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    # Create Resource
    playerOne = Player(size, state)
    playerTwo = Player(size, stateT)
    appleOne = Apple(xAppleOne, yAppleOne)
    appleTwo = Apple(xAppleTwo, yAppleTwo)

    while playerOne.isAlive(playerTwo) and playerTwo.isAlive(playerOne) and not RestartGameDual:
        pygame.display.update()
        clock.tick(GAMETICK)
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    ##! Playe One
                if event.key == pygame.K_LEFT:
                    playerOne.changeOrientation('left')
                if event.key == pygame.K_DOWN:
                    playerOne.changeOrientation('down')
                if event.key == pygame.K_UP:
                    playerOne.changeOrientation('up')
                if event.key == pygame.K_RIGHT:
                    playerOne.changeOrientation('right')

                    ##! Playe Two  w - a - s - d
                if event.key == pygame.K_a:
                    playerTwo.changeOrientation('left')
                if event.key == pygame.K_s:
                    playerTwo.changeOrientation('down')
                if event.key == pygame.K_w:
                    playerTwo.changeOrientation('up')
                if event.key == pygame.K_d:
                    playerTwo.changeOrientation('right')

                if event.key == pygame.K_ESCAPE:
                    RestartGameDual = menu.pauseMenuDualPlayer(pygame, menu)
        displayGame(pygame, screen, playerOne, playerTwo, appleOne, appleTwo)

    ##! Tim HERE display game over menu if not RestartGameDual
    ##! You can use playerOne.isAlive(playerTwo) or playerTwo.isAlive(playerOne) to know which one is alive
    ##! To know the score, you can access to playerOne.size or playerTwo.size
    # End the game
    # if not RestartGameDual:
    #     menu.displayGameOver(player.size)
    #     addNewScore(Score("Solo Player", player.size))
    #     time.sleep(2)

    return RestartGameDual
