import random
from Person import Person
from Ghoul import Ghoul
from Vampire import Vampire
from Werewolf import Werewolf
from Zombie import Zombie
from Player import Player

class Home():
    isClear = False
    monsters = []

    def __init__(self, generated):
        print("Home is instantiated")
        if generated:
            self.monsters = [Ghoul(), Vampire(), Werewolf(), Zombie()]
        else:
            num = random.uniform(0, 10)

            for i in range(0, num):
                rand = random.uniform(1, 4)
                if rand == 1:
                    self.monsters[i] = Ghoul()
                elif rand == 2:
                    self.monsters[i] = Vampire()
                elif rand == 3:
                    self.monsters[i] = Werewolf()
                elif rand == 4:
                    self.monsters[i] = Zombie()
                else:
                    print("You broke something in home")

    def getIsClear(self):
        return self.isClear

    def getMonstersLeft(self):
        return self.inventory.__len__

    def getAttack(self, player):
        inv = player.getInventory()
        fightEnd = False
        while not fightEnd:
            print("The monsters in this house are: ")
            for mon in self.monsters:
                print(self.monsters[mon].getName() + ": " + mon.getHealth())
            print("Your health is: " + player.getHealth())
            print("Your inventory is: ")
            for weap in inv:
                if weap.getName() == "Kiss":
                    print(inv[weap].getName() + "; uses: infinite")
                else:
                    print(inv[weap].getName() + "; uses: " + weap.getUsesLeft())
            att = int(input("Please select an attack, do so by selecting the correct array index as shown in the inventory (please start countring with 0): "))
            for i in inv:
                if att == i:
                    if inv.__len__ < i + 1:
                        print("You selected outside the inventory")
                    else:
                        print("You are attacking with " + inv[i] + "!!!")
                        attVal = Player.getAttack(inv[i])
                        for mon in self.monsters:
                            kill = self.monsters[mon].takeDamage(attVal, inv[i])
                            if kill is True:
                                self.monsters[mon] = Person()
                            if inv[i].getUsesLeft() <= i:
                                del inv[i]
                            player.setInventory(inv)
                        for mon in self.monsters:
                            monAttVal = self.monsters[mon].getAttack()
                            player.takeDamage(monAttVal)
                            if player.isAlive() is True:
                                pass
                            else:
                                return False
                        fightEnd = True
            print("Please enter a valid inventory index please")
