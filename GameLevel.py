from GamePlayer import Player
from GameObject import Block
from GameBag import Bag
from GameButton import Button, BagButton
from GameSprites import player, spider, bag_button, settings_button, fight_button
from Enemy import Enemy
from pygame.sprite import Sprite
from pygame.image import load
from pygame import Rect
from GameGroups import players, enemies, location_based


bag = Bag()

class Level(Sprite):
  def __init__(self, background):
    self.background = load(background)
    self.rect = Rect(0, 0, 1, 1)
    self.width = self.background.get_width()
    self.height = self.background.get_height()

  def create_player(self):
    return Player(400, 400, player, bag, [players, location_based])

  def platform_blocks(self):
    objects = []
    objects.append(Block(1,1,215,200))
    objects.append(Block(1,1,1800,66))
    objects.append(Block(700,20,300,420))
    objects.append(Block(10,209,60,1600))
    objects.append(Block(1034,15,400,175))
    objects.append(Block(1720,12,100,1800))
    objects.append(Block(1555,70,200,100))
    objects.append(Block(1400,490,45,90))
    objects.append(Block(1336,560,60,60))
    objects.append(Block(1250,605,85,100))
    objects.append(Block(1220,708,90,20))
    objects.append(Block(1200,740,10,66))
    objects.append(Block(1670,570,50,180))
    objects.append(Block(1600,1090,110,110))
    objects.append(Block(1370,1200,330,135))
    objects.append(Block(1485,1340,300,210))
    objects.append(Block(1465,1640,300,210))
    objects.append(Block(1100,1390,70,150))
    objects.append(Block(0,1555,1230,280))
    objects.append(Block(905,1430,200,150))
    return objects

  def create_objects(self):
    Button(settings_button, 20, 20)
    BagButton(bag_button, 70, 20, bag)
    Button(fight_button, 120, 20)
    Enemy(800, 500, 1, spider,[enemies, location_based], 2)
    Enemy(766, 623, 1, spider,[enemies, location_based], 2)
    Enemy(800, 712, 1, spider,[enemies, location_based], 2)
    Enemy(1100, 500, 1, spider,[enemies, location_based], 2)
    Enemy(1200, 500, 1, spider,[enemies, location_based], 2)
    Enemy(1300, 500, 1, spider,[enemies, location_based], 2)
    Enemy(1100, 800, 1, spider,[enemies, location_based], 2)
    Enemy(1100, 1000, 1, spider,[enemies, location_based], 2)
    Enemy(1100, 1200, 1, spider,[enemies, location_based], 2)
    Enemy(1100, 1300, 1, spider,[enemies, location_based], 2)
    Enemy(1100, 1500, 1, spider,[enemies, location_based], 2)