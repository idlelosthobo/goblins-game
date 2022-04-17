import random
from .creature import Creature
from ..core import Position


class Goblin(Creature):
    def __init__(self):
        super().__init__()
        self.surface.fill((128, 255, 0))
        self.initialize()

    def update(self):
        self.position.move_to(self.position + Position(random.randint(-1, 1), random.randint(-1, 1)))
