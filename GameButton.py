from pygame.sprite import Sprite
from pygame import Rect
from GameGroups import overlay_objects, player_stopper
from pygame import mouse


class Button(Sprite):

    """
    This is a general buttom.
    - When clicked the Player can't click
    - Runs an action to be set by child.
    - Sets opacity higher on mouseover.
    """

    def __init__(self, sprite, x, y):
      Sprite.__init__(self, [overlay_objects, player_stopper])
      
      self.image = sprite[0]
      self.rect = Rect(x,y, 45, 45)
      self.bright_level = 10
      self.mouse_over = False
      self.is_clickable = True

    def is_mouse_over(self):

      mouse_x, mouse_y = mouse.get_pos()
      location_x, location_y, size_x, size_y = self.rect

      if location_x + size_x > mouse_x > location_x and location_y + size_y > mouse_y > location_y:
        self.mouse_over = True
        return True

      self.mouse_over = False
      self.is_clickable = True

    def action(self):
      ...

    def update(self, controls):

      if self.is_mouse_over():
        self.image.set_alpha(200)

        if controls.MOUSE_LEFT and self.is_clickable:
          self.is_clickable = False
          self.action()

        if not controls.MOUSE_LEFT:
          self.is_clickable = True

      else:
        self.image.set_alpha(150)  
    

class BagButton(Button):
  def __init__(self, sprite, x, y, bag):
    Button.__init__(self, sprite, x, y)

    self.bag = bag

  def action(self):

    if self.bag.visible:
      self.bag.visible = False

    else:
      self.bag.visible = True


