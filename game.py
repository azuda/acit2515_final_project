'''
ACIT 2515 Final Project
Aaron Zhang - A01316218
'''

import pygame


class Game:
  def __init__(self):
    self.window = pygame.display.set_mode((800, 800))

  def run(self):
    # screens = {
    #   "start": StartScreen,
    #   "game": GameScreen,
    #   "game_over": GameOverScreen,
    # }

    running = True
    clock = pygame.time.Clock()
    while running:
      clock.tick(30)

      # event loop - quit when Esc is pressed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key in (pygame.K_ESCAPE):
            running = False

      # get key presses outside of event loop
      keys = pygame.key.get_pressed()
      # handle controls

      # update screen
      pygame.display.update()


if __name__ == "__main__":
  game_x = Game()
  game_x.run()
