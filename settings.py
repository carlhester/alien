class Settings():
  """ A class to store the settings for alien invasion"""

  def __init__(self):
    """ Initialize the games settings"""

    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 130)
    self.bg_image = 'images/space.bmp'

    # ship settings
    self.ship_speed_factor = 10
    
    # bullet settings
    self.bullet_width = 300
    self.bullet_height = 5
    self.bullet_speed = 15
    self.bullet_color = 160, 160, 160
    self.bullets_max = 5

    # alien settings
    self.alien_speed_factor = 1
    self.fleet_drop_speed = 10
    # fleet_direction of 1 represents right; -1 represents left
    self.fleet_direction = 1
