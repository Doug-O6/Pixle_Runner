# This is the basic setup for pygame Display surface
# Using (https://www.youtube.com/watch?v=AY9MnQ4x3zk)

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
#tree_surface = pygame.image.load('graphics/tree_sm.png').convert_alpha()
score_surf = test_font.render('Runner', False, 'Black')
score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,300))
  pygame.draw.rect(screen, 'Pink', score_rect)
  pygame.draw.rect(screen, 'Pink', score_rect, 10)
  screen.blit(score_surf,score_rect)

  #Draw a line with one end following the mouse pointer.
  #pygame.draw.line(screen,'Blue', (20,20), pygame.mouse.get_pos(), 8)

  #screen.blit(tree_surface,(600,150))
  snail_rect.x -= 4
  if snail_rect.right <= 0: snail_rect.left = 800
  screen.blit(snail_surface,snail_rect)
  screen.blit(player_surf,player_rect)

  if player_rect.colliderect(snail_rect):  print('collision')  #returns 0 or 1
  

  pygame.display.update()
  clock.tick(60)