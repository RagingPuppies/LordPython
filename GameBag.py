from pygame.sprite import Sprite
from pygame import Rect
from GameSlot import BagSlot, BootsSlot, ArmorSlot, ShieldSlot, GlovesSlot, HelmetSlot, WeaponSlot, PantsSlot, JewelSlot
from GameGroups import overlay_objects
from pygame import Surface
from GameSprites import bag
from pygame import mouse
import GameColors
from GameObject import Text

class Bag(Sprite):
    def __init__(self):
      Sprite.__init__(self, overlay_objects)
      self.image = bag[0]
      self.rect = Rect(-1000, 80, 400, 600)
      self.mouse_over = False
      self.clickable = False
      self.visible = False
      self.slots_size = 50
      self.total_size = 12
      self.current_capacity = 0
      self.slots = []
      self.moving_item = None
      self.changed = False
      self.text = []
      self.player = None
      self.init_slots()
      

    def init_slots(self):
      self.slots.append(BootsSlot(300, 325, self.slots_size, self))
      self.slots.append(PantsSlot(300, 275, self.slots_size, self))
      self.slots.append(ArmorSlot(300, 225, self.slots_size, self))
      self.slots.append(HelmetSlot(300, 175, self.slots_size, self))
      self.slots.append(GlovesSlot(250, 200, self.slots_size, self))
      self.slots.append(ShieldSlot(350, 250, self.slots_size, self))
      self.slots.append(WeaponSlot(250, 250, self.slots_size, self))
      self.slots.append(JewelSlot(250, 375, self.slots_size, self))
      self.slots.append(JewelSlot(300, 375, self.slots_size, self))
      self.slots.append(JewelSlot(350, 375, self.slots_size, self))
      border = 3
      x_start_point = 53
      y_start_point = 180
      x_offset = x_start_point
      for s in range(self.total_size):
        x = x_offset
        y = y_start_point 
        slot = BagSlot(x, y, self.slots_size, self)
        self.slots.append(slot)
        _, _, size_x, size_y = slot.rect
        x_offset = x + size_x + border
        if s % 3 == 2:
          y_start_point = y + size_y + border
          x_offset = x_start_point

    def find_empty_slot(self):
      for slot in filter(lambda slot: slot.type == 'BAG', self.slots):
        if not slot.item:
          return slot
      print(f"No slot found.")
      return False

    def items_being_drag(self):
      if self.moving_item:
        return True
      return False

    def assert_bag(self, item):
      slot = self.find_empty_slot()
      if slot:
        slot.assert_item(item)
        self.changed = True
        return True
      print("Bag is full.")
      return False

    def apply_item_on_player(self, item):
      if item.use_item(self.player):
        return True

    def update(self, _):
      if self.moving_item:
          mouse_x, mouse_y = mouse.get_pos()
          self.moving_item.rect.x = mouse_x
          self.moving_item.rect.y = mouse_y
      if self.visible:
        self.rect.x = 15
        if self.player and len(self.text) == 0:
          self.text.append(Text(self.rect.x + 235 , self.rect.y + 350  , f"Strength: {self.player.strength}({self.player.active_damage})", color = GameColors.WHITE, group = overlay_objects ))
          self.text.append(Text(self.rect.x + 235 , self.rect.y + 370  , f"Defense: {self.player.defense}({self.player.active_defense})", color = GameColors.WHITE, group = overlay_objects ))
      else:
        self.rect.x = -1000
        for t in self.text:
          self.text.remove(t)
          t.kill()