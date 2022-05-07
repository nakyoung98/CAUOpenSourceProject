import pickle
import random
from constant import HIGH_SCORES_LENGTH, SAVE_FILE_GAME, SAVE_FILE_SCORES


class Game:
    def __init__(self, size, state, xApple, yApple):
        self.size = size
        self.state = state
        self.xApple = xApple
        self.yApple = yApple


class Score:
    def __init__(self, username, score):
        self.username = username
        self.score = score


class Scores:
    def __init__(self, scores=[]):
        self.scores = scores

    def addNewScore(self, score):
        self.scores.append(score)
        self.scores.sort(key=lambda temp: temp.score, reverse=True)
        if (len(self.scores) > HIGH_SCORES_LENGTH):
            self.scores.pop(HIGH_SCORES_LENGTH - 1)


def loadingGame():
    try:
        picklefile = open(SAVE_FILE_GAME, 'rb')
        game = pickle.load(picklefile)
        picklefile.close()
        return game.size, game.state, game.xApple, game.yApple
    except FileNotFoundError:
        file = open(SAVE_FILE_GAME, 'w+')
        file.close()
        return 1, [{'x': 19, 'y': 19, 'look': 'up'}], random.randint(0, 39), random.randint(0, 39)
    except EOFError:
        return 1, [{'x': 19, 'y': 19, 'look': 'up'}], random.randint(0, 39), random.randint(0, 39)


def saveGame(size, state, xApple, yApple):
    game = Game(size, state, xApple, yApple)
    picklefile = open(SAVE_FILE_GAME, 'wb')
    pickle.dump(game, picklefile)
    picklefile.close()


def getBestScores():
    try:
        picklefile = open(SAVE_FILE_SCORES, 'rb')
        scores = pickle.load(picklefile)
        picklefile.close()
        return scores
    except FileNotFoundError:
        file = open(SAVE_FILE_SCORES, 'w+')
        file.close()
        return Scores()
    except EOFError:
        return Scores()


def saveBestScores(scores):
    picklefile = open(SAVE_FILE_SCORES, 'wb')
    pickle.dump(scores, picklefile)
    picklefile.close()


def addNewScore(score):
    scores = getBestScores()
    scores.addNewScore(score)
    saveBestScores(scores)
