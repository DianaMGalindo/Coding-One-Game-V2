import pygame

class TileSpecs(pygame.sprite.Sprite): # sub class of Sprite pygame, so that they can be added to a sprite group.
	def __init__(self, size, x ,y):
		super().__init__()

		self.image = pygame.Surface((size, size)) #size of the tile = 64
		self.rect = self.image.get_rect(topleft= (x,y))

	def update(self, screen_shift):
		self.rect.x += screen_shift


class StaticTile(TileSpecs):
	
	def __init__(self, size, x, y, surface):
		super().__init__(size,x,y)
		self.image = surface		