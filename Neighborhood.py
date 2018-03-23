from Home import Home
from Player import Player


class Neighborhood():
    pos = [0, 0]
    def __init__(self, generated):
        self.generated = generated
        #https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
        print("Neighborhood is instantiated")
        w, h = 3, 2
        Matrix = [[0 for x in range(w)] for y in range(h)]
        for i in range(0, h):
            for j in range(0, w):
                Matrix[i][j] = Home(generated)

    def move(self, player):
        moved = False
        print(moved)
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

    def getPos(self):
        return self.pos

    def setPos(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def getHomeAttack(self, player):
        self.Matrix[self.x, self.y].getAttack(player)
