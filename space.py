import pygame
from pygame.locals import *
import random

size = width, height = (1200, 800)

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Bore")
star_loc1 = random.randint(1, 1201)
star_loc2 = random.randint(1, 801)
star_loc3 = random.randint(1, 1001)
star_loc4 = random.randint(1, 501)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255),
            [star_loc1, star_loc2], 2, 5)
    pygame.draw.circle(screen, (225, 225, 225),
            [star_loc3, star_loc4], 2, 5)
    pygame.display.update()
    
