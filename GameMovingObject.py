from pygame.sprite import DirtySprite, collide_rect
from pygame import Rect
from GameObject import Damage, Slash
from Animation import Animator

class MovingObject(DirtySprite):
  def __init__(self, location_x, location_y, animation, group, level = 1):
    DirtySprite.__init__(self, group)
    # Visibility
    self.animator = Animator(self)
    self.animation = animation
    self.direction = "down"
    self.image = self.animation.stand_down[0]
    self.rect = Rect(location_x, location_y, 50, 60)
    self.animation_speed_counter = 0
    self.animation_speed = 40
    self.animation_multiplier = 1
    self.animframe = 3
    # Attack 
    self.delay_attack = 22
    self.attack_counter = 0
    # Movement
    self.yvel = 0
    self.xvel = 0
    self._walk_speed = 6
    self._running_speed = 8
    self.moving = False
    self.attacking = False
    self.can_attack = True
    self.colliding = False
    self.accelerating = False
    self.running_force = 0

    # Gameplay
    self.maxhp = 20
    self.hp = self.maxhp
    self.active_defense = 0
    self.active_damage = 0
    self.level = level

  def update(self):
    ...

  def collide(self, xvel, yvel, objects, *args):
      for object in objects:
          if collide_rect(self, object):
            if xvel > 0 : self.rect.right = object.rect.left
            if xvel < 0 : self.rect.left = object.rect.right
            if yvel > 0 : self.rect.bottom = object.rect.top
            if yvel < 0 : self.rect.top = object.rect.bottom

  def get_hit(self, damage):
    actual_dmg = (damage - self.active_defense)
    if actual_dmg < self.level:
      actual_dmg = self.level

    self.hp -= actual_dmg
    Damage(self.rect.x + 20, self.rect.y - 50, actual_dmg, 18)
    Slash(self)
    if self.hp < 0:
      self.hp = 0

  def move(self, direction):
    self.moving = True
    if self.accelerating:
      speed = self._running_speed
    else:
      speed = self._walk_speed
    self.direction = direction
    
    if direction == "down" and self.yvel < speed:
      self.yvel += 1
    if direction == "up" and self.yvel > -speed:
      self.yvel -= 1
    if direction == "left" and self.xvel > -speed:
      self.xvel -= 1
    if direction == "right" and self.xvel < speed:
      self.xvel += 1


  def attack(self, target):
    self.attack_counter +=1
    if self.attack_counter >= self.delay_attack:
      self.attack_counter = 0
      self.attacking = False
      self.hit(target)