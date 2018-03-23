from Monster import Monster

class Ghoul(Monster):

    #Creates Constructor for Ghouls
    #@Param Self 
    #   Current Instance
    def __init__(self):
        super(Monster, self).__init__(15, 30, 40, 80)

    #Ghouls take a different amount of damage from Nerd Bombs than other weapons
    #@Param Self
    #   Current Instance
    #@Param damage
    #   How much damage the enemy is taking
    #@Param weapon
    #   Passes which weapon is hitting them
    def takeDamage(self, damage, weapon):
        if weapon.getName == "NerdBombs":
            damage = damage * 5
            print("OWWWWWWWWW THIS HURTS SO MUCH MORE THAN ANYTHING ELSE!")
        self.health -= damage
