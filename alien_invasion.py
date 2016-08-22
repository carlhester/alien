import sys
import pygame

def run_game():
  pygame.init()
  screen = pygame.display.set_mode((1200, 800))
  pygame.display.set_caption(("Alien Invasion"))

  # start the main loop
  while True:
  
    # watch for keyboard events and mouse events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    # Make the most recently drawn screen visible
    pygame.display.flip()

run_game()

