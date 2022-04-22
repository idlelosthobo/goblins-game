from pygame.surface import Surface

from goblins.core import GlobalSingleton, Position, TILE_SIZE
from goblins.interface import CameraSingleton


class Entity:
    def __init__(self, layer):
        self.layer = layer
        self.position = Position()
        self.position.scale_multiplier = TILE_SIZE
        self.surface = Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.surface.get_rect()
        self.state = None
        self.global_singleton = GlobalSingleton()
        self.camera_singleton = CameraSingleton()
        self.update_timer = 0
        self.update_speed = 1000
        self.is_viewable = False
        self.tick_timer = 0
        self.tick_speed = 100

    def draw(self, surface):
        if self.is_viewable:
            surface.blit(
                self.surface,
                (
                    self.camera_singleton.world_translate.x + (self.position.x * TILE_SIZE),
                    self.camera_singleton.world_translate.y + (self.position.y * TILE_SIZE)
                )
            )

    def tick(self):
        self.tick_timer += self.global_singleton.delta_time
        if self.tick_timer >= self.tick_speed:
            self.update_timer += self.global_singleton.delta_time

            if self.update_timer >= self.update_speed:
                self.update()
                self.update_timer = 0

            self.is_viewable = self.camera_singleton.in_focus(self.position.scale)
            self.tick_timer = 0

    def update(self):
        pass


