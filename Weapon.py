import random

class Weapon:
    usesLeft = 1
    lowerMod = 1
    upperMod = 1
    name = "Weapon"

    def __init__(self, uses, lowerMod, upperMod, name):
        self.usesLeft = uses
        self.lowerMod = lowerMod
        self.upperMod = upperMod
        self.name = name

    def use(self):
        self.usesLeft -= 1
        return random.uniform(self.lowerMod, self.upperMod)

    def getUsesLeft(self):
        return self.usesLeft

    def getName(self):
        return self.name
