import random
from Kiss import Kiss
from NerdBombs import NerdBombs
from SourStraws import SourStraws
from ChocolateBars import ChocolateBars

class Player():
    minAtt = 20
    maxAtt = 50
    health = 100000000 #random.randint(500, 750)
    inventory = []

    #Creates Constructor for Player
    #@Param self
    #   Current Instance
    #@Param generated
    #   boolean to set or not set preset values
    def __init__(self, generated):
        print("Player is instantiated")
        if generated:
            self.inventory = [Kiss(), SourStraws(), SourStraws(), SourStraws(), NerdBombs(), NerdBombs(), NerdBombs(), ChocolateBars(), ChocolateBars(), ChocolateBars()]
        else:
            for i in range(2, 10):
                rand = random.randint(1, 3)
                if rand == 1:
                    self.inventory[i] = SourStraws()
                elif rand == 2:
                    self.inventory[i] = NerdBombs()
                elif rand == 3:
                    self.inventory[i] = ChocolateBars()
                else:
                    print("You broke something in player")
    #Player Attack and deals damage depending on random amount with chance of critical hit
    #@Param self
    #   Current self
    def getAttack(self, weapon):
        att = random.randint(self.minAtt, self.maxAtt)

        #normal attack
        if random.randint(1, 10) < 9:
            return att * weapon.use()

        #critical hit
        else:
            print("A critical hit!")
            return att * weapon.use() * 3

    #Chance to block attack and allows player to take damage
    #@Param self
    #   Current self
    #@Param damage
    #   damage taken from the monster
    def takeDamage(self, damage):
        rand = random.randint(1, 10)
        #you blocked the attack!
        if rand == 1:
            print("What luck! the attack misses!")
            damage = 0
        print("Player takes " + str(damage) + " Damage")
        self.health -= damage
        if self.health < 0:
            #makes the game slightly more forgiving
            rand = random.randint(1, 10)
            if rand == 1:
                #you get a second wind!
                self.health = 25
                print("You were fading, BUT YOU FEEL A SUDDEN BURST OF ENERGY!")
            else:
                print("You have died, you better practice more before trying the real thing")

    #Returns true if player is alive, if not return false
    #@Param  self
    #   Current self
    def isAlive(self):
        if self.health > 1:
            return True
        else:
            return False

    #Returns prints the whole inventory
    #@Param  self
    #   Current self
    def getInventory(self):
        return self.inventory

    def setInventory(self, inv):
        self.inventory = inv

    def getHealth(self):
        return self.health
