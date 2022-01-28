import pygame 
from support import get_project_root
import os 

class Finish:
	def __init__(self, surface, load_level):
		self.display_surface = surface
		# self.display_surface = surface.fill('black')


	def input(self):
		keys = pygame.key.get_pressed()	

		if keys[pygame.K_q]:
			pygame.quit()	

	def background(self):
		self.screen_background = pygame.image.load(os.path.join(get_project_root(),'graphics/background/Win_Screen_PlayerOne_v2.jpg'))
		self.display_surface.blit(self.screen_background,(0,0))

						
	def run(self):
		self.input()
		self.background()


class FinishTwo(Finish):
	def __init__(self,surface, load_level):
		super().__init__(surface, load_level)
		self.display_surface = surface
		self.load_level = load_level

	def backgroud_win_two(self):
		self.screen_background = pygame.image.load(os.path.join(get_project_root(),'graphics/background/Win_Screen_PlayerTwo_v2.jpg'))
		self.display_surface.blit(self.screen_background,(0,0))	

	def input(self):
		keys = pygame.key.get_pressed()	

		if keys[pygame.K_SPACE]:
			self.load_level()	

	def run(self):
		self.input()
		self.backgroud_win_two()

class GameOver(Finish):
	
	def __init__(self,surface, load_level):
		super().__init__(surface, load_level)
		self.display_surface = surface
		self.load_level = load_level		

	def game_over(self):
		self.screen_background = pygame.image.load(os.path.join(get_project_root(),'graphics/background/Game_Over_v2.jpg'))
		self.display_surface.blit(self.screen_background,(0,0))	

	def input(self):
		keys = pygame.key.get_pressed()	

		if keys[pygame.K_SPACE]:
			self.load_level()

		if keys[pygame.K_q]:
			pygame.quit()		

	def run(self):
		self.input()
		self.game_over()	

