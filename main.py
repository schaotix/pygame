import pygame
from pygame.locals import *


size = width, height = (800, 800)
road_w = int(width/1.6) # To get about 500 pixels

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mike's Car Game")
screen.fill((60, 220, 0))
pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


pygame.quit()
