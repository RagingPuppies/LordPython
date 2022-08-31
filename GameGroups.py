from pygame.sprite import  Group

static_objects = Group()
enemies = Group()
players = Group()
physical_block = Group()
location_based = Group()
engine_objects = Group() # Objects that needs to update, but not draw
overlay_objects = Group() # Menus, buttons and etc
dropped_items = Group() # Group for items, should be printed specially
player_stopper = Group() # Objects that should stop the player from attacking
