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
        if self.hitting:
            self.counter += 1
            if self.counter == self.delay:
                self.counter = 0
                self.hitting = False

    def hit_enemy(self, enemy, damage = 5):
        if self.counter == 0:
            self.hitting = True
            enemy.get_hit(damage)
            self.update()

