from Monster import Monster
import random

class Vampire(Monster):

    #Creates Constructor for Vampires
    #@Param self
    #   Current Instance
    def __init__(self):
        super(Monster, self).__init__()
        self.maxAtt = 0
        self.minAtt = 20
        self.name = "Vampire"
        self.health = random.uniform(100, 200)

    #Vampires do not take any damage from Chocolate Bars
    #@Param self
    #   Current Instance
    #@Param damage
    #   Damage going to be taken from player
    #@Param weapon
    #   Weapon that player is currently using
    def takeDamage(self, damage, weapon):
        if weapon.getName == "ChocolateBars":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
