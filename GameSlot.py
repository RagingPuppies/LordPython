from pygame.sprite import Sprite
from abc import ABC
from GameGroups import overlay_objects
from pygame import Surface
from pygame import mouse
import GameColors


class AbstractSlot(Sprite, ABC):
    def __init__(self, x, y, size, bag):
      Sprite.__init__(self, overlay_objects)
      self.image = Surface([size, size])
      self.image.fill(GameColors.WHITE)
      self.image.set_alpha(50)  
      self.rect = self.image.get_rect()
      self.x_rel_bag_pos = x
      self.y_rel_bag_pos = y
      self.bag = bag
      self.mouse_over = False
      self.item = None

    def clicked(self, controls):
      mouse_x, mouse_y = mouse.get_pos()
      location_x, location_y, size_x, size_y = self.rect

      if location_x + size_x > mouse_x > location_x and location_y + size_y > mouse_y > location_y and controls.MOUSE_LEFT and self.is_clickable:
        self.mouse_over = True
        self.is_clickable = False
        return True

      if not controls.MOUSE_LEFT:
          self.is_clickable = True
      # Reset mouseover switches
      self.mouse_over = False

    def printx(Self):
      ...

    def assert_item(self, item):
      if not self.item:
        print(f"Got new item {item}")
        self.item = item
        self.item.in_slot = True
        self.bag.changed = True
        return True
      print(f"Already Got item in this Slot.")
      return False

    def toggle_visibiliy(self):
      if self.bag.visible:
        self.rect.x = self.x_rel_bag_pos
        self.rect.y = self.y_rel_bag_pos
        if self.item and self.item.in_slot and not self.item.drag:
          self.item.rect.x = self.rect.x
          self.item.rect.y = self.rect.y          
      else:
        self.rect.x = -1000
        if self.item and self.item.in_slot:
          self.item.rect.x = -1000
          self.item.rect.y = -1000 

    def update(self, controls):

      if self.clicked(controls):
        if self.item and not self.bag.items_being_drag():
          self.item.drag = True
          self.bag.moving_item = self.item
          self.item = None

        else:
          if self.bag.moving_item and (self.bag.moving_item.type == self.type or self.type == 'BAG'):
            if self.assert_item(self.bag.moving_item):
              self.item.drag = False
              self.bag.moving_item = False
          else:
            print('Theres an item moving or item type desont match')

      self.toggle_visibiliy()



class BagSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'BAG'


class BootsSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'BOOTS'


class ArmorSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'ARMOR'


class GlovesSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'GLOVES'


class PantsSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'PANTS'


class HelmetSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'HELMET'


class WeaponSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'WEAPON'


class ShieldSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'SHIELD'


class JewelSlot(AbstractSlot):
    def __init__(self, x, y, size, bag):
      AbstractSlot.__init__(self, x, y, size, bag)
      self.type = 'JEWEL'