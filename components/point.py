import pygame
from .sprite import MySprite
import random


class Point(MySprite):
  '''Represents points that the player can catch'''

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.image = pygame.image.load(f"sprites/point.png")
    self.image = pygame.Surface.convert_alpha(self.image)
    self.image = pygame.transform.scale(self.image, (200, 200))
    self.rect = self.image.get_rect()

    self.fall_speed = 1
    self.rect.y -= 20 * self.fall_speed

    if self.limits:
      self.move_to(random.randint(50, 1230), -100)
