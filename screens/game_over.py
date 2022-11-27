import pygame, json
from .base_screen import BaseScreen


class GameOverScreen(BaseScreen):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    # load current score
    with open("data/this_score.json", "r") as f:
      self.score = json.load(f)
    
    # append this_score to scores.json
    with open("data/scores.json", "r") as f:
      scores = json.load(f)
    scores.append(self.score)
    with open("data/scores.json", "w") as f:
      json.dump(scores, f)


  def draw(self):
    self.window.fill((25, 30, 35))

    pygame.init()
    font1 = pygame.font.SysFont("comicsans", 36)
    font2 = pygame.font.SysFont("comicsans", 24)
    game_over = font1.render("Stage Completed", True, (255, 255, 255))
    score_text = font2.render(f"Score: {self.score['score']}", True, (255, 255, 255))
    acc_text = font2.render(f"Accuracy: {self.score['acc'] * 100}%", True, (255, 255, 255))
    self.window.blit(game_over, (480, 320))
    self.window.blit(score_text, (480, 360))
    self.window.blit(acc_text, (480, 380))


  def update(self):
    pass


  def manage_event(self, event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      self.running = False
      self.next_screen = False
