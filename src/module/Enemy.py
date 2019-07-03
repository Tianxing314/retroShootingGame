import pyxel as pp
from random import randint
from time import time

##Enemy class
class Enemy:
    ##Constructor 
    # @para self
    # @para x the x value
    # @para y the y value
    # @para speed the speed of enemy
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width=20
        self.height=20
        self.life=90
        self.type=0

    ##move enemy
    # @para self
    def move(self):
        if self.y>=245:
            self.x=randint(0,155)
            self.y=-9
            self.life=100
            self.width=20
            self.height=20
            self.type=randint(0,1)
        else:
            self.y+=self.speed

    ##draw enemy
    # @para self
    def draw(self):
        t = time()
        if self.life<=0:
            pp.blt(self.x, self.y, 1, 22, 41 if round(t*10)%2==0 else 61, 20, 20, 0)
        else:
            if self.type==0:
                pp.blt(self.x,self.y,1,22,0 if round(t*10)%2==0 else 20, 20,20,0)
            else:
                pp.blt(self.x,self.y,1,0 if round(t*10)%2==0 else 22,82, 20,20,0)

    ##reset enemy 
    # @para self
    def reset(self):
        self.x=randint(0,155)
        self.y=-9
        self.life=100
        self.width=20
        self.height=20

    ##this method is for getting the point of the enemy
    # @para self
    def check_death(self):
        if self.life<=0:
            return 100
        return 0

    ##make the enemy not collidable
    # @para self
    def not_collidable(self):
        self.width=-1000
        self.height=-1000
