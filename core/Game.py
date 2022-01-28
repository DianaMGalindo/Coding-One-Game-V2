import pygame
import os
from pygame.locals import *
from pygame import mixer
from settings import *
from level import Level
from game_data import level_0
from welcome import Welcome
from finish import Finish, FinishTwo, GameOver
from points_interface import Interface
from support import get_project_root


class Game: 
 	def __init__(self):

 		#game attributes
 		self.max_level = 1
 		self.welcome = Welcome(0, self.max_level, screen, self.load_level)
 		self.game_status = 'welcome'

 		#points bars
 		self.bar_current_points_one = 0
 		self.bar_total_points_one = 8

 		self.bar_current_points_two = 0
 		self.bar_total_points_two = 8
        
        #points counter
 		self.count_points_player_one = 0
 		self.count_points_player_two = 0

 	#points interface 

 		self.points = Interface(screen)	

 	#loading level	
 	def load_level(self):	
 		self.level = Level(level_0, screen, self.load_finish, self.load_finish_two, self.points_count_one, self.points_count_two, self.load_game_over)
 		self.game_status = 'level'

 	#updating players points and bars
 	
 	def points_count_one(self, amount):
 		self.count_points_player_one += amount
 		self.bar_current_points_one += amount

 	def points_count_two(self, amount):
 		self.count_points_player_two += amount
 		self.bar_current_points_two += amount	


 	#loading welcome screen 	
 	def load_welcome(self):
 		self.welcome = Welcome(0, self.max_level, screen, self.load_level)
 		self.game_status = 'welcome' #checking in which stage of the game I am in

 	#loadinf finish screen 	
 	def load_finish(self):
 		self.finish = Finish(screen, self.load_level)
 		self.game_status = 'finish'
                
    


 	def load_finish_two(self):
 		self.finish = FinishTwo(screen, self.load_level)
 		self.game_status = 'finish'

 		#Restarting points count
 		self.count_points_player_one = 0
 		self.count_points_player_two = 0
 		self.bar_current_points_one = 0
 		self.bar_total_points_one = 8

 		self.bar_current_points_two = 0
 		self.bar_total_points_two = 8
	

 	def load_game_over(self):
 		self.finish = GameOver(screen, self.load_level)	
 		self.game_status = 'finish'
 		self.count_points_player_one = 0
 		self.count_points_player_two = 0
 		self.bar_current_points_one = 0
 		self.bar_total_points_one = 8

 		self.bar_current_points_two = 0
 		self.bar_total_points_two = 8
	

 	#run conditions 	
 	def run(self):
 		if self.game_status == 'welcome':
 			self.welcome.run()

 		elif self.game_status == 'finish':
 			self.finish.run()

 		else:
 			self.level.run()
 			self.points.show_bar_one(self.bar_current_points_one, self.bar_total_points_one )
 			self.points.show_bar_two(self.bar_current_points_two, self.bar_total_points_two )
 			self.points.show_points(self.count_points_player_one, self.count_points_player_two)

 			

pygame.init()
pygame.mixer.init()

#PYGAME WINDOW SETUP
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Metaverse')


mixer.music.load(os.path.join(get_project_root() ,'sounds/call-to-adventure-by-kevin-macleod-from-filmmusic-io_lower.wav'))
mixer.music.set_volume(0.12)
mixer.music.play(-1)# adding -1 to play sound in loop 

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


