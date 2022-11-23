import pygame
from .sprite import MySprite


class Point(MySprite):
  '''Parent class of point types'''

  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    if self.limits:
      self.move_to(
        self.limits.center[0] - self.rect.width / 2,
        self.limits.bottom - self.rect.height,
      )


class StandardPoint(Point):
  '''Represents normal points to catch'''

  def __init__(self, width, height, **kwargs):
    super().__init__(**kwargs)
    self.image = pygame.image.load("sprites/point1.png")
    self.image = pygame.Surface.convert_alpha(self.image)
    self.image = pygame.transform.scale(self.image, (width, height))
    self.rect = self.image.get_rect()

    self.fall_speed = 1
    self.rect.y -= 20 * self.fall_speed

