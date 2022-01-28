import pygame
import os
from support import import_sprites_folder
from support import get_project_root


class Players(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__() 
		self.image = pygame.Surface((32,64))
		self.import_player_assets()
		self.image.fill('white')
		self.rect = self.image.get_rect(topleft= (x,y))

		#players movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 4
		self.gravity = 0.8
		self.jump_speed = -16

		#players animation 
		self.frame_index = 0
		self.animation_speed = 0.15	

		#player default

		self.status = 'idle'
		self.face_right = True
		self.player_on_ground = False
		self.player_on_roof = False
		self.player_on_right = False
		self.player_on_left = False

	#player collision
	def gravity_applied(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y	#modifying the y value of the vector

	def jump(self):
		self.direction.y = self.jump_speed

	def update(self):
		self.rect.x += self.direction.x * self.speed

	#animating character 	
	def animate(self):
		animation = self.animations[self.status]

		#creating a loop over frame index (every image within the folder)
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		animated_image = animation[int(self.frame_index)]
			
		if self.face_right == True:
			self.image = animated_image
		else:
			flip = pygame.transform.flip(animated_image, True, False) # (img, horizontal, vertical)
			self.image = flip


		#checking the animation collision status of the character and re-set origin point of rect
		if self.player_on_ground: 
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

		elif self.player_on_ground and self.player_on_left:
			self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)

		elif self.player_on_ground and self.player_on_right:
			self.rect = self.image.get_rect(bottomright = self.rect.bottomright)	

	
		#checking the animation collision status of the character and re-set origin point of rect
		elif self.player_on_roof:
			self.rect = self.image.get_rect(midtop = self.rect.midtop)

		elif self.player_on_roof and self.player_on_left:
			self.rect = self.image.get_rect(topleft = self.rect.topleft)

		elif self.player_on_roof and self.player_on_right:
			self.rect = self.image.get_rect(topright = self.rect.topright)



	def character_status(self):
		if self.direction.y < 0:
			self.status = 'jump'
		elif self.direction.y > 1: # y will never be a constant 0, so the player would look like constantly falling if the value is ;eft to 0 
			self.status = 'fall'
		else:
			if self.direction.x != 0:
				self.status = 'run'		
			else:
				self.status = 'idle'	
								


class PlayerOne(Players):
	def __init__(self, x, y):
		super().__init__(x, y)
		#self.image = self.animations['idle'][self.frame_index]

	#setting up keyboard	
	def keys_setup_one(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1 #modifying the x value of the vector 
			self.face_right = True
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.face_right = False
		else:
			self.direction.x = 0

		if keys[pygame.K_UP] and self.player_on_ground:
			self.jump()	

	#Import character one images	
	def import_player_assets(self):
		character_one_path = os.path.join(get_project_root(),'graphics/character_one/')
		self.animations = {'idle': [], 'jump': [], 'fall': [], 'run': []}

		for animation in self.animations.keys():
			full_path_one = character_one_path + animation
			self.animations[animation] = import_sprites_folder(full_path_one)			

	def update(self):
		self.keys_setup_one()
		self.character_status()
		self.animate()
		

class PlayerTwo(Players):
	def __init__(self, x, y):
		super().__init__(x, y)
		#self.image = self.animations['idle'][1]
		

	def keys_setup_two(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_d]:
			self.direction.x = 1
			self.face_right = True
		elif keys[pygame.K_a]:
			self.direction.x = -1
			self.face_right = False
		else:
			self.direction.x = 0

		if keys[pygame.K_w] and self.player_on_ground:
			self.jump()	

	#Import character two images	
	def import_player_assets(self):
		character_two_path = os.path.join(get_project_root(),'graphics/character_two/')
		self.animations = {'idle': [], 'jump': [], 'fall': [], 'run': []}

		for animation in self.animations.keys():
			full_path_two = character_two_path + animation
			self.animations[animation] = import_sprites_folder(full_path_two)						

	def update(self):
	 	self.keys_setup_two()
	 	self.character_status()
	 	self.animate()
	
