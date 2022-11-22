import pygame


class Player(pygame.sprite.Sprite):
  """Component representing player character"""

  def __init__(self, width, height, colour=(255, 255, 255), **kwargs):
    super().__init__(**kwargs)
    self.image = pygame.Surface((width, height))
    self.image.fill(colour)
    self.rect = self.image.get_rect()
