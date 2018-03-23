from NPC import NPC

class Monster(NPC):
    def __init__(self):
        super(NPC, self).__init__(1, 1, 1, 1)
    def die(self):
        return "FIXME"
