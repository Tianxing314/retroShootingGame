import pyxel as pp
from math import sqrt

##This class is used for enemy bullets.
class Smart_Bullet:
	##constructor
	# @para self
	# @para x the x value
	# @para y the y value
	# @para damage the damage of the bullet
	# @para speed the speed of the bullet
	# @para width the width of the bullet
	# @para height the height of the bullet
	def __init__(self, x, y, damage, speed, width, height):
		self.x=x
		self.y=y
		self.speed_x=0
		self.speed_y=0
		self.speed=speed
		self.damage=damage
		self.height=height
		self.width=width
		self.state=0

	##move it
	# @para self
	def move(self):
		if self.state==1:
			self.x+=self.speed_x
			self.y+=self.speed_y
		if self.state==0:
			self.x=175; self.y=0 ### move out of the screen

	##draw it
	# @para self
	def draw(self):
		pp.blt(self.x, self.y, 1, 51, 1, 2, 2)

	##aim player so that the bullet can damage player
	# @para self
	# @para player the player to be aimed
	def aim(self, player):
		x_difference = player.x+10-self.x
		y_difference = player.y+10-self.y
		factor = 0.1+sqrt(x_difference**2+y_difference**2)/self.speed # 0.1 if for `DivideByZeroError`
		self.speed_x = x_difference/factor
		self.speed_y = y_difference/factor

	##reset bullet
	# @para self
	# @para x the x value
	# @para y the y value
	def reset(self, x, y):
		self.x=x
		self.y=y
		self.state=1

##boss smart bullet is inherited from smart bullet class, it has a new picture and the parameters for drawing a picture
# is messy so it is created
class Boss_Smart_Bullet(Smart_Bullet):
	##draw it
	# @para self
	def draw(self):
		pp.blt(self.x, self.y, 1, 62, 0, 5, 5, 0)