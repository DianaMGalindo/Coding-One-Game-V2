import pygame
from pygame.locals import *
from settings import *
from level import Level
from game_data import level_0


pygame.init()

#PYGAME WINDOW SETUP

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Metaverse')
level = Level(level_0, screen)
 #connecting with my main class Level
#ADDING IMAGES

background = pygame.image.load('Images/Initial_background.jpg')


#CREATING GAME LOOP (Running condition)
run = True
while run:
    
    #adding images within the game loop 
	screen.blit(background, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	level.run()		
	pygame.display.update()		
pygame.quit()			


