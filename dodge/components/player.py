import pygame


class Player(pygame.sprite.Sprite):
  """Component representing player character"""

  def __init__(self, width, height, colour=(255, 255, 255), **kwargs):
    super().__init__(**kwargs)
    self.image = pygame.Surface((width, height))
    self.image.fill(colour)
    self.rect = self.image.get_rect()

    if self.limits:
      self.move_to(
        self.limits.center[0] - self.rect.width / 2,
        self.limits.bottom - self.rect.height,
      )
