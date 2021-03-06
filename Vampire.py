from Monster import Monster
import random

class Vampire(Monster):

    #Creates Constructor for Vampires
    #@Param self
    #   Current Instance
    def __init__(self):
        super(Monster, self).__init__(0, 20, 100, 200)
        self.maxAtt = 20
        self.minAtt = 0
        self.name = "Vampire"
        self.health = random.randint(100, 200)

    #Vampires do not take any damage from Chocolate Bars
    #@Param self
    #   Current Instance
    #@Param damage
    #   Damage going to be taken from player
    #@Param weapon
    #   Weapon that player is currently using
    def takeDamage(self, damage, weapon):
        if weapon == "ChocolateBars":
            damage = 0
            print("Vampire: HAHA YOU CANNOT HURT ME WITH ChocolateBars!")
        self.health -= damage
        print("Vampire takes " + str(damage) + "... " + str(self.health) + " health left")
        if self.health <= 0:
            print("Vampire died")
            return True
        else:
            return False
