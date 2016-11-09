import pygame

class Button:
	def __init__(self, surface, x, y, w, h, color):
		self.surface = surface
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color
	
	def update(self):
		pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.w, self.h))
		pygame.display.update()

class Window:
	def __init__(self, x, y, size):
		pygame.init()
		self.size = size
		self.window = pygame.display.set_mode((x*size, y*size+100))
		buttonSurf = pygame.Surface((0, 100))
		buttonSurf.fill(pygame.Color(75, 75, 75, 255))
		self.window.blit(buttonSurf, (0, 0))
		pygame.display.flip()
		self.b1 = Button(self.window, 100, 100, 100, 10, pygame.Color(255, 0, 255, 255))
		self.b1.update()

	def createRect(self, x, y, black = False):
		Rect = pygame.Rect(x*self.size, y*self.size, self.size, self.size)
		surface = pygame.Surface((self.size, self.size))
		surface.fill(pygame.Color(0, 0, 0, 255)) if black else surface.fill(pygame.Color(255, 255, 255, 255))
		self.window.blit(surface, (x*self.size, y*self.size))

	def flip(self):
		pygame.display.flip()
		self.b1.update()
