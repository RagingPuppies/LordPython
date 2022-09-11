from GameEngine import GameEngine
from GameControls import Controls
from GameLevel import Level
from GameCamera import PlayerCamera


WIN_WIDTH = 800
WIN_HEIGHT = 600

def main():
  controls = Controls()
  level = Level('Resources/Levels/deadlands.png')
  camera = PlayerCamera(level.width, level.height, WIN_WIDTH, WIN_HEIGHT)
  game = GameEngine("LordPython", level, camera ,controls, WIN_WIDTH, WIN_HEIGHT, show_blocks = False)
  game.run()

if __name__ == "__main__":
  main()
