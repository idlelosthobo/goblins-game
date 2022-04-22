from goblins.entities.entity import Entity


class Creature(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 0.0
        self.health = 0.0
        self.maximum_health = 0.0
        self.target_position = self.position

