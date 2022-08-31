from enum import Enum
from pygame import KEYDOWN, KEYUP, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import sys


def handle_event(event, controls):
  #print(event)
  if event.type == QUIT: 
    sys.exit()

  if event.type == KEYDOWN: 
    if event.key == 119:
      controls.UP = True
    if event.key == 115:
      controls.DOWN = True
    if event.key == 97:
      controls.LEFT = True
    if event.key == 100:
      controls.RIGHT = True
    if event.key == 32:
      controls.ACCELERATE = True

  if event.type == KEYUP: 
    if event.key == 119:
      controls.UP = False
    if event.key == 115:
      controls.DOWN = False
    if event.key == 97:
      controls.LEFT = False
    if event.key == 100:
      controls.RIGHT = False
    if event.key == 32:
      controls.ACCELERATE = False

  if event.type == MOUSEBUTTONDOWN: 
    if event.button == 1:
      controls.MOUSE_LEFT = True
    if event.button == 3:
      controls.MOUSE_RIGHT = True

  if event.type == MOUSEBUTTONUP: 
    if event.button == 1:
      controls.MOUSE_LEFT = False
    if event.button == 3:
      controls.MOUSE_RIGHT = False