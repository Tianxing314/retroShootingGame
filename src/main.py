import pyxel as pp
from random import randint, uniform
from time import time
from module.Bullet import *
from module.Smart_Bullet import *
from module.Boss import *
from module.Enemy import *
from module.Player import *
from module.Gift import *
from module.Music import *

########## death page info ##############
COL_DEATH = 0
COL_TEXT_DEATH = 7
########## page info ###############
WIDTH = 175
HEIGHT = 245
########## data section info ##########
HEIGHT_DATA= 10
COL_DATA = 6
COL_BACKGROUND_DATA = 5
########## enemy info ############
ENEMY_Y =-9
######### player bullet info ############
PLAYER_DAMAGE   = 30
PLAYER_SPEED_X  = 0
PLAYER_SPEED_Y  = 20
DISTANCE        = 78
PLAYER_WIDTH	= 3
PLAYER_HEIGHT	= 30
PLAYER_LIFE     = 300
######## enemy smart bullet info #########
ENEMY_SMT_SPEED  = 6
ENEMY_SMT_WIDTH  = 2
ENEMY_SMT_HEIGHT = 2
ENEMY_SMT_DAMAGE = 20
######## boss smart bullet info #########
BOSS_SMT_DAMAGE = 70
BOSS_SMT_SPEED = 6
BOSS_SMT_WIDTH = 5
BOSS_SMT_HEIGHT = 5
######## trump info ###########
TRUMP_LIFE = 20000
TRUMP_WIDTH = 60
TRUMP_HEIGHT = 60
TRUMP_POINT = 10000
######## head info ############
HEAD_LIFE = 7500
HEAD_WIDTH = 30
HEAD_HEIGHT = 30
HEAD_POINT = 4000

