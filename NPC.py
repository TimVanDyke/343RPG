import random
from Observable import Observable
class NPC(Observable):
    maxAtt = 1
    minAtt = 1
    health = 1

    def __init__(self, minAtt, maxAtt, minHealth, maxHealth):
        self.maxAtt = maxAtt
        self.minAtt = minAtt
        self.health = random.uniform(minHealth, maxHealth)

    def attack(self):
        att = random.uniform(self.minAtt, self.maxAtt)

        #normal attack
        if random.uniform(1, 10) < 9:
            return att

        #critical hit
        else:
            return att * 3

    def takeDamage(self, damage, Weapon):
        pass

    def isAlive(self):
        if self.health > 1:
            return True
        else:
            return False
