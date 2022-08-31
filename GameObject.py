from pygame.sprite import Sprite
from pygame import Surface, SRCALPHA
from pygame import Rect
from pygame.font import Font
from GameGroups import static_objects, physical_block
from GameSprites import player_glow, slash
import GameColors

class Block(Sprite):
    def __init__(self, x, y, z, s):
        Sprite.__init__(self, physical_block)
        self.rect = Rect(x, y, z, s)

    def update(self):
      ...

class ImageObject(Sprite):
    def __init__(self):
      Sprite.__init__(self, static_objects)
      self.animation_speed_counter = 0
      self.animation_speed = 1
      self.animation = None
      self.animation_position = 0
    def update(self):
      ...

    def animate(self):
      try:
        if self.animation_speed_counter >= self.animation_speed:
          self.image = self.animation[self.animation_position]
          self.animation_position += 1
          self.animation_speed_counter = 0
        else:
          self.animation_speed_counter += 1
      except IndexError:
        self.kill()



class StaticImageObject(Sprite):
    def __init__(self):
      Sprite.__init__(self, static_objects)

    def update(self):
      ...

class Slash(ImageObject):
    def __init__(self, objective):
      ImageObject.__init__(self)
      self.objective = objective
      self.animation = slash
      self.image = self.animation[0]
      self.rect = Rect(self.objective.rect.x - 20 , self.objective.rect.y - 20, 1, 1)
      

    def update(self):
      self.rect.x = self.objective.rect.x - 20
      self.rect.y = self.objective.rect.y - 20
      self.animate()
      

class Glow(StaticImageObject):
    def __init__(self, objective):
      StaticImageObject.__init__(self)
      self.image = player_glow[0]
      self.rect = self.image.get_rect()
      self.objective = objective

    def update(self):
      self.rect.x = self.objective.rect.x - 40
      self.rect.y = self.objective.rect.y - 15


class StaticDrawObject(Sprite):
    def __init__(self, width, height):
      Sprite.__init__(self, static_objects)
      self.image = Surface([width, height])
      self.max = width
      self.image.fill(GameColors.BLACK)
      self.rect = self.image.get_rect()

    def update(self):
      ...


class PlayerPanel(StaticDrawObject):
    def __init__(self, objective):
      StaticDrawObject.__init__(self, width = 52, height = 9)
      self.objective = objective
      self.healthbar = HealthBar(objective)
      self.manabar = ManaBar(objective)
      self.image.fill(GameColors.BLACK)
      self.image.set_alpha(GameColors.ALPHA_LEVEL) 

    def update(self):
      self.rect.x = self.objective.rect.x 
      self.rect.y = self.objective.rect.y - 55

    def remove_childs(self):
      self.healthbar.kill()
      self.manabar.kill()



"""
#TODO: Maybe bars can be united?
"""

class HealthBar(StaticDrawObject):
    def __init__(self, objective):
      StaticDrawObject.__init__(self, width = 50, height = 3)
      self.objective = objective

    def update(self):
      self.rect.x = self.objective.rect.x + 1
      self.rect.y = self.objective.rect.y -54
      self.image = Surface([(self.objective.hp / self.objective.maxhp) * self.max, self.image.get_height()])
      self.image.set_alpha(GameColors.ALPHA_LEVEL) 
      if self.objective.hp / self.objective.maxhp > 0.5:
        self.image.fill(GameColors.DARK_GREEN)
      if self.objective.hp / self.objective.maxhp <= 0.5:
        self.image.fill(GameColors.ORANGE)
      if self.objective.hp / self.objective.maxhp < 0.3:
        self.image.fill(GameColors.RED)


class ManaBar(StaticDrawObject):
    def __init__(self, objective):
      StaticDrawObject.__init__(self, width = 50, height = 3)
      self.objective = objective
      
    def update(self):
      self.rect.x = self.objective.rect.x + 1
      self.rect.y = self.objective.rect.y - 49
      self.image = Surface([(self.objective.mana / self.objective.maxmana) * self.max, self.image.get_height()])
      self.image.set_alpha(GameColors.ALPHA_LEVEL)  
      self.image.fill(GameColors.DARK_BLUE)


class Text(Sprite):
    def __init__(self, x, y, text, color = GameColors.BLACK, size = 14, group = static_objects):
        Sprite.__init__(self, group)
        self.image = Surface((30, 30), SRCALPHA)
        self.rect = Rect(x, y, 32, 32)
        self.font = Font("Resources/Fonts/diablo_h.ttf", size)
        self.text = str(text)
        self.color = color

    def update(self, _ = None):
        screen_text = self.font.render(self.text, True, self.color)
        self.image = screen_text



class Damage(Text):
  def __init__(self, x, y, text, size):
    Text.__init__(self,x, y, text, size)
    self.counter = 0
    self.color = GameColors.RED
    self.alpha = 150
    self.size = 14

  def update(self):
    Text.update(self)
    self.dmgloop()

  def dmgloop(self):
      if self.counter < 35:
          self.counter += 2
          self.rect[1] -= 3
          font = Font("Resources/Fonts/diablo_h.ttf", self.size)
          screen_text = font.render(self.text, True, self.color)
          self.image = screen_text
          self.image.set_alpha(self.alpha)  
          self.alpha -= 3
          self.size += 1
      else:
          self.kill()





