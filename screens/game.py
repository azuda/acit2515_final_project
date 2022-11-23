import pygame
from .base_screen import BaseScreen

from components import Player


class GameScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.player = Player(100, 100, limits=self.window.get_rect())

    self.sprites = pygame.sprite.Group()
    self.sprites.add(self.player)


  def update(self):
    # movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
      self.player.move("left")
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
      self.player.move("right")
    
    # movement boost
    if keys[pygame.K_LSHIFT]:
      if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        self.player.move("left")
        self.player.move("left")
      if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        self.player.move("right")
        self.player.move("right")
    
    self.sprites.update()

    # handle catching points


  def draw(self):
    self.window.fill((20, 25, 30))
    self.sprites.draw(self.window)


  def manage_event(self, event):
    if event.type == pygame.K_ESCAPE:
      self.running = False
      self.next_screen = False
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
      # boost move speed
      return None
