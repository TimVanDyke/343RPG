from Weapon import Weapon
import random

class Kiss(Weapon):
    def __init__(self):
        super(Weapon, self).__init__(1, 1, 1, "Kiss")
    def use(self):
        return random.uniform(self.lowerMod, self.upperMod)
