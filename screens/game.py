import pygame, json
import handler.handler as handler
from datetime import datetime
from .base_screen import BaseScreen
from components import Player, Point
from sounds import Sound


class GameScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # time handling
    self.start_time = pygame.time.get_ticks()

    # initialize draw stats
    self.score = 0
    self.combo = 0

    # initialize sprite groups
    self.player = Player(limits=self.window.get_rect())
    self.player_group = pygame.sprite.GroupSingle(self.player)
    self.active_points = pygame.sprite.Group()

    # initialize sound effects
    self.sound_click = Sound("sounds/click_normal.wav", 0.25)
    self.sound_pew = Sound("sounds/pew.wav", 0.25)

    # load stage data from json
    with open(f"data/{handler.get_stage()}", "r") as f:
      stage_data = json.load(f)
    self.points_data = stage_data
    self.points_hit = 0
    self.points_count = 0


  def draw(self):
    pygame.init()
    self.window.fill((25, 30, 35))

    # draw sprites
    self.player_group.draw(self.window)
    self.active_points.draw(self.window)

    # draw score and combo
    font = pygame.font.SysFont("comicsans", 30)
    score_text = font.render(f"Score: {str(self.score)}", True, (255, 255, 255))
    self.window.blit(score_text, (10, 670))
    combo_text = font.render(f"Combo: {str(self.combo)}x", True, (255, 255, 255))
    self.window.blit(combo_text, (10, 640))


  def update(self):
    # movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
      if keys[pygame.K_LSHIFT]:
        self.player.move("left", boost=4)
      else:
        self.player.move("left")
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
      if keys[pygame.K_LSHIFT]:
        self.player.move("right", boost=4)
      else:
        self.player.move("right")

    # spawn points at specified time and pos
    for point in self.points_data:
      if point["timing"] <= pygame.time.get_ticks() - self.start_time:
        self.active_points.add(Point(limits=self.window.get_rect(), point_type=point["type"], position=point["position"]))
        self.points_data.remove(point)

    # ensure points are always falling
    for sprite in self.active_points:
      sprite.fall(1.2)

      # player collision with point
      if self.player.rect.colliderect(sprite.rect):
        self.sound_click.play()
        self.combo += 1
        self.score += sprite.value
        self.points_hit += 1
        self.points_count += 1
        sprite.kill()
      # kill points if they fall off screen
      if sprite.rect.y > 720:
        self.sound_pew.play()
        self.combo = 0
        self.points_count += 1
        sprite.kill()

    # update sprites
    self.player_group.update()
    self.active_points.update()

    # check if stage is finished
    if (len(self.active_points) == 0) and (self.points_count > 0):
      # append score to scores.json
      with open("data/this_score.json", "w") as f:
        json.dump({"time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "stage": handler.get_stage()[:-5],
        "score": self.score,
        "acc": round(self.points_hit / self.points_count, 2)}, f)

      self.next_screen = "game_over"
      self.running = False


  def manage_event(self, event):
    pass
