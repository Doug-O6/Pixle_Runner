# This is the basic setup for pygame Display surface

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Koens 1st Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('Hi Koen !!!!!', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,300))
  screen.blit(text_surface,(350,50))
  
  snail_rect.x -= 3
  if snail_rect.right <= 0: snail_rect.left = 800
  screen.blit(snail_surface,snail_rect)

  pygame.display.update()
  clock.tick(60)