import pygame, json
from .base_screen import BaseScreen

from components import Player, Point


class GameScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.score = 0

    # player sprite group
    self.player = Player(limits=self.window.get_rect())
    self.player_group = pygame.sprite.GroupSingle(self.player)

    # points sprite group
    self.active_points = pygame.sprite.Group()

    # get points data from json file doesn't work
    # f = open("stage.json", "r")
    self.points_data = nope


  def draw(self):
    pygame.init()
    self.window.fill((25, 30, 35))
    self.player_group.draw(self.window)
    self.active_points.draw(self.window)

    # draw score
    font = pygame.font.SysFont("comicsans", 30)
    img = font.render(str(self.score), True, (255, 255, 255))
    self.window.blit(img, (10, 670))


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

    # spawn points at specified timings
    for point in self.points_data:
      if point["timing"] <= pygame.time.get_ticks():
        self.active_points.add(Point(limits=self.window.get_rect(), type=point["type"]))
        self.points_data.remove(point)

    # ensure points are always falling
    for sprite in self.active_points:
      sprite.fall(1.2)

      # player collision with point
      if self.player.rect.colliderect(sprite.rect):
        self.score += sprite.value
        sprite.kill()
      # kill points if they fall off screen
      if sprite.rect.y > 720:
        sprite.kill()

    # update sprites
    self.player_group.update()
    self.active_points.update()

    # check that stage is over
    if len(self.active_points) == 0:
      if pygame.time.get_ticks() > 1000:
        with open("scores.json", "w") as f:
          json.dump({"score": self.score}, f)

        self.next_screen = "game_over"
        self.running = False


  def manage_event(self, event):
    pass



nope = [
  {
    "type": "boost",
    "timing": 1000
  },
  {
    "type": "300",
    "timing": 1200
  },
  {
    "type": "100",
    "timing": 1250
  },
  {
    "type": "300",
    "timing": 1500
  },
  {
    "type": "100",
    "timing": 1550
  },
  {
    "type": "100",
    "timing": 1600
  },
  {
    "type": "300",
    "timing": 1700
  },
  {
    "type": "100",
    "timing": 1750
  },
  {
    "type": "300",
    "timing": 1800
  },
  {
    "type": "100",
    "timing": 1900
  },
  {
    "type": "boost",
    "timing": 2000
  },
  {
    "type": "300",
    "timing": 2250
  },
  {
    "type": "300",
    "timing": 2500
  },
  {
    "type": "300",
    "timing": 2750
  },
  {
    "type": "boost",
    "timing": 3000
  }
]
