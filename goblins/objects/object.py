from pygame.surface import Surface

from goblins.core import Pos


class Object:
    def __init__(self):
        self.pos = Pos(0.0, 0.0, 0)
        from goblins.core import TILE_SIZE
        self.surface = Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.surface.get_rect()

    def draw(self, surface):
        surface.blit(self.surface, (100, 100))

    def initialize(self):
        self.rect = self.surface.get_rect()