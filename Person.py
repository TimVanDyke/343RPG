from NPC import NPC

class Person(NPC):
    
    #Creates Constructor for Person
    def __init__(self):
        super(NPC, self).__init__(-1, -5, 100, 100)
