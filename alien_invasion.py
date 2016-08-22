import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption(("Alien Invasion"))

  # make a ship
  ship = Ship(screen)

  # start the main loop
  while True:
    gf.check_events() 
 
    # Redraw the screen during each pass  
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()

run_game()

