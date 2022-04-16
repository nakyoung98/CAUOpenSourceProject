import sys

from constant import HEIGHT, WIDTH, Orientation

# Player()
##
## size, tab(pos,direction,)
##
# move(direction)
# => change cordonné
# => change head direction + body
##
# eat()
# => add body part
##
# isAlive()
# => check if he is alive
##
##


# Apple
##
# position()
##
# respawn()


class Player:
    def __init__(self, size, state):
        self.name = size
        self.state = state

    def move():
        pass

    def changeOrientation(newOrientation):
        pass

    def eat():
        pass

    def isAlive():
        pass


def displayGame(pygame, Player, Apple):
    pass


def gameplay(pygame, screen, loadSave):
    clock = pygame.time.Clock()
    size = 1
    state = [{'x': 19, 'y': 19, 'look': Orientation['up']}]
    # ! Paul c'est ici que tu call ta fonction pour charger une save
    loadSave = loadSave  # useless
    # size, state = loadingGame(loadSave)

    bg = pygame.image.load("textures/GameBackground.jpg")
    bg = pygame.transform.scale(bg,(WIDTH, HEIGHT))

    while True:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        pygame.display.update()
