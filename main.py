import pygame
from pygame.locals import *


size = width, height = (1200, 800)
road_w = int(width/1.6) # To get about 500 pixel
roadmark_w = int(width/80)


pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mike's Car Game")
screen.fill((60, 220, 0))
pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))

pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2-roadmark_w/2, 0, roadmark_w, height))

pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2-road_w/2 + roadmark_w*2, 0, roadmark_w, height)) 

pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


pygame.quit()
