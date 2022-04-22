from pygame.math import Vector2


class Position:
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            layer: int = 0,
            scale_multiplier: int = 1
    ):
        self.scale_multiplier = scale_multiplier
        self._vector = Vector2(x, y)
        self._scale_vector = Vector2(x, y)
        self.update_scale()
        self.layer = layer

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        layer = self.layer
        return Position(x, y, layer, self.scale_multiplier)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.update_scale()

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        layer = self.layer
        return Position(x, y, layer, self.scale_multiplier)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.update_scale()

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __set__(self, instance, value):
        self.x = value.x
        self.y = value.y
        self.layer = value.layer
        self.update_scale()

    def __str__(self):
        return f'{self._vector.x}, {self._vector.y}'

    def __repr__(self):
        return self.__str__()

    def get_x(self) -> float: return self._vector.x

    def set_x(self, x) -> None:
        self._vector.x = x
        self.update_scale()

    x = property(get_x, set_x)

    def get_y(self) -> float: return self._vector.y

    def set_y(self, y) -> None:
        self._vector.y = y
        self.update_scale()

    y = property(get_y, set_y)

    def move_to(self, target):
        self.x = target.x
        self.y = target.y
        self.layer = target.layer
        self.update_scale()

    def lerp_to(self, target, lerp: float = 0.2):
        lerp_snap = 0.01
        if self != target:
            distance_x = (target.x - self.x) * lerp
            distance_y = (target.y - self.y) * lerp

            if lerp_snap > distance_x > -lerp_snap and lerp_snap > distance_y > -lerp_snap:
                self.move_to(target)
            else:
                self.x += distance_x
                self.y += distance_y
                self.update_scale()
        else:
            self.move_to(target)

    def update_scale(self):
        self._scale_vector = Vector2(self.x * self.scale_multiplier, self.y * self.scale_multiplier)

    @property
    def scale(self):
        return self._scale_vector
