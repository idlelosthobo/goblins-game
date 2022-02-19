from goblins.core.config import SCROLL_SPEED, TILE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, WORLD_SIZE


class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.target_x = 0.0
        self.target_y = 0.0
        self.layer = 0
        self.zoom_level = 1
        self.limit_x = TILE_SIZE * WORLD_SIZE - WINDOW_WIDTH
        self.limit_y = TILE_SIZE * WORLD_SIZE - WINDOW_HEIGHT

    def scroll(self):
        if self.x != self.target_x:
            distance_x = (self.target_x - self.x) * 0.2

            if 1.0 > distance_x > -1.0:
                self.x = self.target_x
            else:
                self.x += distance_x

        if self.y != self.target_y:
            distance_y = (self.target_y - self.y) * 0.2

            if 1.0 > distance_y > -1.0:
                self.y = self.target_y
            else:
                self.y += distance_y

        print(f'{self.x = }, {self.y = }')

    def scroll_by(self, x, y):
        self.target_x += x
        self.target_y += y

        if 0.0 > self.target_x:
            self.target_x = 0.0

        if self.limit_x < self.target_x:
            self.target_x = self.limit_x

        if 0.0 > self.target_y:
            self.target_y = 0

        if self.limit_y < self.target_y:
            self.target_y = self.limit_y

    def scroll_east(self):
        self.scroll_by(SCROLL_SPEED, 0)

    def scroll_north(self):
        self.scroll_by(0, SCROLL_SPEED * -1)

    def scroll_south(self):
        self.scroll_by(0, SCROLL_SPEED)

    def scroll_to(self, x, y):
        self.target_x = x
        self.target_y = y

    def scroll_west(self):
        self.scroll_by(SCROLL_SPEED * -1, 0)

    @property
    def translate_world_x(self):
        return 0 - self.x

    @property
    def translate_world_y(self):
        return 0 - self.y
