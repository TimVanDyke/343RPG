from Monster import Monster

class Werewolf(Monster):

    #Creates Constructor for Werewolves
    #@Param self
    #   Current Instance
    def __init__(self):
        super(Monster, self).__init__(0, 40, 200, 200)
        self.maxAtt = 40
        self.minAtt = 0
        self.health = 200
        self.name = "Werewolf"

    #Werewolves don't take damage from Chocolate Bars or Sour Straws
    #@Param self
    #   Current Instance
    #@Param Damage
    #   passed damage from NPC
    #@Param Weapon
    #   passed weapon from player
    def takeDamage(self, damage, weapon):
        if weapon == "ChocolateBars":
            damage = 0
            print("Werewolf: HAHA YOU CANNOT HURT ME WITH ChocolateBars!")
        if weapon == "SourStraws":
            damage = 0
            print("Werewolf: HAHA YOU CANNOT HURT ME WITH SourStraws!")
        self.health -= damage
        print("Werewolf takes " + str(damage) + "... " + str(self.health) + " health left")
        if self.health <= 0:
            print("Werewolf died")
            return True
        else:
            return False
