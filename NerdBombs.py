from Weapon import Weapon

class NerdBombs(Weapon):

    #Creates Constructor for NerdBombs
    #@Param self
    #   Current Instance
    def __init__(self):
        super(Weapon, self).__init__()
        self.usesLeft = 1
        self.lowerMod = 3.5
        self.upperMod = 5
        self.name = "NerdBombs"
