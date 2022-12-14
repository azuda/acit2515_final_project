import pygame


class BaseScreen:
  """Basic class for all screen types"""

  def __init__(self, window):
    self.window = window
    self.next_screen = False


  def run(self):
    clock = pygame.time.Clock()
    self.running = True
    while self.running:
      clock.tick(60)
      self.update()
      self.draw()
      pygame.display.update()

      if self.next_screen == "game":
        clock = pygame.time.Clock()

      # event loop to quit when Esc is pressed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
          self.next_screen = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          self.running = False
          self.next_screen = False

        self.manage_event(event)


    @property
    def rect(self):
      return self.window.get_rect()


    # methods for override by child classes
    def draw(self):
      print("DRAW method")

    def update(self):
      print("UPDATE method")

    def manage_event(self, event):
      print("MANAGE EVENT method")