class Game:
	def __init__(self):
		########################################################################
		#                         INITIALIZATION                               #
		########################################################################

		#                        initialize player                             #

		self.player=Player(WIDTH/2-10, 200, PLAYER_LIFE)

		#                   initialize player's bullet                         #

		self.p_bullet0 = Player_Bullet( self.player.x+10, self.player.y,
										PLAYER_DAMAGE,
										PLAYER_SPEED_X,   PLAYER_SPEED_Y,
										PLAYER_WIDTH,     PLAYER_HEIGHT 
										)
		self.p_bullet1 = Player_Bullet( self.player.x+10, self.player.y-DISTANCE,
										PLAYER_DAMAGE,
										PLAYER_SPEED_X,   PLAYER_SPEED_Y,
										PLAYER_WIDTH,     PLAYER_HEIGHT 
										)
		self.p_bullet2 = Player_Bullet( self.player.x+10, self.player.y-DISTANCE*2,
										PLAYER_DAMAGE,
										PLAYER_SPEED_X,   PLAYER_SPEED_Y,
										PLAYER_WIDTH,     PLAYER_HEIGHT 
										)
		self.left_p_bullet0 = Player_Bullet(self.player.x,     self.player.y+13,
											PLAYER_DAMAGE,
											PLAYER_SPEED_X,    PLAYER_SPEED_Y,
											PLAYER_WIDTH,      PLAYER_HEIGHT 
											)
		self.right_p_bullet0 = Player_Bullet(self.player.x+19, self.player.y+13,
											 PLAYER_DAMAGE,
											 PLAYER_SPEED_X,   PLAYER_SPEED_Y,
											 PLAYER_WIDTH,     PLAYER_HEIGHT 
											)
		self.left_p_bullet1 = Player_Bullet(self.player.x,     self.player.y+13-DISTANCE,
											PLAYER_DAMAGE,
											PLAYER_SPEED_X,    PLAYER_SPEED_Y,
											PLAYER_WIDTH,      PLAYER_HEIGHT 
											)
		self.right_p_bullet1 = Player_Bullet(self.player.x+19, self.player.y+13-DISTANCE,
											 PLAYER_DAMAGE,
											 PLAYER_SPEED_X,   PLAYER_SPEED_Y,
											 PLAYER_WIDTH,     PLAYER_HEIGHT 
											)
		self.left_p_bullet2 = Player_Bullet(self.player.x,     self.player.y+13-DISTANCE*2,
											PLAYER_DAMAGE,
											PLAYER_SPEED_X,    PLAYER_SPEED_Y,
											PLAYER_WIDTH,      PLAYER_HEIGHT 
											)
		self.right_p_bullet2 = Player_Bullet(self.player.x+19, self.player.y+13-DISTANCE*2,
											 PLAYER_DAMAGE,
											 PLAYER_SPEED_X,   PLAYER_SPEED_Y,
											 PLAYER_WIDTH,     PLAYER_HEIGHT 
											)

		#                         initialize gift                              #

		self.gift_x=randint(0, WIDTH-7)
		self.gift_y=0
		self.gift=Gift(self.gift_x, self.gift_y)

        
		#                         initialize boss                              #

		self.Trump = Boss(TRUMP_LIFE, TRUMP_WIDTH, TRUMP_HEIGHT)
		self.head = Head(HEAD_LIFE, HEAD_WIDTH, HEAD_HEIGHT)

		#                         initialize enemy                             #

		self.enemy_speed=randint(1, 3)
		self.enemy0_x=randint(0, 41)
		self.enemy1_x=randint(51, 102)
		self.enemy2_x=randint(112, 155)
		self.enemy3_x=randint(0, 41)
		self.enemy4_x=randint(51, 102)
		self.enemy5_x=randint(112, 155)
		self.enemy0=Enemy(self.enemy0_x, ENEMY_Y, round(uniform(1,3),1))
		self.enemy1=Enemy(self.enemy1_x, ENEMY_Y, round(uniform(1,3),1))
		self.enemy2=Enemy(self.enemy2_x, ENEMY_Y, round(uniform(1,3),1))
		self.enemy3=Enemy(self.enemy3_x, ENEMY_Y, round(uniform(1,3),1))
		self.enemy4=Enemy(self.enemy4_x, ENEMY_Y, round(uniform(1,3),1))
		self.enemy5=Enemy(self.enemy5_x, ENEMY_Y, round(uniform(1,3),1))

		#                      initialize enemy bullet                         #

		self.smart_bullet0=Smart_Bullet(self.enemy0.x+10, self.enemy0.y+20, ENEMY_SMT_DAMAGE,
										ENEMY_SMT_SPEED, ENEMY_SMT_WIDTH, ENEMY_SMT_HEIGHT)
		self.smart_bullet1=Smart_Bullet(self.enemy1.x+10, self.enemy1.y+20, ENEMY_SMT_DAMAGE,
										ENEMY_SMT_SPEED, ENEMY_SMT_WIDTH, ENEMY_SMT_HEIGHT)
		self.smart_bullet2=Smart_Bullet(self.enemy2.x+10, self.enemy2.y+20, ENEMY_SMT_DAMAGE,
										ENEMY_SMT_SPEED, ENEMY_SMT_WIDTH, ENEMY_SMT_HEIGHT)
		self.smart_bullet3=Smart_Bullet(self.enemy3.x+10, self.enemy3.y+20, ENEMY_SMT_DAMAGE,
										ENEMY_SMT_SPEED, ENEMY_SMT_WIDTH, ENEMY_SMT_HEIGHT)
		self.smart_bullet4=Smart_Bullet(self.enemy4.x+10, self.enemy4.y+20, ENEMY_SMT_DAMAGE,
										ENEMY_SMT_SPEED, ENEMY_SMT_WIDTH, ENEMY_SMT_HEIGHT)
		self.smart_bullet5=Smart_Bullet(self.enemy5.x+10, self.enemy5.y+20, ENEMY_SMT_DAMAGE,
										ENEMY_SMT_SPEED, ENEMY_SMT_WIDTH, ENEMY_SMT_HEIGHT)

		#                     initialize Trump's bullet                        #

		self.boss_bullet0=Boss_Bullet( self.Trump.x+30, self.Trump.y+30, 40,
										-2.56, 1.56, 5, 5)
		self.boss_bullet1=Boss_Bullet( self.Trump.x+30, self.Trump.y+30, 40,
										-1.56, 2.56, 5, 5)
		self.boss_bullet2=Boss_Bullet( self.Trump.x+30, self.Trump.y+30, 40,
										0, 3, 5, 5)
		self.boss_bullet3=Boss_Bullet( self.Trump.x+30, self.Trump.y+30, 40,
										1.56, 2.56, 5, 5)
		self.boss_bullet4=Boss_Bullet( self.Trump.x+30, self.Trump.y+30, 40,
										2.56, 1.56, 5, 5)

		#                   initialize Trump's smart bullet                    #

		self.boss_smart_bullet=Boss_Smart_Bullet(self.Trump.x+30, self.Trump.y+30, 
													BOSS_SMT_DAMAGE, BOSS_SMT_SPEED,
													BOSS_SMT_WIDTH, BOSS_SMT_HEIGHT)

		#                     initialize head's bullet                         #

		self.head_bullet0=Head_Bullet(self.head.x+15, self.head.y+15, 25, 0, 5.5, 5, 5)
		self.head_bullet1=Head_Bullet(self.head.x+15, self.head.y+15, 25, 0, 5.5, 5, 5)
		self.head_bullet2=Head_Bullet(self.head.x+15, self.head.y+15, 25, 0, 5.5, 5, 5)
		self.head_bullet3=Head_Bullet(self.head.x+15, self.head.y+15, 25, 0, 5.5, 5, 5)
		self.head_bullet4=Head_Bullet(self.head.x+15, self.head.y+15, 25, 0, 5.5, 5, 5)

		########################################################################
		#                        system information                            #
		########################################################################

		self.state=0  	# 0: start page 
						# 1: playing
						# 1: death page
		pp.init(WIDTH, HEIGHT, caption='Shoot Game', scale=3, fps=35)
		self.bgm=Bgm()
		self.bgm.landpage_music()
		pp.image(0).load(0, 0, "asset/space.png")
		pp.image(1).load(0, 0, "asset/elements.png")
		pp.run(self.update, self.draw)

	def reset(self):
		self.bgm.stop_music()
		self.bgm.landpage_music()
		self.player.reset(PLAYER_LIFE)
		self.Trump.reset(TRUMP_LIFE)
		self.head.reset(HEAD_LIFE)
		self.enemy0.reset()
		self.enemy1.reset()
		self.enemy2.reset()
		self.enemy3.reset()
		self.enemy4.reset()
		self.enemy5.reset()
		self.smart_bullet0.reset(self.enemy0.x, self.enemy0.y)
		self.smart_bullet1.reset(self.enemy1.x, self.enemy1.y)
		self.smart_bullet2.reset(self.enemy2.x, self.enemy2.y)
		self.smart_bullet3.reset(self.enemy3.x, self.enemy3.y)
		self.smart_bullet4.reset(self.enemy4.x, self.enemy4.y)
		self.smart_bullet5.reset(self.enemy5.x, self.enemy5.y)
		self.boss_bullet0.reset(self.Trump.x+30, self.Trump.y+30)
		self.boss_bullet1.reset(self.Trump.x+30, self.Trump.y+30)
		self.boss_bullet2.reset(self.Trump.x+30, self.Trump.y+30)
		self.boss_bullet3.reset(self.Trump.x+30, self.Trump.y+30)
		self.boss_bullet4.reset(self.Trump.x+30, self.Trump.y+30)
		self.boss_smart_bullet.reset(self.Trump.x+30, self.Trump.y+30)
		self.head_bullet0.reset(self.head.x+15, self.head.y+15)
		self.head_bullet1.reset(self.head.x+15, self.head.y+15)
		self.head_bullet2.reset(self.head.x+15, self.head.y+15)
		self.head_bullet3.reset(self.head.x+15, self.head.y+15)
		self.head_bullet4.reset(self.head.x+15, self.head.y+15)
		self.gift.reset()
		self.state=0

	########################################################################
	#                                LOGIC.                                #
	########################################################################

	#                              Main update                             #

	##Override the update method.
	# @para self
	def update(self):

		# 					keyboard control (Global)	

		if pp.btn(pp.KEY_SPACE):
			self.state = 1 
			self.bgm.stop_music()
		if pp.btn(pp.KEY_Q):
			pp.quit()
		if pp.btn(pp.KEY_R):
			self.reset()
		if pp.btn(pp.KEY_B) and pp.btn(pp.KEY_C):
			self.Trump.show_up()
		if pp.btn(pp.KEY_1):
			self.player.life=100000

		#							 ultra

		if self.player.energy==5000:
			if pp.btn(pp.KEY_U):
				self.Trump.life-=3500
				self.head.life-=3500
				self.enemy0.life-=3500
				self.enemy1.life-=3500
				self.enemy2.life-=3500
				self.enemy3.life-=3500
				self.enemy4.life-=3500
				self.enemy5.life-=3500
				self.player.energy=0

		# 							game events

		if self.player.life>0:
			self.update_player() 

			# 					   update events

			self.update_enemy_player()				# player plane    and   enemy plane
			self.update_player_boss()				# player plane    and   Trump
			self.update_player_head()				# player plane    and   head
			self.update_player_gift()				# player plane 	  and   gift
			self.update_player_smt_bullet()			# player plane    and   enemy plane bullet
			self.update_player_bossbullet()			# player plane    and   Trump bullet
			self.update_player_boss_smartbullet()   # player plane    and   Trump smart bullet
			self.update_headbullet_player()         # player plane    and   head bullet
			self.update_bullet_enemy()				# player bullet   and   enemy plane
			self.update_bullet_boss()				# player bullet   and   Trump
			self.update_bullet_head()				# player bullet   and   head				

			
	##update player 
	# some controls over player plane like changing its position, life, power, etc.
	# @para self
	def update_player(self):
		if pp.btn(pp.KEY_A) or pp.btn(pp.KEY_LEFT):
			self.player.x = max(self.player.x-4, 0)
		if pp.btn(pp.KEY_D) or pp.btn(pp.KEY_RIGHT):
			self.player.x = min(self.player.x+4, WIDTH-20)	
		if pp.btn(pp.KEY_W) or pp.btn(pp.KEY_UP):
			self.player.y = max(self.player.y-4, 11)
		if pp.btn(pp.KEY_S) or pp.btn(pp.KEY_DOWN):
			self.player.y = min(self.player.y+4, HEIGHT-20)
		if pp.btn(pp.KEY_P) and pp.btn(pp.KEY_O):
			self.player.power=True
		if pp.btn(pp.KEY_P) and pp.btn(pp.KEY_L):
			self.player.power=False
		if pp.btn(pp.KEY_P) and pp.btn(pp.KEY_K):
			self.player.life=0

	########################################################################
	# 						  Event of Collision                           #
	########################################################################

	## Check whether two objects colllide
	# @para self
	# @para object1 one of two objects
	# @para object2 one of two objects
	def collision(self,object1, object2):
		if object1.x<=object2.x+object2.width and object1.x>=object2.x-object1.width:
			return object1.y<=object2.y+object2.height and object1.y>=object2.y-object1.height
		return False

	# 						    player and gift                            #

	##check player plane and gift
	# @para self
	def update_player_gift(self): 
		if self.collision(self.player, self.gift):
			self.bgm.gift_music()
			self.gift.reset()
			if self.gift.type==8:
				if self.player.power==False:
					self.player.power=True
				else:
					self.player.score+=200
			else:
				self.player.life+=50

	# 						   player and enemy                            #

	##check all enemy(6) and player
	# @para self
	def update_enemy_player(self):
		self.enemy_player(self.enemy0)
		self.enemy_player(self.enemy1)
		self.enemy_player(self.enemy2)
		self.enemy_player(self.enemy3)
		self.enemy_player(self.enemy4)
		self.enemy_player(self.enemy5)

	##check one enemy and player
	# @para self
	# @para enemy
	def enemy_player(self, enemy):
		if self.collision(self.player, enemy):
			self.bgm.damage_music()
			self.player.power=False
			self.player.life-=30
			enemy.life-=enemy.life
			self.player.score+=enemy.check_death()
			enemy.not_collidable()     ### this is for the animation

	# 					   player bullet and enemy                         #

	##Check all player bullets and enemies
	# @para self
	def update_bullet_enemy(self):
		self.c_bullet_all_enemy(self.p_bullet0)
		self.c_bullet_all_enemy(self.p_bullet1)
		self.c_bullet_all_enemy(self.p_bullet2)
		self.c_bullet_all_enemy(self.left_p_bullet0)
		self.c_bullet_all_enemy(self.right_p_bullet0)
		self.c_bullet_all_enemy(self.left_p_bullet1)
		self.c_bullet_all_enemy(self.right_p_bullet1)
		self.c_bullet_all_enemy(self.left_p_bullet2)
		self.c_bullet_all_enemy(self.right_p_bullet2)

	##Check one player bullets and all enemies
	# @para self
	# @para bullet the bullet to be checked
	def c_bullet_all_enemy(self, bullet):
		self.c_bullet_enemy(bullet, self.enemy0)
		self.c_bullet_enemy(bullet, self.enemy1)
		self.c_bullet_enemy(bullet, self.enemy2)
		self.c_bullet_enemy(bullet, self.enemy3)
		self.c_bullet_enemy(bullet, self.enemy4)
		self.c_bullet_enemy(bullet, self.enemy5)

	##check one bullet and one enemy
	# @para self
	# @para bullet teh bullet to be checked
	# @para enemy the enemy to be checked
	def c_bullet_enemy(self, bullet, enemy):
		if self.collision(bullet, enemy):
			self.bgm.damage_music()
			enemy.life-=bullet.damage
			self.player.score+=enemy.check_death()
			if enemy.life<=0:
				if self.player.energy<5000:
					self.player.energy+=100
				enemy.not_collidable()

	# 					   player bullet and Trump                         #

	##check all player bullets and Trump
	# @para self
	def update_bullet_boss(self):
		if self.player.score!=0 and self.player.score%7800==0:
			self.Trump.show_up()
		self.Trump.move()
		self.c_boss_bullet(self.p_bullet0)
		self.c_boss_bullet(self.p_bullet1)
		self.c_boss_bullet(self.p_bullet2)
		self.c_boss_bullet(self.left_p_bullet0)
		self.c_boss_bullet(self.right_p_bullet0)
		self.c_boss_bullet(self.left_p_bullet1)
		self.c_boss_bullet(self.right_p_bullet1)
		self.c_boss_bullet(self.left_p_bullet2)
		self.c_boss_bullet(self.right_p_bullet2)

	##check one player bullets and Trump
	# @para self
	# @para bullet the bullet to be checked
	def c_boss_bullet(self, bullet):
		if self.collision(self.Trump, bullet):
			self.bgm.damage_music()
			self.Trump.life-=bullet.damage
			self.player.score+=self.Trump.check_death(TRUMP_LIFE, TRUMP_POINT)

	# 					   player bullet and Trump                         #

	##Check all player bullets and head
	# @para self
	def update_bullet_head(self):
		if self.player.score!=0 and self.player.score%3300==0:
			self.head.show_up()
		self.head.move()
		self.c_head_bullet(self.p_bullet0)
		self.c_head_bullet(self.p_bullet1)
		self.c_head_bullet(self.p_bullet2)
		self.c_head_bullet(self.left_p_bullet0)
		self.c_head_bullet(self.right_p_bullet0)
		self.c_head_bullet(self.left_p_bullet1)
		self.c_head_bullet(self.right_p_bullet1)
		self.c_head_bullet(self.left_p_bullet2)
		self.c_head_bullet(self.right_p_bullet2)

	##Check one player bullet and head
	# @para self
	# @para bullet the bullet to be checked
	def c_head_bullet(self, bullet):
		if self.collision(self.head, bullet):
			self.bgm.damage_music()
			self.head.life-=bullet.damage
			self.player.score+=self.head.check_death(HEAD_LIFE, HEAD_POINT)


	# 					   player plane and Trump                          #

	##Check player plane and Trump
	# @para self
	def update_player_boss(self):
		if self.collision(self.Trump, self.player):
			self.player.life=0

	# 					   player bullet and Trump                         #

	##check player plane and head
	# @para self
	def update_player_head(self):
		if self.collision(self.head, self.player):
			self.player.life=0

	# 					   player bullet and Trump                         #

	##check player plane and all enemy smart bullets
	# @para self
	def update_player_smt_bullet(self):
		self.c_player_smt_bullet(self.smart_bullet0, self.enemy0)
		self.c_player_smt_bullet(self.smart_bullet1, self.enemy1)
		self.c_player_smt_bullet(self.smart_bullet2, self.enemy2)
		self.c_player_smt_bullet(self.smart_bullet3, self.enemy3)
		self.c_player_smt_bullet(self.smart_bullet4, self.enemy4)
		self.c_player_smt_bullet(self.smart_bullet5, self.enemy5)

    ##check player and one enemy smart bullet
    # @para bullet the bullet tobe checked
    # @para enemy the enemy who owns the bullet, it gives the bullet 
    #             location when the bullet meets some conditions
	def c_player_smt_bullet(self, bullet, enemy):
		if enemy.y==-9:
			bullet.reset(enemy.x, enemy.y)
			bullet.state=1
			bullet.aim(self.player)
		if self.collision(bullet, self.player):
			self.player.life-=bullet.damage
			bullet.x=-1
			bullet.y=-1
			bullet.state=0

	# 					player plane and Trump's bullet                    #

	##check player and all boss bullet
	# @para self
	def update_player_bossbullet(self):
		self.c_player_bossbullet(self.boss_bullet0)
		self.c_player_bossbullet(self.boss_bullet1)
		self.c_player_bossbullet(self.boss_bullet2)
		self.c_player_bossbullet(self.boss_bullet3)
		self.c_player_bossbullet(self.boss_bullet4)

    ##check player and one boss bullet
    # @para self
    # @para bullet the bullet to be checked
	def c_player_bossbullet(self, bullet):
		if self.Trump.x==WIDTH//2-30:
			bullet.reset(self.Trump.x+30, self.Trump.y+30)
		if self.collision(bullet, self.player):
			self.player.life-=bullet.damage
			bullet.x=190
			bullet.y=250

    # 			        player and Trump's smart bullet                    #

    ##check Trump's smart bullet and player
    # @para self
	def update_player_boss_smartbullet(self):
		if self.Trump.x==WIDTH//2-30:
			self.boss_smart_bullet.reset(self.Trump.x+30, self.Trump.y+30)
			self.boss_smart_bullet.aim(self.player)
		if self.collision(self.boss_smart_bullet, self.player):
			self.bgm.damage_music()
			self.player.life-=self.boss_smart_bullet.damage
			self.boss_smart_bullet.x=190
			self.boss_smart_bullet.y=250
			self.player.power=False
			self.boss_smart_bullet.state=0

    # 					   player and head's bullet                        #

    ##check player and head's bullets
    # @para self
	def update_headbullet_player(self):
			self.c_headbullet_player(self.head_bullet0, WIDTH//2-15-35)#-18-17
			self.c_headbullet_player(self.head_bullet1, WIDTH//2-15-17)#-17
			self.c_headbullet_player(self.head_bullet2, WIDTH//2-15-1)#it should be 15 but head move 2 pixels
																	  # per frame so it is added by 1
			self.c_headbullet_player(self.head_bullet3, WIDTH//2-15+17)#17
			self.c_headbullet_player(self.head_bullet4, WIDTH//2-15+35)#18+17

    ##check player and one head's bullet
    # @para self
    # @para bullet the bullet to be checked
    # @para location the location where the bullet is shot
	def c_headbullet_player(self, bullet, position):
		if self.head.x==position:
			bullet.reset(self.head.x+15, self.head.y+15)
		if self.collision(bullet, self.player):
			self.player.life-=bullet.damage
			bullet.x=190
			bullet.y=250

    ########################################################################
    # 					              Draw                                 #
    ########################################################################

    ##Override the draw method.
	# @para self
	# the order of the draw_*** method are ordered, DO NOT change the order.
	def draw(self):
		if self.state==0:
			self.draw_startPage()
		if self.state==1:
			self.draw_gameBackground()
			self.draw_bullet()
			self.draw_enemy()
			self.draw_boss_bullet()
			self.draw_head_bullet()
			self.draw_gift()
			self.draw_smart_bullet()
			self.head.draw()
			self.Trump.draw()
			self.player.draw()
			self.draw_data()
		if self.player.life<=0 and self.state==1:
			self.state=-1
			self.draw_death()
			self.bgm.stop_music()
			self.bgm.end_music()

	##draw startpage
	# @para self
	def draw_startPage(self):
		self.draw_gameBackground()
		pp.text(62, 110, "Press \'SPACE\'", pp.frame_count % 15)

    ##draw game background
    # @para self
	def draw_gameBackground(self):
		pp.cls(0)
		pp.blt(0, 0, 0, 0, 0, 175, 245)

    ##draw gift
    # @para self
	def draw_gift(self):
		self.gift.draw()
		self.gift.move(self.player.score)

    ##draw enemy
    # @para self
	def draw_enemy(self):
		self.draw_one_enemy(self.enemy0)
		self.draw_one_enemy(self.enemy1)
		self.draw_one_enemy(self.enemy2)
		self.draw_one_enemy(self.enemy3)
		self.draw_one_enemy(self.enemy4)
		self.draw_one_enemy(self.enemy5)

	##draw one enemy
	# @para self
	def draw_one_enemy(self, enemy):
		enemy.draw()
		enemy.move()
	
	##this method is used to update the data, including score, HP, Ultra, once per frame.
	# @para self
	def draw_data(self):
		t=time()
		score='Score: {:04}'.format(self.player.score)
		energy=''
		if self.player.energy==5000:
			energy='ULTRA:     ' if round(10*t)%2==0 else 'ULTRA: {:02}%'.format(round(self.player.energy/50))
		else:
			energy='ULTRA: {:02}%'.format(round(self.player.energy/50))
		life= 'HP: {:04}'.format(self.player.life)
		data = score+'     '+energy+'      '+life
		pp.rect(0, 0, WIDTH, HEIGHT_DATA, COL_BACKGROUND_DATA)
		pp.text(1, 1, data, COL_DATA)

	##This method is used to draw one bullet.
	# This bullet must be player's bullet, and there are three of them.
	# This method is for method `draw_bullet`.
	# @para self
	# @para bullet the bullet that is going to be drew.
	def draw_one_bullet(self, bullet, y):
		bullet.draw()
		bullet.move(self.player.x+10, y)

	##This method is used to draw one left bullet and one right bullet.
	# This bullets must be player's, and there are six of them.
	# This method is for method `draw_bullet`.
	# @para self
	# @para bulletl the left bullet that is going to be drew.
	# @para bulletr the right bullet that is going to be drew.
	# @para y the y value where the bullet should go to.
	def draw_side_bullet(self, bulletl, bulletr, y):
		bulletl.draw(); bulletr.draw()
		bulletl.move(self.player.x,    y)
		bulletr.move(self.player.x+19, y)

	##draw player's bullets
	# @para self
	def draw_bullet(self):
		self.bgm.shoot_music()
		if not self.player.power:
			self.left_p_bullet0. out()
			self.right_p_bullet0.out()
			self.left_p_bullet1. out()
			self.right_p_bullet1.out()
			self.left_p_bullet2. out()
			self.right_p_bullet2.out()
			self.draw_one_bullet(self.p_bullet0, self.player.y)
			self.draw_one_bullet(self.p_bullet1, self.player.y-DISTANCE)
			self.draw_one_bullet(self.p_bullet2, self.player.y-DISTANCE*2)
		else:
			self.draw_side_bullet(self.left_p_bullet0, self.right_p_bullet0,
									self.player.y+13)
			self.draw_side_bullet(self.left_p_bullet1, self.right_p_bullet1,
									self.player.y+13-DISTANCE)
			self.draw_side_bullet(self.left_p_bullet2, self.right_p_bullet2,
									self.player.y+13-DISTANCE*2)
			self.p_bullet0.out()
			self.p_bullet1.out()
			self.p_bullet2.out()

    ##draw Trump's bullet
    # @para self
	def draw_boss_bullet(self):
		self.draw_one_boss_bullet(self.boss_bullet0)
		self.draw_one_boss_bullet(self.boss_bullet1)
		self.draw_one_boss_bullet(self.boss_bullet2)
		self.draw_one_boss_bullet(self.boss_bullet3)
		self.draw_one_boss_bullet(self.boss_bullet4)

    ##draw one Trump's bullet
    # @para self
    # @para bullet the bullet to be drew
	def draw_one_boss_bullet(self, bullet):
		bullet.draw(); bullet.move()

    ##draw all smart bullets
    # @para self
	def draw_smart_bullet(self):
		self.draw_one_smt_bullet(self.smart_bullet0)
		self.draw_one_smt_bullet(self.smart_bullet1)
		self.draw_one_smt_bullet(self.smart_bullet2)
		self.draw_one_smt_bullet(self.smart_bullet3)
		self.draw_one_smt_bullet(self.smart_bullet4)
		self.draw_one_smt_bullet(self.smart_bullet5)
		self.draw_one_smt_bullet(self.boss_smart_bullet)

	##draw one smart bullet
	# @para self
	# @para bullet the bullet to be drew.
	def draw_one_smt_bullet(self, bullet):
		bullet.draw(); bullet.move()

	##draw all head's bullets
	# @para self
	def draw_head_bullet(self):
		self.draw_one_smt_bullet(self.head_bullet0)
		self.draw_one_smt_bullet(self.head_bullet1)
		self.draw_one_smt_bullet(self.head_bullet2)
		self.draw_one_smt_bullet(self.head_bullet3)
		self.draw_one_smt_bullet(self.head_bullet4)

	##draw death page
	# @para self
	def draw_death(self):
		highScore=''
		with open('data/score.txt') as f:
			oldScore=int(f.readline())
			if self.player.score>oldScore:
				highScore+=str(self.player.score)
				with open('data/score.txt', 'r+') as f:
					f.writelines(highScore)
			else:
				highScore=int(oldScore)
		pp.cls(0)
		score='Score: {:04}'.format(self.player.score)
		pp.blt(76, 35, 1, 0, 0 if round(time()*10)%2==0 else 20, 20, 20, 0)
		pp.text(68, 65, "GAME OVER", COL_TEXT_DEATH)
		pp.text(60, 80, "--------------", COL_TEXT_DEATH)
		pp.text(65, 95, score, COL_TEXT_DEATH)
		pp.text(66, 110, "BEST: {:04}".format(int(highScore)), COL_TEXT_DEATH)
		pp.text(73, 125, "(R)ESET", COL_TEXT_DEATH)
		pp.text(74, 140, "(Q)UIT", COL_TEXT_DEATH)

if __name__ == "__main__":
	g=Game()






