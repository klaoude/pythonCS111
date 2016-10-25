from Window import *

NUM_CASE_X = 100
NUM_CASE_Y = 100
CASE_SIZE = 10

class MainGame:
	def __init__(self):
		self.window = Window(NUM_CASE_X, NUM_CASE_Y, CASE_SIZE)
		self.map = []
		for i in range(0, NUM_CASE_X):
			self.map.append([])
			for j in range(0, NUM_CASE_Y):
				self.map[i].append(0)
				self.window.createRect(i, j, 0)

	def lodaFromFile(self, files):
		f = open(files)
		i = 0
		j = 0
		for l in f:
			for c in l:
				if(not(c == '\n')):
					self.map[i][j] = int(c)
					j+=1
			i+=1
			j=0

	def toggle(self, x, y):
		self.map[x][y] = not self.map[x][y]

	def editMode(self):
		c = True
		while c:
			for e in pygame.event.get():
				if(e.type == pygame.MOUSEBUTTONUP):
					x = pygame.mouse.get_pos()[0]//CASE_SIZE
					y = pygame.mouse.get_pos()[1]//CASE_SIZE
					self.toggle(x, y)
					a = self.map[x][y]
					self.window.createRect(x, y, a)
					self.window.flip()
				if(e.type == pygame.KEYDOWN and e.key == pygame.K_a):
					c = False

	def print(self):
		for i in range(0, len(self.map)):
			print(self.map[i])
			for j in range(0, NUM_CASE_Y):
				self.window.createRect(i, j, self.map[i][j])
		self.window.flip()

	def set(self, x, y, a):
		if(not a == 0 or not a == 1):
			return False
		self.map[x][y] = a
		return True

	def aliveNextTurn(self, x, y):
		numAlive = 0
		wasAlive = self.map[x][y]
		for j in range(y-1, y+2):
			for i in range(x-1, x+2):
				if(i >= 0 and j >= 0):
					if(i < NUM_CASE_X-1 and y < NUM_CASE_Y-1):
						if(self.map[i][j] == 1):
							if(not (x==i and y==j)):
								numAlive+=1
		if(wasAlive and numAlive < 2):
			return 0
		if(wasAlive and (2 <= numAlive <= 3)):
			return 1
		if(wasAlive and numAlive > 3):
			return 0
		if(not wasAlive and numAlive == 3):
			return 1
		return wasAlive

	def turn(self, nbTurn = 1):
		newMap = []
		for i in range(0, NUM_CASE_X):
			newMap.append([])
			for j in range(0, NUM_CASE_Y):
				newMap[i].append(0)
		for i in range(0, NUM_CASE_X):
			for j in range(0, NUM_CASE_Y):
				newMap[i][j] = self.aliveNextTurn(i, j)
		self.map = newMap
