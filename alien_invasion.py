import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  bg = pygame.image.load(ai_settings.bg_image)
  pygame.display.set_caption(("Alien Invasion"))

  # make a ship, a group of bullets and a group of aliens
  ship = Ship(ai_settings, screen)
  aliens = Group()
  bullets = Group()

  # create a fleet of aliens
  gf.create_fleet(ai_settings, screen, ship, aliens)

  # start the main loop
  while True:
    gf.check_events(ai_settings, screen, ship, bullets) 
    ship.update()
    gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
    gf.update_aliens(ai_settings, aliens)
    gf.update_screen(ai_settings, screen, bg, ship, aliens, bullets)


run_game()

