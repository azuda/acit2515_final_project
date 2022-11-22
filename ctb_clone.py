'''
ACIT 2515 Final Project
Pygame CTB Clone
Aaron Zhang - A01316218
'''

import pygame
from screens import StartScreen, GameScreen, GameOverScreen


class Game:
  def __init__(self):
    self.window = pygame.display.set_mode((800, 800))

  def run(self):
    screens = {
      "start": StartScreen,
      "game": GameScreen,
      "game_over": GameOverScreen,
    }

    current_screen = "start"
    running = True
    while running:
      # get screen class
      screen_class = screens.get(current_screen)
      if not screen_class:
        raise RuntimeError(f"Screen {current_screen} not found")

      # link new screen object to window
      screen = screen_class(self.window)
      screen.run()



      

      # update screen
      pygame.display.update()


if __name__ == "__main__":
  game_x = Game()
  game_x.run()
