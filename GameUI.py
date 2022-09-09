from pygame.sprite import Sprite
from pygame import Surface
from GameGroups import overlay_objects
import GameColors
from GameObject import Text

class ItemDescriptionPanel(Sprite):
  def __init__(self, width, height, objective):
    Sprite.__init__(self, [overlay_objects])
    self.image = Surface([width, height])
    self.image.fill(GameColors.BLACK)
    self.image.set_alpha(GameColors.ALPHA_LEVEL) 
    self.rect = self.image.get_rect()
    self.objective = objective
    self.x_offset = 50
    self.rect.x = self.objective.rect.x + self.x_offset
    self.rect.y = self.objective.rect.y + self.x_offset
    self.text = []

    if len(self.text) == 0:
      start_x = 10
      start_y = 10
      for k, v in self.objective.properties.items():
        self.text.append(Text((self.rect.x + start_x), (self.rect.y + start_y), f"{k}: {v}", color = GameColors.WHITE, group = overlay_objects ))
        start_y += 20


  def update(self, _):
    self.rect.x = self.objective.rect.x + self.x_offset
    self.rect.y = self.objective.rect.y + self.x_offset



  def clean(self):
    for t in self.text:
      t.kill()
    self.kill()