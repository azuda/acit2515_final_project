import pygame
from .sprite import MySprite
import random


class Point(MySprite):
  """Represents points that the player can catch"""

  def __init__(self, type="300", **kwargs):
    if type not in ["300", "100", "boost"]:
      raise AttributeError("Invalid point type")

    super().__init__(**kwargs)

    # load corresponding image for point type
    if type is "300":
      self.image = pygame.image.load("sprites/point_300.png")
    elif type is "100":
      self.image = pygame.image.load("sprites/point_100.png")
    elif type is "boost":
      self.image = pygame.image.load("sprites/point_boost.png")

    self.image = pygame.Surface.convert_alpha(self.image)
    self.image = pygame.transform.scale(self.image, (150, 150))
    self.rect = self.image.get_rect()

    if self.limits:
      self.move_to(random.randint(50, 1230), -100)
