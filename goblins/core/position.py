from pygame.math import Vector2


class Position:
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            layer: int = 0
    ):
        self._vector = Vector2(x, y)
        self.layer = layer

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        layer = self.layer
        return Position(x, y, layer)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        layer = self.layer
        return Position(x, y, layer)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __set__(self, instance, value):
        self.x = value.x
        self.y = value.y
        self.layer = value.layer

    def __str__(self):
        return f'{self._vector.x}, {self._vector.y}'

    def __repr__(self):
        return self.__str__()

    def get_x(self) -> float: return self._vector.x

    def set_x(self, x) -> None:
        self._vector.x = x

    x = property(get_x, set_x)

    def get_y(self) -> float: return self._vector.y

    def set_y(self, y) -> None:
        self._vector.y = y

    y = property(get_y, set_y)

    def move_to(self, target):
        self.x = target.x
        self.y = target.y
        self.layer = target.layer

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
        else:
            self.move_to(target)
