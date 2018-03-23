from NPC import NPC

class Monster(NPC):
    
    #Creates Constructor for Monsters
    def __init__(self):
        super(NPC, self).__init__(1, 1, 1, 1)
        
    def die(self):
        return "FIXME"
