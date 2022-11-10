import pygame
import sys
import time

pygame.init()

water_image = pygame.image.load('images/water_image.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
pygame.display.set_caption("Water Game")
screen.fill((0, 0, 255))

screen_rect = screen.get_rect()

rows = screen_rect.height/tile_size
columns = screen_rect.width/tile_size

for x in range(int(rows)):
    for y in range(int(columns)):
        screen.blit(water_image, (x*water_rect.width, y*water_rect.height))


pygame.display.flip()

while True:
    recent_events = pygame.event.get()
    for event in recent_events:
        if event.type == pygame.QUIT:
            screen.fill((255, 0, 0))
            pygame.quit()
            sys.exit()

