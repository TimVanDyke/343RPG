from NPC import NPC

class Monster(NPC):

    #Creates Constructor for Monsters
    #@Param self
    #   Current Instance
    def __init__(self):
        super(NPC, self).__init__()
        self.maxAtt = 1
        self.minAtt = 1
        self.health = 1
        self.name = "Monster"
