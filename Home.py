import random
from Person import Person
from Ghoul import Ghoul
from Vampire import Vampire
from Werewolf import Werewolf
from Zombie import Zombie
from Oberservable import Observable
from Observer import Observer

class Player(Observable, Observer):
    isClear = False
    inventory = []

    def __init__(self, generated):
        if generated:
            self.inventory = [Ghoul(), Vampire(), Werewolf(), Zombie()]
        else:
            num = random.uniform(0, 10)

            for i in range(0, num):
                rand = random.uniform(1, 4)
                if rand == 1:
                    self.inventory[i] = Ghoul()
                elif rand == 2:
                    self.inventory[i] = Vampire()
                elif rand == 3:
                    self.inventory[i] = Werewolf()
                elif rand == 4:
                    self.inventory[i] = Zombie()
                else:
                    print("You broke something in home")

    def getIsClear(self):
        return self.isClear

    def observableUpdate(self):
        pass

    def observerUpdate(self):
        pass

    def getMonstersLeft(self):
        return self.inventory.__len__()
