from Monster import Monster
import random

class Zombie(Monster):

    #Creates Constructor for SourStraws
    #@Param Self
    #   Current Instance
    def __init__(self):
        super(Monster, self).__init__(0, 10, 50, 100)
        self.maxAtt = 10
        self.minAtt = 0
        self.name = "Zombie"
        self.health = random.randint(50, 100)

    #Zombies take double the damage when hit with sour straws
    #@Param damage
    #    Damage passed from NPC
    #@Param weapon
    #    Weapon passed from Player
    def takeDamage(self, damage, weapon):
        if weapon == "SourStraws":
            damage = damage * 2
            print("Zombie: OWW SourStraws REALLY HURT ME!")
        self.health -= damage
        print("Zombie takes " + str(damage) + "... " + str(self.health) + " health left")
        if self.health <= 0:
            print("Zombie died")
            return True
        else:
            return False
