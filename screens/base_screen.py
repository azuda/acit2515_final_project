import pygame


class BaseScreen:
  '''Basic class for all screen types'''

  def __init__(self, window):
    self.window = window
    self.next_screen = False

  def run(self):
    clock = pygame.time.Clock()
    self.running = True
    
    while self.running:
      clock.tick(30)
      self.update()
      self.draw()
      pygame.display.update()

      # event loop - quit when Esc is pressed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key in (pygame.K_ESCAPE):
            running = False
      
    @property
    def rect(self):
      return self.window.get_rect()


    # METHODS FOR CHILD CLASS OVERRIDE
    def draw(self):
      print("DRAW method")
    
    def update(self):
      print("UPDATE method")

    def manage_event(self, event):
      print("MANAGE EVENT method")
