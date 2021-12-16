import pygame

class TileSpecs(pygame.sprite.Sprite):
	def __init__(self, size, x ,y):
		super().__init__()

		self.image = pygame.Surface((size, size)) #size of the tile = 64
		self.image.fill('grey')
		self.rect = self.image.get_rect(topleft= (x,y))

	def update(self, screen_shift):
		self.rect.x += screen_shift