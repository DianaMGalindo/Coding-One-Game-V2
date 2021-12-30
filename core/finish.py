import pygame 

class Finish:
	def __init__(self, surface):
		self.display_surface = surface.fill('black')


	def input(self):
		keys = pygame.key.get_pressed()	

		if keys[pygame.K_SPACE]:
			print('game over')

	def run(self):
		self.input()	