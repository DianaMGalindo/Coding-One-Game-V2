import pygame
from pygame import mixer
from os import walk
from support import import_sprites_folder

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

class AnimatedTiles(TileSpecs):
	def __init__(self, size, x, y, path):
		super().__init__(size,x,y)

		self.frames = import_sprites_folder(path)
		self.frame_index = 0
		self.animation_speed = 0.13	
		self.image = self.frames[self.frame_index]

		#overwriting the position of the tile
		offset_y = size + y 
		self.rect = self.image.get_rect(bottomleft= (x, offset_y))


	def animate(self):	

		#creating a loop over frame index (every image within the folder)
		self.frame_index += self.animation_speed

		if self.frame_index >= len(self.frames):
			self.frame_index = 0

		self.image = self.frames[int(self.frame_index)]


	def update(self, screen_shift):
		self.animate()
		self.rect.x += screen_shift


class Edibles(AnimatedTiles):
	def __init__ (self, size, x, y, path, value_one, value_two):
		super().__init__(size,x,y,path)	

		self.value_one = value_one
		self.value_two = value_two


	def player_one_value(self):
		 
		self.value_one = value_one

		# if value_one == 1:
		# 	yummy_sound = mixer.Sound('../sounds/yummy.ogg')
		# 	yummy_sound.play()


	def player_two_value(self):
		self.value_two = value_two
			

class Trees(StaticTile):

	def __init__(self, size, x, y, path, offset_y):
		super().__init__(size, x, y, pygame.image.load(path).convert_alpha(), offset_y)
		
class House(StaticTile):

	def __init__(self, size, x, y, path, offset_y):
		super().__init__(size, x, y, pygame.image.load(path).convert_alpha(), offset_y)		

class Door(StaticTile):
	def __init__(self, size, x, y, path, offset_y):	
		super().__init__(size, x, y, pygame.image.load(path).convert_alpha(), offset_y)

class Background(StaticTile):
	def __init__(self, size, x, y, path, offset_y):
		super().__init__(size, x, y, pygame.image.load(path).convert_alpha(), offset_y)		