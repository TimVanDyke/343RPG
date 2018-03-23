from Weapon import Weapon

class ChocolateBars(Weapon):

    #Creates Constructor for ChocolateBars
    #@Param Self
    #   Current Instance
    def __init__(self):
        super(Weapon, self).__init__()
        self.usesLeft = 4
        self.lowerMod = 2
        self.upperMod = 2.4
        self.name = "ChocolateBars"
