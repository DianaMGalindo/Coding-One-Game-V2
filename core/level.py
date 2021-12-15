import pygame 
from support import import_csv_layout


class Level: # main class
	def __init__(self, level_data, surface): #level_data will be a dictionary with all csv files from Tileset
		self.display_surface = surface 

		#import csv data and grab the data from terrain key
		terrain_layout = import_csv_layout(level_data['terrain'])
		print(terrain_layout)

	def run(self): #methos to run the level  	
		pass