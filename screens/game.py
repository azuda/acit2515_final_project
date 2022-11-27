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

    # load stage points data from json
    with open("stage.json", "r") as f:
      stage_data = json.load(f)
    self.points_data = stage_data


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

    # spawn points at specified time and pos
    for point in self.points_data:
      if point["timing"] <= pygame.time.get_ticks():
        self.active_points.add(Point(limits=self.window.get_rect(), point_type=point["type"], position=point["position"]))
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
