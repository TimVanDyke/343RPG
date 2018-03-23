from Weapon import Weapon

class SourStraws(Weapon):

    #Creates Constructor for SourStraws
    #@Param self
    #   Current Instance
    def __init__(self):
        super(Weapon, self).__init__()
        self.usesLeft = 2
        self.lowerMod = 1
        self.upperMod = 1.75
        self.name = "SourStraws"
