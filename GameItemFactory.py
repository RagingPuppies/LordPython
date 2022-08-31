from ast import Dict
from unittest.mock import patch
from GameItem import Wearable 
import pygame
import random
import csv


def random_item(level, loc_x, loc_y):
  with open('Resources/Datasets/items.csv', newline='') as csvfile:
       reader = csv.DictReader(csvfile)
       items = list(reader)

  filtered_items = list(filter(lambda i: int(i['level']) == level, items))
  factory = ItemFactory(random.choice(filtered_items))
  return factory.create_item(loc_x, loc_y)


class ItemFactory:
  def __init__(self, item: Dict) -> None:
    self.item = item
    self.name = item['name']
    self.path = 'Resources/Sprites/Misc/Items'
    self.type = item['type']

  def construct_img_path(self) -> str:
    filename = self.name.lower().replace(' ', '_')
    return f"{self.path}/{filename}.png"

  def load_image(self, scale = 0.5):
    path = self.construct_img_path()
    print(path)
    img = pygame.image.load(path)
    x, y, x_s, y_s = img.get_rect()
    scaled = pygame.transform.scale(img, ( int(x_s*scale), int(y_s*scale) ))
    return [scaled]

  def create_item(self, loc_x, loc_y):
    wearables = ['BOOTS', 'PANTS', 'ARMOR', 'HELMET', 'GLOVES', 'WEAPON', 'SHIELD', 'JEWEL']
    if self.type in wearables:
      return Wearable(self.load_image(), loc_x, loc_y, self.item)


  