from goblins.entities.entity import Entity


class Plant(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 0.0
        self.maximum_health = 0.0

