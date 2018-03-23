from Observer import Observer
from Neighborhood import Neighborhood
from Player import Player

class Game(Observer):
    def __init__(self, x=1, y=1):
        self.player = Player()
        self.nHood = Neighborhood()
        self.nHood.setPos(x, y)
        self.win = False
        self.gameLoop()

    def observerUpdate(self):
        pass

    def gameLoop(self):
        while not self.win:
            dead = False
            dead = self.nHood.move(self.player)
            if dead:
                self.gameEnd(False)
            self.gameEnd(self.win)

    def gameEnd(self, win):
        if win is True:
            print("You won this time, ready to save the real thing?")
        else:
            if not self.player.isAlive():
                print("You need to be better if you actually plan on saving your family")
