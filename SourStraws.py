from Weapon import Weapon

class SourStraws(Weapon):
    
    #Creates Constructor for SourStraws
    #@Param self
    #   Current Instance
    def __init__(self):
        super(Weapon, self).__init__(2, 1, 1.75, "sourStraws")
