from pygame.transform import flip
from enum import Enum
   
class Animator():
  def __init__(self, obj):
    self.animation_speed_counter = 0
    self.animation_speed = 40
    self.animation_multiplier = 1
    self.animframe = 3
    self.obj = obj

  def animate(self):
    if self.obj.attacking:
      self.animation_speed = int(20 * self.animation_multiplier)
      self.loop_animation(getattr(self.obj.animation, f"attack_{self.obj.direction}"))
    elif self.obj.moving:
      if self.obj.accelerating:
        self.animation_speed = int(20 * self.animation_multiplier)
      else:
        self.animation_speed = int(25 * self.animation_multiplier)
      self.loop_animation(getattr(self.obj.animation, f"walk_{self.obj.direction}"))

    else:
      self.animation_speed = int(40 * self.animation_multiplier)
      self.loop_animation(getattr(self.obj.animation, f"stand_{self.obj.direction}"))


  def loop_animation(self, animtype):
      """
      Animation speed might be too fast, we want to reduce it speed by
      looping a counter.
      """
      for anim in animtype:
          if self.animation_speed_counter >= self.animation_speed:
            self.update_image(anim)
            self.animation_speed_counter = 0
          else:
            self.animation_speed_counter += 1



  def update_image(self, image):
      """
      Reduce code by flipping the image on left/right
      This should set the actual image on the object canvas.
      """
      if self.obj.direction == "left":
          image = flip(image, True, False)
      self.obj.image = image



   