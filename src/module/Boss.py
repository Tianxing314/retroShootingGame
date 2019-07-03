import pyxel as pp
from time import time

## Boss class
# @brief Boss class it self is used fot Chramp, the figure out the basic
# behavior of a boss
class Boss:
	##Constructor 
	# @para self
	# @para life the life of the boss
	# @para width the width of the boss
	# @para height the height of the boss
	def __init__(self, life, width, height):
		self.direction=1
		self.x=0
		self.y=246
		self.life=life
		self.state=0
		self.width=width
		self.height=height

		#state 0 not show up
		#state 1 show up

    ##draw it
    # @para self
	def draw(self):
		t=time()
		if self.life>=5000:
			pp.blt(self.x, self.y, 1, 75, 73 if round(t*10)%2==0 else 12, 60, 60, 0)	
		else:
			pp.blt(self.x, self.y, 1, 75 if round(t*10)%2==0 else 0, 134 if round(t*10)%2==0 else 200, 60, 60, 0)
	
	##move it
	# when it is in state 1 it move left till the end and the 
	# move right to the end and repeat it.
	# @para self
	def move(self):
		if self.state==1:
			if self.x==115:
				self.direction=-1
			elif self.x==0:
				self.direction=1
			if self.direction==1 and self.x<115:
				self.x+=1
			elif self.direction==-1 and self.x>0:
				self.x-=1
		elif self.state==0:
			self.x=0
			self.y=246
    ##show up
    # when the state is 0 and some condidtions meet, it shows aup and its state changes to 1
    # @para self
	def show_up(self):
		if self.state==0:
			self.x=85
			self.y=30
			self.state=1
    
    #check whether it is dead, if dead return points
    # @para self
    # @para life the life that it is going to reset
    # @para point the point going to be returned
    # @return point if it is dead, 0 otherwise
	def check_death(self, life, point):
		if self.life<=0:
			self.reset(life)
			return point
		return 0

	def reset(self, life):
		self.state=0
		self.life=life

##Head class
# @brief inherited form Boss class.
class Head(Boss):
	##draw it
    # @para self
	def draw(self):
		t=time()
		if self.life>=2000:
			pp.blt(self.x, self.y, 1, 44, 12 if round(t*10)%2==0 else 74, 30, 30, 0)	
		else:
			pp.blt(self.x, self.y, 1, 44 if round(t*10)%2==0 else 0, 43 if round(t*10)%2==0 else 200, 30, 30, 0)
   
    ##move it
	# when it is in state 1 it move left till the end and the 
	# move right to the end and repeat it.
	# the difference between it and its parent is that the speed of it is 2.
	# @para self
	def move(self):
		if self.state==1:
			if self.x>=144:
				self.direction=-1
			elif self.x<=2:
				self.direction=1
			if self.direction==1 and self.x<144:
				self.x+=2
			elif self.direction==-1 and self.x>2:
				self.x-=2
		elif self.state==0:
			self.x=0
			self.y=246