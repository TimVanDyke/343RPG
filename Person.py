from NPC import NPC

class Person(NPC):
    def __init__(self):
        super(NPC, self).__init__(-1, -5, 100, 100)
