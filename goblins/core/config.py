import random
import os

random.seed(1)

DEBUG = True

SCROLL_SPEED = 100

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360

# PyGame has a texture limit of 16,000 x 16,000

TILE_SIZE = 16

WORLD_LAYERS = 1
WORLD_SIZE = 1000

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSET_DIR = os.path.join(BASE_DIR, 'assets')
