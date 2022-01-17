import pygame 

class Welcome:
	def __init__(self, start_level, max_level, surface, load_level):

		self.display_surface = surface
		self.max_level = max_level
		self.start_level = start_level
		self.load_level = load_level


	def input(self):
		keys = pygame.key.get_pressed()	

		if keys[pygame.K_SPACE]:
			self.load_level()

	def background(self):
		self.screen_background = pygame.image.load('../graphics/background/Welcome_Screen.jpg')
		self.display_surface.blit(self.screen_background,(0,0))		


	def run(self):
		self.input()
		self.background()	