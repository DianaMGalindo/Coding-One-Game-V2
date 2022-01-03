import pygame
from pygame.locals import *
from settings import *
from level import Level
from game_data import level_0
from welcome import Welcome
from finish import Finish
from points_interface import Interface


class Game: 
 	def __init__(self):

 		#game attributes
 		self.max_level = 1
 		self.welcome = Welcome(0, self.max_level, screen, self.load_level)
 		self.game_status = 'welcome'

 		#points bar
 		self.bar_current_points_one = 10
 		self.bar_total_points_one = 100

 		self.bar_current_points_two = 20
 		self.bar_total_points_two = 100
        
        #points counter
 		self.count_points_player_one = 0
 		self.count_points_player_two = 1

 	#points interface 

 		self.points = Interface(screen)	

 	#loading level	
 	def load_level(self):	
 		self.level = Level(level_0, screen, self.load_finish, self.points_count_one, self.points_count_two)
 		self.game_status = 'level'

 	#updating players points
 	
 	def points_count_one(self, amount):
 		self.count_points_player_one += amount

 	def points_count_two(self, amount):
 		self.count_points_player_two += amount	



 	#loading welcome screen 	
 	def load_welcome(self):
 		self.welcome = Welcome(0, self.max_level, screen, self.load_level)
 		self.game_status = 'welcome' #checking in which stage of the game I am in

 	#loadinf finish screen 	
 	def load_finish(self):
 		self.finish = Finish(screen)
 		self.game_status = 'finish'	

 	#run conditions 	
 	def run(self):
 		if self.game_status == 'welcome':
 			self.welcome.run()
 		elif self.game_status == 'finish':
 			self.finish.run()		
 		else:
 			self.level.run()
 			self.points.show_bar_one( self.bar_current_points_one, self.bar_total_points_one )
 			self.points.show_bar_two( self.bar_current_points_two, self.bar_total_points_two )
 			self.points.show_points(self.count_points_player_one, self.count_points_player_two)

 			


pygame.init()

#PYGAME WINDOW SETUP
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Metaverse')

 #connecting with my main class Level


#Instances of my main classes
#level = Level(level_0, screen)
game = Game()

#CREATING GAME LOOP (Running condition)
run = True
while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	#adding images within the game loop 		
	#screen.fill('grey')		

	#level.run()	
	game.run()
	pygame.display.update()
	clock.tick(60)		
pygame.quit()			


