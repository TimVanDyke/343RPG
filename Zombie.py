from Monster import Monster
import random

class Zombie(Monster):

    #Creates Constructor for SourStraws
    def __init__(self):
        super(Monster, self).__init__(0, 10, 50, 100)
        self.maxAtt = 0
        self.minAtt = 10
        self.name = "Zombie"
        self.health = random.randint(50, 100)

    #Zombies take double the damage when hit with sour straws
    def takeDamage(self, damage, weapon):
        if weapon.getName == "SourStraws":
            damage = damage * 2
            print("OWW THAT REALLY HURTS ME!")
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
