import sys
import random

from constant import HEIGHT, WIDTH, GAMETICK, MODULO_SCREEN, Orientation


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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


class Player:
    def __init__(self, size, state):
        self.size = size
        self.state = state

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

    def changeOrientation(self, newOrientation):
        if (newOrientation == 'up' and self.state[0]['look'] != 'down'):
            self.state[0]['look'] = 'up'
        if (newOrientation == 'down' and self.state[0]['look'] != 'up'):
            self.state[0]['look'] = 'down'
        if (newOrientation == 'left' and self.state[0]['look'] != 'right'):
            self.state[0]['look'] = 'left'
        if (newOrientation == 'right' and self.state[0]['look'] != 'left'):
            self.state[0]['look'] = 'right'

    def eat(self, apple, lastX, lastY, lastLook):
        if apple.x == self.state[0]['x'] and apple.y == self.state[0]['y']:
            apple.respawn(self.state)
            self.state.append({'x': lastX, 'y': lastY, 'look': lastLook})
            self.size += 1

    def isAlive(self):
        if self.state[0]['x'] < 0 or self.state[0]['y'] < 0 or self.state[0]['x'] > 39 or self.state[0]['y'] > 39:
            return False
        for i in range(len(self.state)):
            for i2 in range(len(self.state)):
                if i != i2 and self.state[i]['x'] == self.state[i2]['x'] and self.state[i]['y'] == self.state[i2]['y']:
                    return False
        return True


def displayGame(pygame, screen, player, apple):
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
    player.eat(apple, lastX, lastY, lastLook)
    a = pygame.image.load("textures/Apple.png")
    screen.blit(a, (apple.x*MODULO_SCREEN, apple.y*MODULO_SCREEN))
    pygame.display.update()
    pass


def gameplay(pygame, screen, loadSave):
    clock = pygame.time.Clock()
    size = 1
    xApple, yApple = random.randint(0, 39), random.randint(0, 39)
    state = [{'x': 19, 'y': 19, 'look': 'up'}]
    # ! Paul c'est ici que tu call ta fonction pour charger une save
    # size, state, xApple, yApple = loadingGame(loadSave)
    #################
    loadSave = loadSave  # useless
    #################

    player = Player(size, state)
    apple = Apple(xApple, yApple)
    bg = pygame.image.load("textures/GameBackground.jpg")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    while player.isAlive():
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
        displayGame(pygame, screen, player, apple)
    return player.size
