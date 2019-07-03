import pyxel as pp

##Bullet class
# @brief the root class for palyer's bullets, Chramp's bullets and head's bullets.
class Bullet:
	##Constructor
	# @para self
	# @para x the x position
	# @para y the y position
	# @para damage the damage of the bulet
	# @para speed_x the speed of bullet in the x direction
	# @para speed_y the speed of the bullet in the y direction
	# @para width the width of the bullet
	# @para height the height of the bullet d
	def __init__(self, x, y, damage, speed_x, speed_y, width, height):
		self.x=x
		self.y=y
		self.speed_x=speed_x
		self.speed_y=speed_y
		self.damage=damage
		self.width=width
		self.height=height
    
    ##move it
    # @para self
	def move(self):
		self.x+=self.speed_x
		self.y+=self.speed_y

    ##draw it
    # @para self
	def draw(self):
		pp.blt(self.x, self.y, 1, 45, 1, 1, 3)

    ##reset it
    # @para self
    # @para x, the new x value
    # @para y the new y value
	def reset(self, x, y):
		self.x=x; self.y=y

##Player_Bullet class
# @brief inherited from Bullet class
class Player_Bullet(Bullet):

	##move it
	# @brief when it is in the play zone, it flies normally,
	# when it is not, set it to the specified location (x,y)
	# @para self
	# @para x the specified x value
	# @para y the specified y value
	def move(self, x, y):
		if self.y<=11:
			self.reset(x, y)
		else:	
			self.y-=self.speed_y

    ##move it out of the play zone
    # @brief move it out of the play zone
    # @para self
	def out(self):
		self.x=176; self.y=0

##Boss_Bullet class
# @brief inherited from Bullet class
class Boss_Bullet(Bullet):
	##draw it
    # @para self
	def draw(self):
		pp.blt(self.x, self.y, 1, 56, 0, 5, 5, 0)

##Head_Bullet class
# @brief inherited from Bullet class
class Head_Bullet(Bullet):
	##draw it
    # @para self
	def draw(self):
		pp.blt(self.x, self.y, 1, 50, 6, 5, 5, 0)
