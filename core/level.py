import pygame 
from support import import_csv_layout, import_sliced_img
from settings import tile_size
from tile_specs import TileSpecs, StaticTile, trees


class Level: # main class
	def __init__(self, level_data, surface): #level_data will be a dictionary with all csv files from Tileset
		self.display_surface = surface 
		self.level_shift = -4 

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
						sprite = trees(tile_size, x_position, y_position)

					sprite_group.add(sprite) 

		return sprite_group	

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
