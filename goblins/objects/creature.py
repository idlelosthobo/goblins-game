from .object import Object


class Creature(Object):
    def __init__(self):
        super().__init__()
        self.speed = 0.0
        self.health = 0.0
        self.maximum_health = 0.0
