from Weapon import Weapon
import random

class Kiss(Weapon):
    
    #Creates Constructor for Kisses
    def __init__(self):
        super(Weapon, self).__init__(1, 1, 1, "Kiss")
        
    #Uses the weapon and sets a random damage amount
    def use(self):
        return random.uniform(self.lowerMod, self.upperMod)
