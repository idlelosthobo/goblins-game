from .creature import Creature


class Goblin(Creature):
    def __init__(self):
        super().__init__()
        self.surface.fill((0, 255, 0))
        self.initialize()
