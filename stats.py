class Stats():
  """ Track statistics for alien invasion """

  def __init__(self, ai_settings):
    """ init stats"""
    self.ai_settings = ai_settings
    self.reset_stats()

  def reset_stats(self):
    """ Init stats that can change"""
    self.ships_left = self.ai_settings.ship_limit
