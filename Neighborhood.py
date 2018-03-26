from Home import Home
from Player import Player


class Neighborhood():
    def __init__(self, generated):
        self.pos = [0, 0]
        self.generated = generated
        #https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
        print("Neighborhood is instantiated")
        self.w, self.h = 2, 2
        self.x, self.y = 0, 0
        self.Matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        for i in range(0, self.h):
            for j in range(0, self.w):
                self.Matrix[i][j] = Home(generated)

    #Moves Player from house to house
    #@Param Self
    #   Current Instance
    #@Param Player
    #   passes specific player
    def move(self, player):
        print("You are here: ")
        print(self.position)
        print(" ")
        moved = False
        while not moved:
            dir = str(input("please give a direction in quotes: (w for up, a for left, s for down, d for right)"))
            if dir == "w":
                if self.getPos()[1] == 0:
                    print("you are already at the top of the Neighborhood! We need to finish our own Neighborhood first!")
                else:
                    self.setPos(0, -1)
                    alive = self.getHomeAttack(player)
                    if alive is False:
                        return True
                    else:
                        pass
                    moved = True
                    return False
            elif dir == "a":
                if self.getPos()[0] == 0:
                    print("you are already at the left side of the Neighborhood! We need to finish our own Neighborhood first!")
                else:
                    self.setPos(-1, 0)
                    alive = self.getHomeAttack(player)
                    if alive is False:
                        return True
                    else:
                        pass
                    moved = True
                    return False
            elif dir == "s":
                if self.getPos()[1] == self.h - 1:
                    print("you are already at the bottom of the Neighborhood! We need to finish our own Neighborhood first!")
                else:
                    self.setPos(0, 1)
                    alive = self.getHomeAttack(player)
                    if alive is False:
                        return True
                    else:
                        pass
                    moved = True
                    return False
            elif dir == "d":
                if self.getPos()[0] == self.w - 1:
                    print("you are already at the right side of the Neighborhood! We need to finish our own Neighborhood first!")
                else:
                    self.setPos(1, 0)
                    alive = self.getHomeAttack(player)
                    if alive is False:
                        return True
                    else:
                        pass
                    moved = True
                    return False
            else:
                print("Please type 'w', 'a', 's', or 'd'")

    #Return position of Player
    #@Param Self
    #   Current Instance
    def getPos(self):
        return self.pos

    #Sets position of Player
    #@Param Self
    #   Current Instance
    #@Param X
    #   X coordinate of player
    #@Param Y
    #   Y coordinate of player
    def setPos(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    #Returns if house is clear
    #@Param Self
    #   Current Instance
    #@Param Player
    #   Passes Player to this method
    def getHomeAttack(self, player):
        self.Matrix[self.x][self.y].getAttack(player)

    def isMapClear(self):
        for i in range(0, self.h):
            for j in range(0, self.w):
                if not self.Matrix[i][j].getIsClear():
                    return False
        return True
