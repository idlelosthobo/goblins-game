from random import randint

from pygame.surface import Surface

from goblins.core import TILE_SIZE, WORLD_LAYERS, WORLD_SIZE
from goblins.interface import CameraSingleton


class Layer:
    def __init__(self, world):
        self.surface = Surface((TILE_SIZE * WORLD_SIZE, TILE_SIZE * WORLD_SIZE))
        self.world = world
        self.generate()
        self.camera_singleton = CameraSingleton()

    def draw(self, surface):
        surface.blit(
            self.surface,
            (self.camera_singleton.world_translate.x, self.camera_singleton.world_translate.y)
        )

    def generate(self):
        grass_tile = Surface((TILE_SIZE, TILE_SIZE))
        for x in range(WORLD_SIZE):
            for y in range(WORLD_SIZE):
                grass_tile.fill((randint(0,20), randint(50,56), 0))
                self.surface.blit(grass_tile, (x * TILE_SIZE, y * TILE_SIZE))

