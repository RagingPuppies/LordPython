from GameLivingObject import LivingObject
from pygame.sprite import  collide_rect
from GameObject import PlayerPanel, Glow
from FightEngine import Attack
from GameGroups import enemies, player_stopper
from random import randint

class Player(LivingObject):
  def __init__(self, loc_x, loc_y, animation, bag, group):
    LivingObject.__init__(self, loc_x, loc_y, animation, group)
    self.running_force = 50
    self.pannel = PlayerPanel(self)
    self.glow = Glow(self)
    self.normal_attack = Attack()
    self.maxhp = 50
    self.hp = self.maxhp
    self.maxmana = 100
    self.mana = self.maxmana
    self.bag = bag
    self.bag.player = self

    # Player States
    self.defense = 0
    self.strength = 5


  def update(self , controls, objects):
    if self.hp < 1:
      self.pannel.remove_childs()
      self.pannel.kill()
      self.glow.kill()
      self.kill()
  
    if not self.attacking:
      self.movement(controls)
      self.idle(controls)

      self.rect.left += self.xvel
      self.collide(self.xvel, 0, objects)
      self.rect.top += self.yvel
      self.collide(0, self.yvel, objects)

    if self.attacking:
      enemy = self.collide_with_enemy()
      self.attack(enemy)

    if self.is_attacking(controls) and not self.attacking:
      self.attacking = True
    
    if self.bag.changed:
      self.active_defense = self.defense + self.wearable_defense_additions()
      self.active_damage = self.wearable_attack_additions()
      #TODO: fix removal of text
      for t in self.bag.text:
        self.bag.text.remove(t)
        t.kill()
      self.bag.changed = False
    self.animate()

  def wearable_defense_additions(self):
    total_defense = 0
    for slot in filter(lambda slot: slot.type != 'BAG', self.bag.slots):
      if slot.item:
        if getattr(slot.item, 'defense', None):
          total_defense += slot.item.defense
    return total_defense

  def add_health_points(self, points):
    if self.hp + points > self.maxhp:
      self.hp = self.maxhp
    else:
      self.hp += points
      
  def wearable_attack_additions(self):
    total_attack = 0
    for slot in filter(lambda slot: slot.type != 'BAG', self.bag.slots):
      if slot.item:
        if getattr(slot.item, 'attack', None):
          total_attack += slot.item.attack
    return total_attack

  def movement(self, controls):
    if self.running_force > 0 and controls.ACCELERATE:
      self.accelerating = True
    if controls.UP: self.move("up")
    if controls.DOWN: self.move("down")
    if controls.LEFT: self.move("left")
    if controls.RIGHT: self.move("right")

  def collide_with_enemy(self):
      for enemy in enemies:
        if collide_rect(self, enemy):
            return enemy

  def calc_damage(self):
    max_rand = randint(0, self.level)
    return self.active_damage + self.strength + max_rand

  def is_attacking(self, controls):
    if controls.MOUSE_LEFT and not any(o.mouse_over for o in player_stopper):
      return True

  def hit(self, enemy):
    if enemy:
      self.normal_attack.hit_enemy(enemy, self.calc_damage())

  def idle(self, controls):
    if not (controls.LEFT or controls.RIGHT or controls.UP or controls.DOWN or controls.ACCELERATE):
        self.xvel = 0
        self.yvel = 0
        self.moving = False
        self.accelerating = False
    
    if not controls.RIGHT and not controls.LEFT:
      self.xvel = 0

    if not controls.UP and not controls.DOWN:
      self.yvel = 0

  def pickup(self, item):
    if self.bag.assert_bag(item):
      return True



