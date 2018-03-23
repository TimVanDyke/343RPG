from Monster import Monster

class Werewolf(Monster):

    #Creates Constructor for Werewolves
    def __init__(self):
        super(Monster, self).__init__(0, 40, 200, 200)
        self.maxAtt = 0
        self.minAtt = 40
        self.health = 200
        self.name = "Werewolf"
    #Werewolves don't take damage from Chocolate Bars or Sour Straws
    def takeDamage(self, damage, weapon):
        if weapon == "ChocolateBars":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        if weapon == "SourStraws":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
