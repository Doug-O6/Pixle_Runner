# This is the basic setup for pygame Display surface
# Using (https://www.youtube.com/watch?v=AY9MnQ4x3zk)

import pygame
from sys import exit

# Functions  -----------------------------------------------------
def display_score():
  current_time = int((pygame.time.get_ticks() - start_time) / 1000)
  score_surf = test_font.render(f'Score:  {current_time}',False,(64,64,64))
  score_rect = score_surf.get_rect(center=(400,50))
  screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

# Backgrounds sky and ground
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

# Text - will be made score board
# score_surf = test_font.render('Runner', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# Snail image and rectangle for collision recognition
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

# Player image and rectangle for collision recognition
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()  

    if game_active == True:           # Game active code ---------------------------
      if event.type == pygame.MOUSEBUTTONDOWN:
        if player_rect.collidepoint(event.pos):
          if player_rect.bottom == 300:
            player_gravity = -25

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if player_rect.bottom == 300:
            player_gravity = -25

    else:                            #  Game end code ---------------------------
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          snail_rect.left = 800
          game_active = True
          start_time = pygame.time.get_ticks()
          


  if game_active == True:           # Game active code ---------------------------
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    # pygame.draw.rect(screen, '#c0e8ec', score_rect)
    # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    # screen.blit(score_surf,score_rect)
    display_score()

    # Snail movement (right to left movement only)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    # Player movement (jumping up and down only using space bar and mouse click on player)
    player_gravity += 1 
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect(snail_rect):  print('collision')  #returns 0 or 1

    if snail_rect.colliderect(player_rect):
      game_active = False
  else:                       # Game end code ---------------------------
    screen.fill('Yellow')
  
  # Pygame display refresh rate = 60 times/sec
  pygame.display.update()
  clock.tick(60)