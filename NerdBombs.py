from Weapon import Weapon

class NerdBombs(Weapon):
    
    #Creates Constructor for NerdBombs
    def __init__(self):
        super(Weapon, self).__init__(1, 3.5, 5, "NerdBombs")
