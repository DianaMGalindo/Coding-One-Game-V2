import pygame

class TileSpecs(pygame.sprite.Sprite): # sub class of Sprite pygame, so that they can be added to a sprite group.
	def __init__(self, size, x ,y):
		super().__init__()

		self.image = pygame.Surface((size, size)) #size of the tile = 64
		self.rect = self.image.get_rect(topleft= (x,y))


	def update(self, screen_shift):
		self.rect.x += screen_shift


class StaticTile(TileSpecs):
	
	def __init__(self, size, x, y, surface, offset_y = False):
		super().__init__(size,x,y)
		self.image = surface

		if offset_y	== True:
			offset_y = size + y 
			self.rect = self.image.get_rect(bottomleft=(x, offset_y))

class Trees(StaticTile):

	def __init__(self, size, x, y, path, offset_y):
		super().__init__(size, x, y, pygame.image.load(path).convert_alpha(), offset_y)
		
class House(StaticTile):

	def __init__(self, size, x, y, path, offset_y):
		super().__init__(size, x, y, pygame.image.load(path).convert_alpha(), offset_y)		

class Door(StaticTile):
	def __init__(self, size, x, y, path, offset_y):	
		super().__init__(size, x, y, pygame.image.load(path).convert_alpha(), offset_y)
		