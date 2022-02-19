from random import randint

from pygame.surface import Surface

from goblins.core import TILE_SIZE, WORLD_LAYERS, WORLD_SIZE


class Layer:
    def __init__(self):
        self.surface = Surface((TILE_SIZE * WORLD_SIZE, TILE_SIZE * WORLD_SIZE))
        self.generate()

    def draw(self, surface, x, y):
        surface.blit(self.surface, (x, y))

    def generate(self):
        grass_tile = Surface((TILE_SIZE, TILE_SIZE))
        for x in range(WORLD_SIZE):
            for y in range(WORLD_SIZE):
                grass_tile.fill((0, randint(50,60), 0))
                self.surface.blit(grass_tile, (x * TILE_SIZE, y * TILE_SIZE))

