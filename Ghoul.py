from Monster import Monster

class Ghoul(Monster):

    #Creates Constructor for Ghouls
    def __init__(self):
        super(Monster, self).__init__(15, 30, 40, 80)

    #Ghouls take a specific amount of damage from Nerd Bombs
    def takeDamage(self, damage, weapon):
        if weapon.getName == "NerdBombs":
            damage = damage * 5
            print("OWWWWWWWWW THIS HURTS SO MUCH MORE THAN ANYTHING ELSE!")
        self.health -= damage
