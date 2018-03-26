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

    #Loops through Game logic
    #@Param Self
    #   Current Instance
    def gameLoop(self):
        print("Hello, welcome to the Haunted Neighborhood")
        while not self.win:
            self.nHood.move(self.player)
            alive = self.player.isAlive()
            if not alive:
                self.gameEnd(False)
            win = self.nHood.isMapClear()
            if win:
                self.gameEnd(True)

    #Check if win condition has been met
    #@Param Self
    #   Current Instance
    #@Param Win
    #   passes win bool to be checked
    def gameEnd(self, win):
        if win is True:
            print("You won this time, ready to save the real thing?")
            exit()
        else:
            if not self.player.isAlive():
                print("You need to be better if you actually plan on saving your family")
                exit()

g = Game()
print("ran")
