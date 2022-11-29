import pygame


class Sound:
  def __init__(self, name, volume):
    self.sound = pygame.mixer.Sound(name)
    self.sound.set_volume(volume)

  def play(self):
    self.sound.play()
