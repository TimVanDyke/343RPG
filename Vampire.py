from Monster import Monster

class Vampire(Monster):

    def __init__(self):
        super(Monster, self).__init__(0, 20, 100, 200)

    def takeDamage(self, damage, weapon):
        if weapon.getName == "ChocolateBars":
            damage = 0
            print("HAHA YOU CANNOT HURT ME WITH THIS!")
        self.health -= damage
