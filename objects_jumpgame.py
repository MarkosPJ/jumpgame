import random

class Player():
	def __init__(self,y_pos,y_vel):
		self.y_pos = y_pos
		self.y_vel = y_vel

	def move(self):
		"Calculate position of player on next frame."

		#move in direction
		self.y_pos -= self.y_vel

		
		if not self.isOnFloor():
			#gravity
			self.y_vel -= 2
		else:
			self.y_vel = 0
			self.y_pos = 0


	def jump(self):
		"Initiates jump of player."
        
		self.y_vel = 20

	def isOnFloor(self):
		return self.y_pos >= 0

class Hints():
        height = 50
        width = 10
        initial = [800, 950, 1100, 1150]
        def __init__(self):
                self.x_pos = random.choice(self.
                                           initial)
                self.x_vel = 10
                # Kann man auch verallgemeinern.

        def approach(self):
                "Calculate position of hint on next frame."
                self.x_pos -= self.x_vel
                if self.isGone():
                        self.x_pos = random.choice(self.initial)

        def isGone(self):
                return self.x_pos <= 0


"""
"test"
player = Player(0,0)
player.jump()

for i in range(25):
	player.move()

	print(int(player.y_pos)*"#")
"""

