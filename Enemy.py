from GameLivingObject import LivingObject
from GameObject import HealthBar
from pygame.sprite import  collide_rect
from FightEngine import Attack
import math, random
from GameItemFactory import random_item

class Enemy(LivingObject):
    def __init__(self, loc_x, loc_y, level, animation , group, speed, sight = 200):
        LivingObject.__init__(self, loc_x, loc_y, animation, group)
        self.running_force = 900
        self.sight = sight
        self._step = speed
        self.level = level
        self.animation_multiplier = 10
        self.normal_attack = Attack(delay = 100)
        self.health_bar = HealthBar(self)
        
    def update(self, player, objects):
        if self.hp < 1:
            self.health_bar.kill()
            random_item(self.level, self.rect.x, self.rect.y)
            self.kill()

        if self.player_in_range(player) and not self.attacking:   
            self.move_towards_player(player)
        else:
            self.moving = False
            self.yvel = 0
            self.xvel = 0

        self.rect.left += self.xvel
        self.collide(self.xvel, 0, objects, player)
        self.rect.top += self.yvel
        self.collide(0, self.yvel, objects, player)

        self.animate()

    def collide(self, xvel, yvel, objects, player):
        LivingObject.collide(self, xvel, yvel, objects)
        if collide_rect(self, player):
            self.attacking = True
            self.normal_attack.hit_enemy(player)
        else:
            self.attacking = False

    def player_in_range(self, player):
        return math.hypot(self.rect.x - player.rect.x, self.rect.y - player.rect.y) < float(self.sight)

    def move_towards_player(self, player):
        if not self.attacking:
            offset = 50
            if self.rect.x > player.rect.x - random.randint(-offset, offset) : self.move("left")
            if self.rect.x < player.rect.x - random.randint(-offset, offset) : self.move("right")
            if self.rect.y > player.rect.y - random.randint(-offset, offset) : self.move("up")
            if self.rect.y < player.rect.y - random.randint(-offset, offset) : self.move("down")

            
