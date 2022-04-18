from goblins.entities.entity import Entity


class Creature(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 0.0
        self.health = 0.0
        self.maximum_health = 0.0

