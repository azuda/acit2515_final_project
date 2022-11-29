import pygame, json
from datetime import datetime
from .base_screen import BaseScreen
from components import Player, Point
from sounds import Sound


class GameScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # initialize stats to draw
    self.score = 0
    self.combo = 0

    # player sprite group
    self.player = Player(limits=self.window.get_rect())
    self.player_group = pygame.sprite.GroupSingle(self.player)

    # points sprite group
    self.active_points = pygame.sprite.Group()

    # load stage points data from json
    with open("data/stage2.json", "r") as f:
      stage_data = json.load(f)
    self.points_data = stage_data
    self.total_score = 0

    # load sound effects
    self.sound_click = Sound("sounds/click_normal.wav", 0.25)
    self.sound_pew = Sound("sounds/pew.wav", 0.25)


  def draw(self):
    pygame.init()
    self.window.fill((25, 30, 35))
    self.player_group.draw(self.window)
    self.active_points.draw(self.window)

    font = pygame.font.SysFont("comicsans", 30)
    # draw score
    score_text = font.render(f"Score: {str(self.score)}", True, (255, 255, 255))
    self.window.blit(score_text, (10, 670))
    # draw combo
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
      if point["timing"] <= pygame.time.get_ticks():
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
        self.total_score += sprite.value
        sprite.kill()
      # kill points if they fall off screen
      if sprite.rect.y > 720:
        self.sound_pew.play()
        self.combo = 0
        self.total_score += sprite.value
        sprite.kill()

    # update sprites
    self.player_group.update()
    self.active_points.update()

    # check that stage is over
    if len(self.active_points) == 0:
      if pygame.time.get_ticks() > 1000:
        # append score to scores.json
        with open("data/this_score.json", "w") as f:
          json.dump({"time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
          "score": self.score,
          "acc": round(self.score / self.total_score, 2)}, f)

        self.next_screen = "game_over"
        self.running = False


  def manage_event(self, event):
    pass
