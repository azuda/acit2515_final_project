import pygame


class Player(pygame.sprite.Sprite):
  '''Component representing player character'''

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.image = pygame.image.load("../sprites/player.png")
    self.rect = self.image.get_rect()
  
