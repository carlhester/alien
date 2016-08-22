import pygame

class Ship():
  def __init__(self, ai_settings, screen):
    """ Initialize the ship and set its starting position"""
    self.screen = screen
    self.ai_settings = ai_settings

    # Load the shp image and get its rect
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # start each new ship at the bottom center
    self.center = float(self.rect.centerx)
  
    # movement flag
    self.moving_right = False
    self.moving_left = False

  def update(self):
    """ update the ships position based on the movement flag """
    # update the ships center value, not the rect
    if self.moving_right and self.rect.right < self.screen_rect.right: 
      self.center += self.ai_settings.ship_speed_factor
    elif self.moving_left and self.rect.left > 0:
      self.center -= self.ai_settings.ship_speed_factor

    # update the rect object from self.center
    self.rect.centerx = self.center


  def blitme(self):
    """ Draw the ship at its current location """
    self.screen.blit(self.image, self.rect)


    
