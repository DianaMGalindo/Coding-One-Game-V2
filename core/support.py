from csv import reader #allow the reading of csv files

def import_csv_layout(path): #path will pass the csv file
	terrain_map = []
	with open(path) as map:
		level = reader(map, delimiter = ',') #delimiter refers to how each individual point of data is separated. csv will separate with commas.

		for row in level: #for every row in the csv
			terrain_map.append(list(row)) #store every row in a single list
		return terrain_map 	