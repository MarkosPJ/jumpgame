class Player():
	def __init__(self,y_pos,y_vel):
		self.y_pos = y_pos
		self.y_vel = y_vel

	def move(self):
		"Calculate position of player on next frame."

		#move in direction
		self.y_pos += self.y_vel

		
		if not self.isOnFloor():
			#gravity
			self.y_vel -= 0.5
		else:
			self.y_vel = 0
			self.y_pos = 0


	def jump(self):
		"Initiates jump of player."

		self.y_vel = 5

	def isOnFloor(self):
		return self.y_pos <= 0



"test"
player = Player(0,0)
player.jump()

for i in range(25):
	player.move()

	print(int(player.y_pos)*"#")