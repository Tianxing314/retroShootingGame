import pyxel as pp
from time import time

##Player class defines the information of player and its behaviours.
class Player:
    ##constructor
    # @para self
    # @para x the x value
    # @para y the y value
    # @para the life of the player
    def __init__(self, x, y, life):
        self.x=x
        self.y=y
        self.width=20
        self.height=20
        self.life=life
        self.score=0
        self.power=False
        self.energy=0

    ##draw player
    # @ para self
    def draw(self):
        t = time()
        if self.life>100:
            pp.blt( self.x, self.y, 1, 0, 20 if round(t*10)%2==0 else 0, 20, 20, 0)
        else:
            pp.blt( self.x, self.y, 1, 0, 41 if round(t*10)%2==0 else 200, 20, 20, 0)

    ##reset player
    # @para self
    # @para life the new life point
    def reset(self, life):
        self.life=life
        self.score=0
        self.x=77.5
        self.y=200
        self.power=False
        self.energy=0

    ##reset the player
    # @para self
    def death(self):
        self.life=0
