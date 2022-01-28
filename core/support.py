import pygame
from csv import reader #allow the reading of csv files
from settings import tile_size
from os import walk #go through file system. It will return directory path, directory names (folders within the folder), filenames
from pathlib import Path 


def import_csv_layout(path): #path will pass the csv file
	terrain_map = []
	with open(path) as map:
		level = reader(map, delimiter = ',') #delimiter refers to how each individual point of data is separated. csv will separate with commas.

		for row in level: #for every row in the csv
			terrain_map.append(list(row)) #store every row in a single list
		return terrain_map 	

def import_sliced_img(path): #path will load the img file
	surface = pygame.image.load(path).convert_alpha() #image containing transparency
	slice_x = int(surface.get_size()[0] / tile_size) #get size will return a tuple, 0 index being width
	slice_y = int(surface.get_size()[1] / tile_size) # 1 index being height 

	sliced_tiles = []
	#Slicing the tile surface
	for row in range(slice_y):	
		for column in range(slice_x):
			x = column * tile_size
			y = row * tile_size
			new_surface = pygame.Surface((tile_size,tile_size), flags = pygame.SRCALPHA)# SRCALPHA will convert all unused pixels to transparent 
			new_surface.blit(surface,(0,0), pygame.Rect(x,y,tile_size, tile_size))

			sliced_tiles.append(new_surface)	

	return sliced_tiles	

def import_sprites_folder(path): 
	surface_list = []

	for _, __, images in walk(path):
		for image in images:
			full_path = path + '/' + image
			sprites_surface = pygame.image.load(full_path).convert_alpha()
			surface_list.append(sprites_surface)

	return surface_list
		

#Normalizing paths

def get_project_root() -> Path:
	return Path(__file__).parent.parent



