from pygame.sprite import DirtySprite, collide_rect
from pygame.transform import flip
from pygame import Rect
from GameObject import Damage, Slash



class LivingObject(DirtySprite):
  def __init__(self, location_x, location_y, animation, group, walk_speed = 3):
    DirtySprite.__init__(self, group)
    # Visibility
    self.animation = animation
    self.direction = "down"
    self.image = self.animation.stand_down[0]
    self.rect = Rect(location_x, location_y, 50, 50)
    self.animation_speed_counter = 0
    self.animation_speed = 40
    self.animation_multiplier = 1
    self.animframe = 3
    self.attack_time = 30
    self.attack_counter = 0
    # Movement
    self.yvel = 0
    self.xvel = 0
    self._step = walk_speed
    self.moving = False
    self.attacking = False
    self.colliding = False
    self.accelerating = False
    self._running_step = 6
    self.running_force = 0
    # Gameplay
    self.maxhp = 20
    self.hp = self.maxhp

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
    self.hp -= damage
    Damage(self.rect.x + 20, self.rect.y - 50, damage, 18)
    Slash(self)
    if self.hp < 0:
      self.hp = 0

  def move(self, direction):
    self.moving = True
    if self.accelerating:
      speed = self._running_step
    else:
      speed = self._step
    self.direction = direction
    if direction == "down":
      self.yvel = speed
    if direction == "up":
      self.yvel = -speed
    if direction == "left":
      self.xvel = -speed
    if direction == "right":
      self.xvel = speed

  def attack_loop(self):
    if self.attack_time >= self.attack_counter:
      self.attack_counter +=1
    else:
      self.attacking = False
      self.attack_counter = 0

  def animate(self):
    """
    #TODO: Make Generic to all objects
    """
    if self.attacking:
      self.animation_speed = int(20 * self.animation_multiplier)
      self.loop_animation(getattr(self.animation, f"attack_{self.direction}"))
    elif self.moving:
      if self.accelerating:
        self.animation_speed = int(20 * self.animation_multiplier)
      else:
        self.animation_speed = int(25 * self.animation_multiplier)
      self.loop_animation(getattr(self.animation, f"walk_{self.direction}"))

    else:
      self.animation_speed = int(40 * self.animation_multiplier)
      self.loop_animation(getattr(self.animation, f"stand_{self.direction}"))


  def loop_animation(self, animtype):
      for anim in animtype:
          if self.animation_speed_counter >= self.animation_speed:
            self.update_image(anim)
            self.animation_speed_counter = 0
          else:
            self.animation_speed_counter += 1

  def update_image(self, image):
      if self.direction == "left":
          image = flip(image, True, False)
      self.image = image

      