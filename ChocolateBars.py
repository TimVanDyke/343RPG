from Weapon import Weapon

class ChocolateBars(Weapon):
    
    #Creates Constructor for ChocolateBars
    def __init__(self):
        super(Weapon, self).__init__(4, 2, 2.4, "ChocolateBars")
