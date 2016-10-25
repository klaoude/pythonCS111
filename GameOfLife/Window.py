import pygame

class Window:
	def __init__(self, x, y, size):
		pygame.init()
		self.size = size
		self.window = pygame.display.set_mode((x*size, y*size))

	def createRect(self, x, y, black = False):
		Rect = pygame.Rect(x*self.size, y*self.size, self.size, self.size)
		surface = pygame.Surface((self.size, self.size))
		surface.fill(pygame.Color(0, 0, 0, 255)) if black else surface.fill(pygame.Color(255, 255, 255, 255))
		self.window.blit(surface, (x*self.size, y*self.size))

	def flip(self):
		pygame.display.flip()
