import pygame 

class Welcome:
	def __init__(self, start_level, max_level, surface, load_level):

		self.display_surface = surface.fill('grey')
		self.max_level = max_level
		self.start_level = start_level
		self.load_level = load_level


	def input(self):
		keys = pygame.key.get_pressed()	

		if keys[pygame.K_SPACE]:
			self.load_level()


	def run(self):
		self.input()	