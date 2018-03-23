from NPC import NPC

class Monster(NPC):
    
    #Creates Constructor for Monsters
    #@Param self
    #   Current Instance
    def __init__(self):
        super(NPC, self).__init__(1, 1, 1, 1)
    
    #@Param self
    #   Current Instance
    def die(self):
        return "FIXME"
