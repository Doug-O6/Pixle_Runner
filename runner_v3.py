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
  return current_time

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

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

# Intro screen -----
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,30,2)
player_stand_rect = player_stand.get_rect(center = (400,200))


game_name = test_font.render('Pixel Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press Space Bar to Play', False, (111,196,169))
game_message_rect = game_message.get_rect(center=(400,340))

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
    score = display_score()

    # Snail movement (right to left movement only)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    # Player movement (jumping up and down only using space bar and mouse click on player)
    player_gravity += 1 
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surf,player_rect)
 
    if snail_rect.colliderect(player_rect):
      game_active = False
  else:                       # Game end code ---------------------------
    screen.fill((94,129,162))
    screen.blit(player_stand,player_stand_rect)

    score_message = test_font.render(f'Score:  {score}', False, (111,196,169))
    score_message_rect = score_message.get_rect(center=(400,330))
    screen.blit(game_name,game_name_rect)

    if score == 0:
      screen.blit(game_message,game_message_rect)
    else:
      screen.blit(score_message,score_message_rect)
  
  # Pygame display refresh rate = 60 times/sec
  pygame.display.update()
  clock.tick(60)