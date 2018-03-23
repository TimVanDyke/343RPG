from Weapon import Weapon
import random

class Kiss(Weapon):

    #Creates Constructor for Kisses
    #@Param self
    #   Current Instance
    def __init__(self):
        super(Weapon, self).__init__(1, 1, 1, "Kiss")

    #Uses the weapon and sets a random damage amount
    #@Param self
    #   Current Instance
    def use(self):
        return random.uniform(self.lowerMod, self.upperMod)
