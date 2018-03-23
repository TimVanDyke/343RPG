import random
from Kiss import Kiss
from NerdBombs import NerdBombs
from SourStraws import SourStraws
from ChocolateBars import ChocolateBars
from Oberservable import Observable

class Player(Observable):
    minAtt = 10
    maxAtt = 20
    health = random.uniform(100, 125)
    inventory = []

    def __init__(self, generated):
        if generated:
            self.inventory = [Kiss(), SourStraws(), SourStraws(), SourStraws(), NerdBombs(), NerdBombs(), NerdBombs(), ChocolateBars(), ChocolateBars(), ChocolateBars()]
        else:
            for i in range(2, 10):
                rand = random.uniform(1, 3)
                if rand == 1:
                    self.inventory[i] = SourStraws()
                elif rand == 2:
                    self.inventory[i] = NerdBombs()
                elif rand == 3:
                    self.inventory[i] = ChocolateBars()
                else:
                    print("You broke something in player")

    def attack(self):
        att = random.uniform(self.minAtt, self.maxAtt)

        #normal attack
        if random.uniform(1, 10) < 9:
            return att

        #critical hit
        else:
            return att * 3

    def takeDamage(self, damage):
        rand = random.uniform(1, 10)
        #you blocked the attack!
        if rand == 1:
            damage = 0
        self.health -= damage
        if self.health < 0:
            #makes the game slightly more forgiving
            rand = random.uniform(1, 10)
            if rand == 1:
                #you get a second wind!
                self.health = 25
                print("You were fading, BUT YOU FEEL A SUDDEN BURST OF ENERGY!")
            else:
                print("You have died, you better practice more before trying the real thing")

    def isAlive(self):
        if self.health > 1:
            return True
        else:
            return False

    def observableUpdate():
        pass
