import pygame
from .sprite import MySprite


class Player(MySprite):
  '''Component representing player character'''

  def __init__(self, width, height, **kwargs):
    super().__init__(**kwargs)
    self.image = pygame.image.load("./sprites/player.png")
    self.image = pygame.Surface.convert_alpha(self.image)
    self.image = pygame.transform.scale(self.image, (width, height))
    self.rect = self.image.get_rect()

    if self.limits:
      self.move_to(
        self.limits.center[0] - self.rect.width / 2,
        self.limits.bottom - self.rect.height,
      )
