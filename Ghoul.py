from Monster import Monster
import random

class Ghoul(Monster):

    #Creates Constructor for Ghouls
    #@Param Self
    #   Current Instance
    def __init__(self):
        super(Monster, self).__init__(15, 30, 40, 80)
        self.maxAtt = 15
        self.minAtt = 30
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
        print("Ghoul takes " + damage + "... " + self.health + " health left")
        self.health -= damage
        if self.health <= 0:
            print("Monster died")
            return True
        else:
            return False
