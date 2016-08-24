import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
  """ A class to manage bullets from the ship """

  def __init__(self, screen, ai_settings, ship):
    """ Create a bullet at the current ship position """
    super(Bullet, self).__init__()
    self.screen = screen
    self.ai_settings = ai_settings

    # Create a rect for the bullet at 0,0
    self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) 
    self.rect.centerx = ship.rect.centerx
    self.rect.top = ship.rect.top

    # Store the top coord of the bullet as a float
    self.y = float(self.rect.y)

    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed

  def update(self):
    """ Move up the screen """
    # update the decimal position 
    self.y -= self.speed_factor
    # update the rect
    self.rect.y = self.y

  def draw_bullet(self):
    """ Draw bullet to screen"""
    pygame.draw.rect(self.screen, self.color, self.rect)


  
