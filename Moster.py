from NPC import NPC

class Monster(NPC):

    name = "Monster"
    #Creates Constructor for Monsters
    #@Param self
    #   Current Instance
    def __init__(self):
        super(NPC, self).__init__(1, 1, 1, 1)
