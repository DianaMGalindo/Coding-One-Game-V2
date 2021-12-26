import pygame 
from support import import_csv_layout, import_sliced_img
from settings import tile_size, screen_range_upper, screen_range_lower
from tile_specs import TileSpecs, StaticTile, Trees, House, Door
from player import Players, PlayerOne, PlayerTwo



class Level: # main class
	def __init__(self, level_data, surface): #level_data will be a dictionary with all csv files from Tileset
		self.display_surface = surface 
		self.level_shift = 0

		#PLayer One

		player_one_layout = import_csv_layout(level_data['player-one'])
		self.player_one = pygame.sprite.GroupSingle()
		#self.goal  = pygame.sprite.GroupSingle() #should be door
		self.player_one_setup(player_one_layout	)

		#PLayer Two

		player_two_layout = import_csv_layout(level_data['player-two'])
		self.player_two = pygame.sprite.GroupSingle()
		#self.goal  = pygame.sprite.GroupSingle() #should be door
		self.player_two_setup(player_two_layout	)


		#Terrain setup
		#import csv data and grab the data from terrain key
		terrain_layout = import_csv_layout(level_data['terrain'])
		self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain') # especify the type of tile group being created

		#Props setup
		props_layout = import_csv_layout(level_data['props'])
		self.props_sprites = self.create_tile_group(props_layout, 'props')


		#Trees setup 
		trees_layout = import_csv_layout(level_data['trees'])
		self.trees_sprites = self.create_tile_group(trees_layout, 'trees')

		#Houses setup
		house_layout = import_csv_layout(level_data['house'])
		self.house_sprites = self.create_tile_group(house_layout, 'house')

		#Door setup

		door_layout = import_csv_layout(level_data['door'])
		self.door_sprites = self.create_tile_group(door_layout, 'door')

	
	#creating the 'camera' effect to be able to navigate the level
	def window_scroll(self):
		player_one_scroll = self.player_one.sprite
		player_two_scroll = self.player_two.sprite

		player_one_x = player_one_scroll.rect.centerx
		player_two_x = player_two_scroll.rect.centerx

		direction_x = player_one_scroll.direction.x	
		direction_x_two = player_two_scroll.direction.x	

		if player_one_x < screen_range_lower and direction_x  < 0:
			self.level_shift = 4
			player_one_scroll.speed = 0
			
		elif player_one_x  > screen_range_upper and direction_x  > 0:
			self.level_shift = -4
			player_one_scroll.speed = 0
			
		else: 
			if player_two_x < screen_range_lower and direction_x_two <0:
				self.level_shift = 4
				player_two_scroll.speed = 0
			elif player_two_x > screen_range_upper and direction_x_two > 0:
				self.level_shift = -4
				player_two_scroll.speed = 0	
			else:	
				self.level_shift = 0
				player_one_scroll.speed = 4
				player_two_scroll.speed = 4


	#creating function that will find 'x' and 'y' position of each tile.	
	def create_tile_group(self, level_layout, layout_type):
		sprite_group = pygame.sprite.Group() 

		for row_index, row in enumerate(level_layout): #index of each row will be 'y'
			for column_index, tile_value in enumerate(row): # looping through row to find 'x'
				if tile_value != '-1': 
					x_position = column_index * tile_size
					y_position = row_index * tile_size

					#importing the sliced tile set that will populate the layout
					if layout_type == "terrain":
						terrain_tile_list = import_sliced_img('../graphics/terrain/Terrain_V2.png') #sliced images
						
						#getting the value of every tile imported in terrain_tile_list
						tile_surface = terrain_tile_list[int(tile_value)]
						sprite = StaticTile(tile_size, x_position, y_position, tile_surface)
						#sprite_group.add(sprite) # Adding individual sprites to group of sprites

					if layout_type == 'props':
						props_tile_list = import_sliced_img('../graphics/props/props.png')	
						tile_surface = props_tile_list[int(tile_value)]
						sprite = StaticTile(tile_size, x_position, y_position, tile_surface)

					if layout_type == 'trees':
						if tile_value == '0' :
								sprite = Trees(tile_size, x_position, y_position,'../graphics/trees/Tree_left.png', offset_y = True)
						if tile_value == '1':
								sprite = Trees(tile_size, x_position, y_position,'../graphics/trees/Tree_right.png', offset_y = True)

					if layout_type == 'house':
						sprite = House(tile_size, x_position, y_position,'../graphics/house/house.png', offset_y = True)

					if layout_type == 'door':
						sprite = Door(tile_size, x_position, y_position,'../graphics/door/door.png', offset_y = True )		

					sprite_group.add(sprite) 

		return sprite_group


	def horizontal_collision(self):
		player_1 = self.player_one.sprite 
		player_2 = self.player_two.sprite 
		player_1.rect.x += player_1.direction.x * player_1.speed
		player_2.rect.x += player_2.direction.x * player_2.speed

		for sprite in self.terrain_sprites.sprites():

			if sprite.rect.colliderect(player_1.rect):
				if player_1.direction.x < 0: #checking if the player is moving to the left
					player_1.rect.left = sprite.rect.right
				elif player_1.direction.x >0:
					player_1.rect.right = sprite.rect.left

			if sprite.rect.colliderect(player_2.rect):
				if player_2.direction.x <0:
					player_2.rect.left = sprite.rect.right
				elif player_2.direction.x > 0: # player moving to the right
					player_2.rect.right = sprite.rect.left			


	def vertical_collision(self):
		player_1 = self.player_one.sprite 
		player_2 = self.player_two.sprite
		#and self.player_two.sprite	
		player_1.gravity_applied()
		player_2.gravity_applied()

		for sprite in self.terrain_sprites.sprites():

		#PLAYER ONE
			if sprite.rect.colliderect(player_1.rect):
				if player_1.direction.y < 0: #player moving up
					player_1.rect.top = sprite.rect.bottom
					player_1.direction.y = 0
					player_1.player_on_roof = True # player collides with the roof

				elif player_1.direction.y > 0:	#player moving down
					player_1.rect.bottom = sprite.rect.top
					player_1.direction.y = 0
					player_1.player_on_ground = True # player collides with the ground


		#PLAYER TWO		 			
			if sprite.rect.colliderect(player_2.rect):
				if player_2.direction.y < 0: #player moving up
					player_2.rect.top = sprite.rect.bottom
					player_2.direction.y = 0
					player_2.player_on_roof = True # player collides with the roof

				elif player_2.direction.y > 0:	#player moving down
					player_2.rect.bottom = sprite.rect.top
					player_2.direction.y = 0
					player_2.player_on_ground = True # player collides with the ground	


		#checking if the player is on the ceiling	
		if player_1.player_on_roof and player_1.direction.y > 0: #player is falling 
			player_1.player_on_roof = False	 

		#checking if the player is on the ground 		
		if player_1.player_on_ground and player_1.direction.y < 0 or player_1.direction.y >1:
			player_1.player_on_ground = False # the player is jumping or falling

		 #checking if the player is on the ceiling	
		if player_2.player_on_roof and player_2.direction.y > 0: #player is falling 
			player_2.player_on_roof = False	 

		#checking if the player is on the ground 		
		if player_2.player_on_ground and player_2.direction.y < 0 or player_2.direction.y >1:
			player_2.player_on_ground = False # the player is jumping or falling

														

	def player_one_setup(self, layout):
		for row_index, row in enumerate(layout):
			for column_index, tile_value in enumerate(row):
				x_position = column_index * tile_size
				y_position = row_index * tile_size

				if tile_value == '0':
					sprite = PlayerOne(x_position, y_position)
					self.player_one.add(sprite)
				if tile_value == '1':
						print('door goes here')	

	def player_two_setup(self, layout):
		for row_index, row in enumerate(layout):
			for column_index, tile_value in enumerate(row):
				x_position = column_index * tile_size
				y_position = row_index * tile_size

				if tile_value == '0':
					sprite = PlayerTwo(x_position, y_position)
					self.player_two.add(sprite)
				if tile_value == '1':
						print('door goes here')						



	def run(self): #method to run the level


		#terrain
		self.terrain_sprites.draw(self.display_surface) #drawing the terrain. draw(surface to draw)
		self.terrain_sprites.update(self.level_shift)# moving the screen to see all level	

		#props
		self.props_sprites.draw(self.display_surface)
		self.props_sprites.update(self.level_shift)

		#trees
		self.trees_sprites.draw(self.display_surface)
		self.trees_sprites.update(self.level_shift)

		#house 
		self.house_sprites.draw(self.display_surface)
		self.house_sprites.update(self.level_shift)

		#door
		self.door_sprites.draw(self.display_surface)
		self.door_sprites.update(self.level_shift)

		self.window_scroll()

		#Players

		self.player_one.draw(self.display_surface)
		self.player_two.draw(self.display_surface)
		self.player_one.update()
		self.player_two.update()
		self.horizontal_collision()
		self.vertical_collision()
		
		

	
		


        
