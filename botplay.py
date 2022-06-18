import time
import sys
import random
from constant import BOTGAMETICK, GAMETICK, HEIGHT, MODULO_SCREEN, WIDTH
from singleplay import Apple, Player, displayGame

def isSnakeInCase(bot, x, y):
    if x < 0 or y < 0 or x >= 40 or y >= 40:
        return -1
    for i in range(len(bot.state)):
        if bot.state[i]['x'] == x and bot.state[i]['y'] == y:
            return -1
    return 0

def tryToGoSomewhere(bot, newDirection):
    freeUp = isSnakeInCase(bot, bot.state[0]['x'], bot.state[0]['y'] - 1)
    freeDown = isSnakeInCase(bot, bot.state[0]['x'], bot.state[0]['y'] + 1)
    freeLeft = isSnakeInCase(bot, bot.state[0]['x'] - 1, bot.state[0]['y'])
    freeRight = isSnakeInCase(bot, bot.state[0]['x'] + 1, bot.state[0]['y'])

    bot.changeOrientation(newDirection)
    if (newDirection == 'up' and freeUp == -1):
        if freeRight == 0:
            bot.changeOrientation('right')
        elif freeDown == 0:
            bot.changeOrientation('down')
        else:
            bot.changeOrientation('left')
        return

    if (newDirection == 'right' and freeRight == -1):
        if freeDown == 0:
            bot.changeOrientation('down')
        elif freeLeft == 0:
            bot.changeOrientation('left')
        else:
            bot.changeOrientation('up')
        return

    if (newDirection == 'down' and freeDown == -1):
        if freeLeft == 0:
            bot.changeOrientation('left')
        elif freeUp == 0:
            bot.changeOrientation('up')
        else:
            bot.changeOrientation('right')
        return

    if (newDirection == 'left' and freeLeft == -1):
        if freeUp == 0:
            bot.changeOrientation('up')
        elif freeRight == 0:
            bot.changeOrientation('right')
        else:
            bot.changeOrientation('down')
        return

def botMove(bot, apple):
    appleX = apple.x
    appleY = apple.y
    botX = bot.state[0]['x']
    botY = bot.state[0]['y']
    diffX = appleX - botX
    diffY = appleY - botY
    # print(diffX, diffY)

    if diffX == 0:
        if diffY > 0:
            tryToGoSomewhere(bot, 'down')
        else:
            tryToGoSomewhere(bot, 'up')
        return
    if diffY == 0:
        if diffX > 0:
            tryToGoSomewhere(bot, 'right')
        else:
            tryToGoSomewhere(bot, 'left')
        return

    if diffX > 0 and diffY > 0:
        if diffX >= diffY:
            tryToGoSomewhere(bot, 'right')
        else:
            tryToGoSomewhere(bot, 'down')
        return
    if diffX < 0 and diffY < 0:
        if diffX >= diffY:
            tryToGoSomewhere(bot, 'left')
        else:
            tryToGoSomewhere(bot, 'up')
        return
    if abs(diffX) - abs(diffY) >= 0:
        if (diffY >= 0):
            tryToGoSomewhere(bot, 'down')
        else:
            tryToGoSomewhere(bot, 'up')
        return
    if abs(diffX) - abs(diffY) < 0:
        if (diffX >= 0):
            tryToGoSomewhere(bot, 'right')
        else:
            tryToGoSomewhere(bot, 'left')
        return

def botEasyWin(bot):
    botX = bot.state[0]['x']
    botY = bot.state[0]['y']
    # print(botX, botY)

    if botY == 0:
        if botX == 0:
            bot.changeOrientation('down')
        else:
            bot.changeOrientation('left')
        return
    
    if botX % 2 == 0:
        if botY == 39:
            bot.changeOrientation('right')
        else:
            bot.changeOrientation('down')
        return

    if botX % 2 == 1:
        if botY == 1 and botX != 39:
            bot.changeOrientation('right')
        else:
            bot.changeOrientation('up')
        return


def botPlay(pygame, screen, menu):
    clock = pygame.time.Clock()
    size = 1
    xApple, yApple = random.randint(
        0, 39), random.randint(0, 39)  # default Value
    state = [{'x': 19, 'y': 19, 'look': 'up'}]  # default Value
    RestartBotGame = False

    bg = pygame.image.load("textures/GameBackground.jpg")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    font = pygame.font.SysFont('Time New Roman', 60)


    bot = Player(size, state)
    apple = Apple(xApple, yApple)

    while bot.isAlive() and not RestartBotGame:
        pygame.display.update()
        clock.tick(BOTGAMETICK)
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        # botMove(bot, apple)
        botEasyWin(bot)
        displayGame(pygame, screen, bot, apple, font)

    # End the game
    if not RestartBotGame and bot.state[0]['x'] != -5:
        menu.displayGameOver(bot.size)
        print(bot.size)
        # addNewScore(Score("Solo Player", player.size))
        time.sleep(0.5)
        botPlay(pygame, screen, menu)