#! /usr/bin/python

import pygame
from pygame import *
from pygame.transform import flip

playersheet = pygame.image.load('Resources/Sprites/Mobs/Player.png')
slashsheet = pygame.image.load('Resources/Sprites/Misc/slash.png')
glowsheet = pygame.image.load('Resources/Sprites/Misc/glow.png')
drgskl = pygame.image.load('Resources/Sprites/Misc/Dragon_Breath.png')
guisheet = pygame.image.load('Resources/Sprites/Misc//gui.png')
items = pygame.image.load('Resources/Sprites/Misc/items.jpg')

def create_sequence(sprite, number_of_images ,start_x, start_y, size_x, size_y, jumper, scale = 1, go_down = None, go_down_walk_speed = 0):
    sequence = []
    for n in range(number_of_images):
        frame = Surface((size_x,size_y),pygame.SRCALPHA)
        frame.blit(sprite,(start_x, start_y))
        # Change image size and put in sequence array
        sequence.append(pygame.transform.scale(frame, ( int(size_x*scale), int(size_y*scale) )))
        start_x -= jumper  
        if go_down and n == go_down_walk_speed:
            start_y -= size_y
            start_x = -1
    return sequence  

def create_image(sprite ,start_x, start_y, size_x, size_y, scale = 1):
    frame = Surface((size_x, size_y),pygame.SRCALPHA)
    frame.blit(sprite,(start_x, start_y))
    # Change image size
    return [pygame.transform.scale(frame, ( int(size_x*scale), int(size_y*scale) ))]


class Player:
    def __init__(self, sprite):
        self.sprite = sprite
        self.scale = 0.8
        self.stand_down = create_sequence(self.sprite, 8 ,-1, -1, 62, 127, 65, self.scale)
        self.stand_right = create_sequence(self.sprite, 8 ,-1, -130, 62, 127, 65, self.scale)
        self.stand_left = create_sequence(self.sprite, 8 ,-1, -130, 62, 127, 65, self.scale)
        self.stand_up = create_sequence(self.sprite, 8 ,-1, -259, 62, 127, 65, self.scale)
        self.walk_down = create_sequence(self.sprite, 6 ,-1, -388, 62, 127, 65, self.scale)
        self.walk_right = create_sequence(self.sprite, 6 ,-1, -517, 62, 127, 65, self.scale)
        self.walk_left = create_sequence(self.sprite, 6 ,-1, -517, 62, 127, 65, self.scale)
        self.walk_up = create_sequence(self.sprite, 6 ,-1, -646, 62, 127, 65, self.scale)
        self.attack_right = create_sequence(self.sprite, 4 ,-1, -905, 184, 158, 186, self.scale)
        self.attack_left = create_sequence(self.sprite, 4 ,-1, -905, 184, 158, 186, self.scale)
        self.attack_down = create_sequence(self.sprite, 4 ,-1, -785, 64, 119, 65, self.scale)
        self.attack_up = create_sequence(self.sprite, 4 ,-1, -1066, 64, 156, 65, self.scale)
        self.die_down = create_sequence(self.sprite, 3 ,-1, -1221, 62, 127, 65, self.scale)
        self.die_right = create_sequence(self.sprite, 3 ,-1, -1348, 62, 127, 65, self.scale)
        self.die_left = create_sequence(self.sprite, 3 ,-1, -1348, 62, 127, 65, self.scale)
        self.die_up = create_sequence(self.sprite, 3 ,-1, -1460, 62, 127, 65, self.scale)

class Spider:
    def __init__(self) -> None:
        self.scale = 0.5
        spider_attack_down = pygame.image.load('Resources/Sprites/Mobs/Spider/spider_attack_down_sprite.png')
        spider_attack_up = pygame.image.load('Resources/Sprites/Mobs/Spider/spider_attack_up_sprite.png')
        spider_attack_left = pygame.image.load('Resources/Sprites/Mobs/Spider/spider_attack_left_sprite.png')
        spider_left = pygame.image.load('Resources/Sprites/Mobs/Spider/spider_left_sprite.png')
        spider_down= pygame.image.load('Resources/Sprites/Mobs/Spider/spider_down_sprite.png')
        spider_up= pygame.image.load('Resources/Sprites/Mobs/Spider/spider_up_sprite.png')
        self.stand_down = create_sequence(spider_down, 3 ,-1, -1, 300, 300, 300, self.scale, True, 7)       
        self.stand_right =create_sequence(spider_left, 3 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.stand_left = create_sequence(spider_left, 3 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.stand_up = create_sequence(spider_up, 3 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.walk_down = create_sequence(spider_down, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.walk_right = create_sequence(spider_left, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.walk_left = create_sequence(spider_left, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.walk_up = create_sequence(spider_up, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.attack_right = create_sequence(spider_attack_left, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.attack_left = create_sequence(spider_attack_left, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.attack_down = create_sequence(spider_attack_down, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)
        self.attack_up = create_sequence(spider_attack_up, 15 ,-1, -1, 300, 300, 300, self.scale, True, 7)



spider = Spider()
player = Player(playersheet)
player_glow = create_sequence(glowsheet, 1 ,0, 0, 150, 133, 65)
slash = create_sequence(slashsheet, 3, 0, 0, 90, 100, 90, 1)
bag = create_sequence(guisheet, 1, -422, -20, 267, 315, 90, 1.5)

# Items

# Buttons
bag_button = create_sequence(guisheet, 1, -754, -173, 30, 30, 90, 1.5)
settings_button = create_sequence(guisheet, 1, -754, -237, 30, 30, 90, 1.5)
fight_button = create_sequence(guisheet, 1, -754, -143, 30, 30, 90, 1.5)











### SKILL 1 ###
character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-3,6))
character = pygame.transform.scale(character, (136,149))
dragon_flame1 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-177,6))
character = pygame.transform.scale(character, (136,149))
dragon_flame2 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-353,6))
character = pygame.transform.scale(character, (136,149))
dragon_flame3 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-532,6))
character = pygame.transform.scale(character, (136,149))
dragon_flame4 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-15,-200))
character = pygame.transform.scale(character, (136,149))
dragon_flame5 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-192,-200))
character = pygame.transform.scale(character, (136,149))
dragon_flame6 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-369,-200))
character = pygame.transform.scale(character, (136,149))
dragon_flame7 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-543,-200))
character = pygame.transform.scale(character, (136,149))
dragon_flame8 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-20,-406))
character = pygame.transform.scale(character, (136,149))
dragon_flame9 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-174,-406))
character = pygame.transform.scale(character, (136,149))
dragon_flame10 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-303,-406))
character = pygame.transform.scale(character, (136,149))
dragon_flame11 = character

character = Surface((136,149),pygame.SRCALPHA)
character.blit(drgskl,(-416,-406))
character = pygame.transform.scale(character, (136,149))
dragon_flame12 = character



dragon_flame = [dragon_flame1,dragon_flame2,dragon_flame3,dragon_flame4,dragon_flame5,dragon_flame6,dragon_flame7,dragon_flame8,dragon_flame9,dragon_flame10,dragon_flame11,dragon_flame12]




## GUI ##


character = Surface((245,191),pygame.SRCALPHA)
character.blit(guisheet,(-20,-267))
character = pygame.transform.scale(character, (245*2,191*2))
charmenu = character
gui = [bag,charmenu]

character = Surface((17,18),pygame.SRCALPHA)
character.blit(guisheet,(-462,-335))
character = pygame.transform.scale(character, (17*2,18*2))
plus = character


