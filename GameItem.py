from pygame.sprite import Sprite
from pygame import Rect, Surface
from GameGroups import dropped_items, player_stopper, location_based, overlay_objects
from pygame import mouse, BLEND_RGB_ADD, BLEND_RGB_SUB
from GameUI import ItemDescriptionPanel
import math


class AbstractItem(Sprite):

    def __init__(self, sprite, x, y):
      Sprite.__init__(self, [dropped_items, player_stopper, location_based])
      
      self.image = sprite[0]
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.bright_level = 35
      self.pickup_radius = 100
      self.mouse_over = False
      self.is_clickable = True
      self.is_bright = False
      self.droped = True
      self.in_slot = False
      self.in_bag = False
      self.drag = False
      self.description = None
      self.type = None
      self.properties = {'Name': 'Abstract Item'}


    def is_mouse_over(self, mouse_x, mouse_y):

      location_x, location_y, size_x, size_y = self.rect

      if location_x + size_x > mouse_x > location_x and location_y + size_y > mouse_y > location_y:
        self.mouse_over = True
        return True

      # Reset mouseover switches
      self.mouse_over = False
      self.is_clickable = True

    def player_in_range(self, player):
        return math.hypot(self.rect.x - player.rect.x, self.rect.y - player.rect.y) < float(self.pickup_radius)

    def create_description(self):
      if not self.description:
        self.description = ItemDescriptionPanel(250, 200, self)

    def action(self, player):

      if self.droped and self.player_in_range(player):
        if player.pickup(self):
          self.droped = False
          location_based.remove(self)
          overlay_objects.add(self)

      if self.in_slot:
        self.in_bag = True

    def update(self, controls, player = None):

      mouse_x, mouse_y = mouse.get_pos()
      
      if self.drag:
        self.rect.x = mouse_x
        self.rect.y = mouse_y

      if self.is_mouse_over(mouse_x, mouse_y):

        if self.in_bag and not self.drag:
          self.create_description()

        if not self.is_bright:
          self.image.fill((self.bright_level, self.bright_level, self.bright_level), special_flags=BLEND_RGB_ADD)
          self.is_bright = True

        if controls.MOUSE_LEFT and self.is_clickable:
          self.is_clickable = False
          self.action(player)

        if not controls.MOUSE_LEFT:
          self.is_clickable = True

      else:

        if self.is_bright:
          self.image.fill((self.bright_level, self.bright_level, self.bright_level), special_flags=BLEND_RGB_SUB)
          self.is_bright = False


        if self.description:
          self.description.clean()
          self.description = None

class Wearable(AbstractItem):
    def __init__(self, sprite, x, y, item):
      AbstractItem.__init__(self, sprite, x, y)
      self.defense = item['defense']
      self.type = item['type']
      self.price = 0
      self.properties = {'Name': item['name'], 'Defense': item['defense'], 'Price': self.price}
