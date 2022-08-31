import pygame
from GameEventHandler import handle_event
from GameGroups import static_objects, enemies, location_based, engine_objects, overlay_objects, dropped_items

MOUSE_OVER = False

class GameEngine:
  def __init__(self, name, level, camera, controls, WIN_WIDTH, WIN_HEIGHT, step = 27, show_blocks = False):
    self.name = pygame.display.set_caption(name)
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    self.step = step 
    self.controls = controls
    self.show_blocks = show_blocks
    self.level = level
    self.camera = camera
    self.visible_game_objects = []
    self.invisible_game_objects = []
  
  def run(self):
    self.initialize()
    while True:
        self.clock.tick(self.step)
        self.compute_events()
        self.compute_objects()
        self.render_all_objects()
        pygame.display.update()

  def initialize(self):
    """Create game objects"""
    pygame.init() 
    self.visible_game_objects = self.level.create_objects()
    self.player = self.level.create_player()
    self.platform_blocks = self.level.platform_blocks()

  def compute_player(self):
    self.camera.update(self.player)
    self.player.update(self.controls , self.platform_blocks)


  def compute_objects(self):
    for enemy in enemies:
      enemy.update(self.player, self.platform_blocks)

    for object in static_objects:
      object.update()

    for object in engine_objects:
      object.update()

    for object in overlay_objects:
      object.update(self.controls)

    for object in dropped_items:
      object.update(self.controls, self.player)

    self.compute_player()

  def render_all_objects(self):
    self.screen.blit(self.level.background, self.camera.apply(self.level))
    
    objects = location_based.sprites()
    objects.sort(key=lambda x: x.rect.y)
    for object in objects:
      self.screen.blit(object.image , self.center_pivot_sprite(object))

    for object in static_objects:
      self.screen.blit(object.image, self.camera.apply(object))

    for object in overlay_objects:
      self.screen.blit(object.image, object)


    if self.show_blocks:
      for block in self.platform_blocks:
        color = (255,0,0)
        pygame.draw.rect(self.screen, color, self.camera.apply(block))

  def center_pivot_sprite(self, object):
      middle_placer = self.camera.apply(object).center
      return object.image.get_rect(center = middle_placer)

  def compute_events(self):
    for event in pygame.event.get():
      handle_event(event, self.controls)


