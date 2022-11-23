import pygame
from .base_screen import BaseScreen


class GameScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)


  def run(self):
    # get key presses outside of event loop
    keys = pygame.key.get_pressed()
    # handle controls