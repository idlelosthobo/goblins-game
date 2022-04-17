from pygame.surface import Surface

from goblins.core import Position, TILE_SIZE
from goblins.singletons import GlobalSingleton


class Entity:
    def __init__(self):
        self.position = Position()
        self.surface = Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.surface.get_rect()
        self.state = None
        self.global_singleton = GlobalSingleton()
        self.update_timer = 0
        self.update_speed = 1000

    def draw(self, surface):
        surface.blit(
            self.surface,
            (
                self.global_singleton.world_translate.x + (self.position.x * TILE_SIZE),
                self.global_singleton.world_translate.y + (self.position.y * TILE_SIZE)
            )
        )

    def initialize(self):
        self.rect = self.surface.get_rect()

    def tick(self):
        self.update_timer += self.global_singleton.delta_time
        if self.update_timer >= self.update_speed:
            self.update()
            self.update_timer = 0

    def update(self):
        pass


