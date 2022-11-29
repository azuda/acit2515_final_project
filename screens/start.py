import pygame
import handler.handler as handler
from .base_screen import BaseScreen


class StartScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    pygame.init()
    self.font = pygame.font.SysFont("comicsans", 36)
    self.play_message = self.font.render("Enter stage to play:", True, (255, 255, 255))
    self.input_text = ""


  def draw(self):
    pygame.init()
    self.window.fill((25, 30, 35))
    self.window.blit(self.play_message, (470, 360))
    self.window.blit(self.text_surface, (470, 400))


  def update(self):
    self.text_surface = self.font.render(self.input_text, True, (255, 255, 255))


  def manage_event(self, event):
    # handle user input for stage selection
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        valid_stage = handler.stage_select(self.input_text)
        if not valid_stage:
          self.input_text = ""
        else:
          self.next_screen = "game"
          self.running = False
      elif event.key == pygame.K_BACKSPACE:
        self.input_text = self.input_text[:-1]
      else:
        self.input_text += event.unicode
