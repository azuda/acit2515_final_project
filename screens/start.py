import pygame
from .base_screen import BaseScreen


class StartScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def draw(self):
    self.window.fill((25, 30, 35))

    pygame.init()
    font = pygame.font.SysFont("comicsans", 36)
    img = font.render("Press SPACE to play", True, (255, 255, 255))
    self.window.blit(img, (240, 360))

  def update(self):
    pass

  def manage_event(self, event):
    print(event)
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      self.next_screen = "game"
      self.running = False
