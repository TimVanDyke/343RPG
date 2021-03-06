import random
class NPC(object):

    maxAtt = 1
    minAtt = 1
    health = 1
    name = "Person"

    #Creates Constructor for NPCs
    #@Param self
    #   Current Instance
    def __init__(self, minAtt, maxAtt, minHealth, maxHealth):
        self.maxAtt = maxAtt
        self.minAtt = minAtt
        self.health = random.randint(minHealth, maxHealth)

    #Allows for monster to attack with a chance for critical hit
    #@Param self
    #   Current Instance
    def getAttack(self):
        att = random.randint(self.minAtt, self.maxAtt)

        #normal attack
        if random.randint(1, 10) < 9:
            return att

        #critical hit
        else:
            return att * 3

    #Monster takes damage depending on damage and weapon passed
    #@Param self
    #   Current Instance
    #@Param damage
    #   Damage that NPC will be taking
    #@Param Weapon
    #   Weapon that the player currently holds
    def takeDamage(self, damage, Weapon):
        pass

    #Return true if player is alive and false if player is dead
    #@Param self
    #   Current Instance
    def isAlive(self):
        if self.health > 1:
            return True
        else:
            return False

    def getHealth(self):
        return self.health

    def getName(self):
        return self.name
