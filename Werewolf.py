from Monster import Monster

class Werewolf(Monster):

    name = "Werewolf"
    #Creates Constructor for Werewolves
    def __init__(self):
        super(Monster, self).__init__(0, 40, 200, 200)

    #Werewolves don't take damage from Chocolate Bars or Sour Straws
    def takeDamage(self, damage, weapon):
        if weapon.getName == "ChocolateBars":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        if weapon.getName == "SourStraws":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
