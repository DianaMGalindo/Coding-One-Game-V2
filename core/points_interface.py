import pygame

class Interface: 
	def __init__(self, surface):
		self.display_surface = surface

		#points bar 
		self.points_bar_one = pygame.image.load('../graphics/points_bar/player_one_bar.png').convert_alpha()
		self.points_bar_two = pygame.image.load('../graphics/points_bar/player_two_bar.png').convert_alpha()

		self.bar_one_top_left = (116, 79)
		self.bar_two_top_left = (306, 79)

		self.bar_max_width = 68
		self.bar_height = 3

		#live text
		self.text = pygame.font.Font('../graphics/points_bar/Hexadecimal.otf', 16)

	#method to display points bar	
	def	show_bar_one(self, current, full):

		self.display_surface.blit(self.points_bar_one, (45, 45))
        
        #finding the amount of pixels on screen equivalet to the total amount of points 
		points_pixel_ratio = self.bar_max_width * current / full
		points_rect = pygame.Rect((self.bar_one_top_left), (points_pixel_ratio, self.bar_height))

		pygame.draw.rect(self.display_surface, '#1d1838', points_rect)

	def show_bar_two(self, current, full):
		self.display_surface.blit(self.points_bar_two, (235, 45))

        #finding the amount of pixels on screen equivalet to the total amount of points 
		points_pixel_ratio = self.bar_max_width * current / full
		points_rect = pygame.Rect((self.bar_two_top_left), (points_pixel_ratio, self.bar_height))

		pygame.draw.rect(self.display_surface, '#1d1838', points_rect)


	#method to display number of points

	def show_points (self, amount_one, amount_two):
		point_amount_one = self.text.render(str(amount_one), False, '#ebcb85')
		self.display_surface.blit(point_amount_one,(100, 64))

		point_amount_two = self.text.render(str(amount_two), False, '#1d1838')
		self.display_surface.blit(point_amount_two, (292, 64))