import random

class Weapon:
    usesLeft = 1
    lowerMod = 1
    upperMod = 1
    name = "Weapon"

    #Creates Constructor for Weapons
    def __init__(self, uses, lowerMod, upperMod, name):
        self.usesLeft = uses
        self.lowerMod = lowerMod
        self.upperMod = upperMod
        self.name = name
    
    #minuses a use from weapons when they are used
    def use(self):
        self.usesLeft -= 1
        return random.uniform(self.lowerMod, self.upperMod)
    
    #returns the amount of uses left on a weapon
    def getUsesLeft(self):
        return self.usesLeft

    #returns name of a weapon
    def getName(self):
        return self.name
