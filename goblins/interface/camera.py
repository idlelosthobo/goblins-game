import logging

from goblins.core.config import *
from goblins.core import Position, Singleton


class CameraSingleton(Singleton):
    position = Position()
    target = Position()
    zoom_level = 1
    limit_x = TILE_SIZE * WORLD_SIZE - WINDOW_WIDTH
    limit_y = TILE_SIZE * WORLD_SIZE - WINDOW_HEIGHT

    def in_focus(self, position):
        if self.position.x - WINDOW_WIDTH < position.x < self.position.x + (WINDOW_WIDTH * 2)  and \
                self.position.y - WINDOW_HEIGHT < position.y < self.position.y + (WINDOW_HEIGHT * 2):
            return True
        else:
            return False

    def update(self):
        if self.position != self.target:
            self.position.lerp_to(self.target)

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
    def world_translate(self):
        return Position(0 - self.position.x, 0 - self.position.y)
