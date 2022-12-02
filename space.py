import pygame
from pygame.locals import *
import random


def main():
	size = width, height = (1200, 800)

	pygame.init()
	running = True
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Space Bore")
	keys = pygame.key.get_pressed()

	ship = pygame.image.load("ship.png")
	rock = pygame.image.load("rock.png")
	bg_img = pygame.image.load("space.jpg")
	
	rock_loc = rock.get_rect()
	# rock_loc.center = width / 2, height * -1
	first_col = width / 4 + random.randint(0,300)
	second_col = width / 4 + random.randint(301,600)
	third_col = width / 4 + random.randint(601,900)
	fourth_col = width / 4 + random.randint(901,1200)
	
	ship_loc = ship.get_rect()
	ship_loc.center = width / 2, height * 0.8
	
	pygame.display.update()

	counter = 0
	
	while running:
		rock_loc[1] += 1
		if rock_loc[1] > height:
			rock_loc[1] = -200
			coord = random.randint(0,4)
			if coord == 0:
				rock_loc.center = first_col, -200
			if coord == 1:
				rock_loc.center = second_col, -200
			if coord == 2:
				rock_loc.center = third_col, -200
			if coord == 3:
				rock_loc.center = fourth_col, -200
		
		# end game
		if rock_loc[0] == ship_loc[0] and rock_loc[1] > ship_loc[1] - 70:
			print("KABOOM!")
			break
				
		for event in pygame.event.get():
		    if event.type == QUIT:
		        running = False
		    if event.type == KEYDOWN:
		        if event.key in [K_a, K_LEFT]:
		            ship_loc[0] -= 20
		        if event.key in [K_d, K_RIGHT]:
		            ship_loc[0] += 20
		
		screen.blit(bg_img,(0,0))
		screen.blit(ship, ship_loc)
		screen.blit(rock, rock_loc)
		pygame.display.update()
	
	pygame.quit()
		
		
if __name__ == "__main__":
	main()
		



