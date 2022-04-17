import random
import os

random.seed(1)

DEBUG = True

SCROLL_SPEED = 100

TILE_SIZE = 8

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360

WORLD_LAYERS = 1
WORLD_SIZE = 2000

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSET_DIR = os.path.join(BASE_DIR, 'assets')
