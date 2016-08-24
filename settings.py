class Settings():
  """ A class to store the settings for alien invasion"""

  def __init__(self):
    """ Initialize the games settings"""

    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 130)

    # ship settings
    self.ship_speed_factor = 5
    
    # bullet settings
    self.bullet_width = 5
    self.bullet_height = 5
    self.bullet_speed = 5
    self.bullet_color = 160, 160, 160
    self.bullets_max = 15
