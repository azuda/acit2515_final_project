import pygame
from .base_screen import BaseScreen

from components import Player, Point


class GameScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.sprites = pygame.sprite.Group()

    # player sprite
    self.player = Player(limits=self.window.get_rect())
    self.sprites.add(self.player)

    self.point = Point(limits=self.window.get_rect(), type="300")
    self.sprites.add(self.point)


  def draw(self):
    self.window.fill((25, 30, 35))
    self.sprites.draw(self.window)


  def update(self):
    # movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
      if keys[pygame.K_LSHIFT]:
        self.player.move("left", boost=2.5)
      else:
        self.player.move("left")
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
      if keys[pygame.K_LSHIFT]:
        self.player.move("right", boost=2.5)
      else:
        self.player.move("right")

    # ensure point is always falling
    self.point.move("down")

    # player collision with point
    if self.player.rect.colliderect(self.point.rect):
      self.point.kill()
      point = Point(limits=self.window.get_rect())
      self.sprites.add(point)
      # temporary redirect to start screen
      # self.next_screen = "start"
      # self.running = False

    # update sprites
    self.sprites.update()


  def manage_event(self, event):
    if event.type == pygame.K_ESCAPE:
      self.running = False
      self.next_screen = False
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
      # boost move speed
      return None
