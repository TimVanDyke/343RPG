#!/usr/bin/env python3
from Neighborhood import Neighborhood
from Player import Player

class Game():
    def __init__(self, x=1, y=1, generated=True):
        print("Game is instantiated")
        self.player = Player(generated)
        self.nHood = Neighborhood(generated)
        self.nHood.setPos(x, y)
        self.win = False
        self.gameLoop()

    def gameLoop(self):
        while not self.win:
            print("Hello, welcome to the Haunted Neighborhood")
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
        exit()

g = Game()
print("ran")
