import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
  """ Respond to keypresses"""
  if event.key == pygame.K_ESCAPE:
    sys.exit()
  elif event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True
  elif event.key == pygame.K_UP:
    ship.moving_up = True
  elif event.key == pygame.K_DOWN:
    ship.moving_down = True
  elif event.key == pygame.K_SPACE:
    # create a new bullet
    new_bullet = Bullet(screen, ai_settings, ship)
    bullets.add(new_bullet)

def check_keyup_events(event, ship):
  """ Respond to keyrelease"""
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False
  elif event.key == pygame.K_UP:
    ship.moving_up = False
  elif event.key == pygame.K_DOWN:
    ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
  """ Respond to keypresses and mouse events """
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event,ai_settings, screen, ship, bullets)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship, bullets):
  """ Update images on the screen anf lip to new screen """
  # Redraw the screen during each pass through the loop
  screen.fill(ai_settings.bg_color)
  
  # redraw all bullets behind ship and aliens
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()

  # Make the most recently drawn screen visible
  pygame.display.flip()


  
