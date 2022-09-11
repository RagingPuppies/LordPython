from pygame.sprite import Sprite
from GameGroups import engine_objects

class Attack(Sprite):
    def __init__(self, delay = 50):
        Sprite.__init__(self, engine_objects)
        self.delay = delay
        self.counter = 0
        self.hitting = False
        self.can_hit = True

    def update(self):
        ...

    def hit_enemy(self, enemy, damage = 2):
        enemy.get_hit(damage)
        self.update()

