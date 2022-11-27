import pygame
from .sprite import MySprite
import random


class Point(MySprite):
  """Represents points that the player can catch"""

  def __init__(self, point_type="300", timing=None, position=random.randint(50, 1230), **kwargs):
    super().__init__(**kwargs)
    self.time = timing

    # load corresponding image for point type
    if point_type == "300":
      self.image = pygame.image.load("sprites/point_300.png")
      self.value = 300
    elif point_type == "100":
      self.image = pygame.image.load("sprites/point_100.png")
      self.value = 100
    elif point_type == "boost":
      self.image = pygame.image.load("sprites/point_boost.png")
      self.value = 310
    else:
      raise AttributeError("Invalid point type")

    self.image = pygame.Surface.convert_alpha(self.image)
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()

    if self.limits:
      self.move_to(position, -100)
