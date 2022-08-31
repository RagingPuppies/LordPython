from GameLivingObject import LivingObject
from pygame.sprite import  collide_rect
from GameObject import PlayerPanel, Glow
from FightEngine import Attack
from GameGroups import enemies, player_stopper

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

  def update(self , controls, objects):   
    if self.hp < 1:
      self.pannel.remove_childs()
      self.pannel.kill()
      self.glow.kill()
      self.kill()

    self.attack(controls)
  
    if not self.attacking:
      self.movement(controls)
      self.idle(controls)

      self.rect.left += self.xvel
      self.collide(self.xvel, 0, objects)
      self.rect.top += self.yvel
      self.collide(0, self.yvel, objects)

    if self.attacking:
      self.attack_loop()
      
    self.animate()


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

  def attack(self, controls):
    if controls.MOUSE_LEFT and not any(o.mouse_over for o in player_stopper):  
      self.attacking = True
      enemy = self.collide_with_enemy()
      if enemy:
        self.normal_attack.hit_enemy(enemy)

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



