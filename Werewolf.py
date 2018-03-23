from Monster import Monster

class Werewolf(Monster):

    def __init__(self):
        super(Monster, self).__init__(0, 40, 200, 200)

    def takeDamage(self, damage, weapon):
        if weapon.getName == "ChocolateBars":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        if weapon.getName == "SourStraws":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        self.health -= damage
