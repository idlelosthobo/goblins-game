from random import randint

from pygame.surface import Surface

from goblins.core import TILE_SIZE, WORLD_LAYERS, WORLD_SIZE
from goblins.singletons import GlobalSingleton


class Layer:
    def __init__(self):
        self.surface = Surface((TILE_SIZE * WORLD_SIZE, TILE_SIZE * WORLD_SIZE))
        self.generate()
        self.global_singleton = GlobalSingleton()

    def draw(self, surface):
        surface.blit(
            self.surface,
            (self.global_singleton.world_translate.x, self.global_singleton.world_translate.y)
        )

    def generate(self):
        grass_tile = Surface((TILE_SIZE, TILE_SIZE))
        for x in range(WORLD_SIZE):
            for y in range(WORLD_SIZE):
                grass_tile.fill((0, randint(50,56), 0))
                self.surface.blit(grass_tile, (x * TILE_SIZE, y * TILE_SIZE))

