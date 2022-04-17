import logging

from goblins.core.config import *
from goblins.core import Position
from goblins.singletons import GlobalSingleton


class Camera:
    def __init__(self):
        self.position = Position()
        self.target = Position()
        self.zoom_level = 1
        self.limit_x = TILE_SIZE * WORLD_SIZE - WINDOW_WIDTH
        self.limit_y = TILE_SIZE * WORLD_SIZE - WINDOW_HEIGHT
        self.global_singleton = GlobalSingleton()

    def update(self):
        if self.position != self.target:
            self.position.lerp_to(self.target)
            self.global_singleton.world_translate.x = 0 - self.position.x
            self.global_singleton.world_translate.y = 0 - self.position.y

    def scroll_by(self, x, y):
        self.target.x += x
        self.target.y += y

        if 0.0 > self.target.x:
            self.target.x = 0.0

        if self.limit_x < self.target.x:
            self.target.x = self.limit_x

        if 0.0 > self.target.y:
            self.target.y = 0

        if self.limit_y < self.target.y:
            self.target.y = self.limit_y

    def scroll_east(self):
        self.scroll_by(SCROLL_SPEED, 0)

    def scroll_north(self):
        self.scroll_by(0, SCROLL_SPEED * -1)

    def scroll_south(self):
        self.scroll_by(0, SCROLL_SPEED)

    def scroll_to(self, x, y):
        self.target.x = x
        self.target.y = y

    def scroll_west(self):
        self.scroll_by(SCROLL_SPEED * -1, 0)

    @property
    def translate_world_x(self):
        return 0 - self.position.x

    @property
    def translate_world_y(self):
        return 0 - self.position.y
