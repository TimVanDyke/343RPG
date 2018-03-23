import random

class Weapon:
    usesLeft = 1
    lowerMod = 1
    upperMod = 1
    name = "Weapon"

    #Creates Constructor for Weapons
    #@Param self
    #   Current Instance
    #@Param uses
    #   Number of uses a weapon has left
    #@Param lowerMod
    #   Lowest modifier weapon has for attack damage
    #@Param upperMod
    #   Highest modifier weapon has for attack damage
    #@Param name
    #   Name of weapon being used
    def __init__(self, uses, lowerMod, upperMod, name):
        self.usesLeft = uses
        self.lowerMod = lowerMod
        self.upperMod = upperMod
        self.name = name
    
    #minuses a use from weapons when they are used
    #@Param self
    #   Current Instance
    def use(self):
        self.usesLeft -= 1
        return random.uniform(self.lowerMod, self.upperMod)
    
    #returns the amount of uses left on a weapon
    #@Param self
    #   Current Instance
    def getUsesLeft(self):
        return self.usesLeft

    #returns name of current weapon
    #@Param self
    #   Current Instance
    def getName(self):
        return self.name
