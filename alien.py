import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """ class to represent the single alien in the fleet """

  def __init__(self, ai_settings, screen):
    """ init alien and set starting pos. """ 
    super(Alien, self).__init__()
    self.screen = screen
    self.ai_settings = ai_settings

    # Load the alien image and get its rect
    self.image = pygame.image.load('images/alien.bmp')
    self.rect = self.image.get_rect()

    # start each new alien at the top left
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # store the aliens exact position
    self.x = float(self.rect.x)

  def blitme(self):
    """ Draw the alien at its current location """
    self.screen.blit(self.image, self.rect)
