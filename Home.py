import random
from Person import Person
from Ghoul import Ghoul
from Vampire import Vampire
from Werewolf import Werewolf
from Zombie import Zombie
from Player import Player


class Home():
    #Creates Constructor for ChocolateBars
    #@Param Self
    #   Current Instance
    #@Param generated
    #   Specific set
    def __init__(self,generated):
        self.monsters = []
        self.isClear = False
        if generated:
            self.monsters = [Ghoul(), Vampire(), Werewolf(), Zombie()]
        else:
            num = random.randint(0, 10)

            for i in range(0, num):
                rand = random.randint(1, 4)
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

    #Returns if house is clear
    #@Param Self
    #   Current Instance
    def getIsClear(self):
        return self.isClear

    #Returns if house has monsters
    #@Param Self
    #   Current Instance
    def getMonstersLeft(self):
        return self.inventory.__len__

    #Returns if house is clear
    #@Param Self
    #   Current Instance
    #@Param Player
    #   Passes Player with inv
    def getAttack(self, player):
        inv = player.getInventory()
        fightEnd = False
        while not fightEnd:
            print("The monsters in this house are: ")
            for mon in self.monsters:
                print(mon.getName() + ": " + str(mon.getHealth()))
            print("Your health is: " + str(player.getHealth()))
            print("Your inventory is: ")
            for weap in inv:
                if weap.getName() == "Kiss":
                    print(weap.getName() + "; uses: infinite")
                else:
                    print(weap.getName() + "; uses: " + str(weap.getUsesLeft()))
            att = str(input("Please select an attack, do so by typing the name of the weapon: "))
            #used for weapon selection
            weapCount = 0
            for weap in inv:
                weapCount += 1
                if att == weap.getName():
                    print("You are attacking with " + weap.getName() + "!!!")
                    attVal = player.getAttack(weap)
                    #player attacks monsters
                    monCount = 0
                    for mon in self.monsters:
                        kill = mon.takeDamage(attVal, weap.getName())
                        if kill is True:
                            del self.monsters[monCount]
                            self.monsters.append(Person())
                        if weap.getUsesLeft() <= 0:
                            del inv[weapCount - 1]
                            player.setInventory(inv)
                        monCount += 1
                    for mon in self.monsters:
                        monAttVal = mon.getAttack()
                        player.takeDamage(monAttVal)
                        if player.isAlive() is True:
                            pass
                        else:
                            return False
                    monCount = 0
                    for NPC in self.monsters:
                        if NPC.getName() == "Zombie":
                            monCount += 1
                        elif NPC.getName() == "Werewolf":
                            monCount += 1
                        elif NPC.getName() == "Ghoul":
                            monCount += 1
                        elif NPC.getName() == "Vampire":
                            monCount += 1
                        if monCount <= 0:
                            self.isClear = True
                            fightEnd = True
                    break
            print("Please enter a valid attack")
