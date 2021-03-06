from Monster import Monster
import random

class Ghoul(Monster):

    #Creates Constructor for Ghouls
    #@Param Self
    #   Current Instance
    def __init__(self):
        super(Monster, self).__init__(15, 30, 40, 80)
        self.maxAtt = 30
        self.minAtt = 15
        self.name = "Ghoul"
        self.health = random.randint(40, 80)

    #Ghouls take a different amount of damage from Nerd Bombs than other weapons
    #@Param Self
    #   Current Instance
    #@Param damage
    #   How much damage the enemy is taking
    #@Param weapon
    #   Passes which weapon is hitting them
    def takeDamage(self, damage, weapon):
        if weapon == "NerdBombs":
            damage = damage * 5
            print("OWWWWWWWWW NerdBombs HURT ME MORE THAN ANYTHING ELSE!")
        self.health -= damage
        print("Ghoul takes " + str(damage) + "... " + str(self.health) + " health left")
        if self.health <= 0:
            print("Ghoul died")
            return True
        else:
            return False
