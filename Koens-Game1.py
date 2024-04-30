# This is the basic setup for pygame Display surface

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Koens First Game')
clock = pygame.time.Clock()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  # Draw all elements
  # Update everything
  pygame.display.update()
  clock.tick(60)