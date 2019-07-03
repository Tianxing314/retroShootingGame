import pyxel as pp
from random import randint

##the gift class defines an object that would show up in the game and give the player some benefit
class Gift:
    ##constructor
    # @para self
    # @para x the x value
    # @para y the y value
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.type=8
        self.width=5
        self.height=5
        self.life=1

    ##move the gift
    # @para self
    def move(self, score):
        if self.y<245:
            self.y+=randint(2,4)
        else:
            if score%1500 == 0:
                self.x = randint(0, 168)
                self.y = 0
                if 1==randint(1,2):
                    self.type=0 # add HP
                else:
                    self.type=8 # add bullet
    
    ##dwar gift
    # @para self               
    def draw(self):
        pp.blt(self.x, self.y, 1, 69+self.type, 0, 7, 7, 0)

    #reset the gift
    # @para self
    def reset(self):
        self.x=-7
        self.y=-7
        self.life=1