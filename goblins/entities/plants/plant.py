from goblins.entities.entity import Entity


class Plant(Entity):
    def __init__(self):
        super().__init__()
        self.health = 0.0
        self.maximum_health = 0.0

