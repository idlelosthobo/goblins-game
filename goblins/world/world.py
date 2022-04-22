import random

from goblins.entities.creatures.goblin import Goblin
from goblins.core import GlobalSingleton, WORLD_LAYERS
from goblins.entities.plants.pumpkin import Pumpkin
from goblins.world.layer import Layer


class World:
    def __init__(self):
        self.layer_list = list()
        self.entity_list = list()
        self.generate()
        self.global_singleton = GlobalSingleton()

    def generate(self):
        for i in range(WORLD_LAYERS):
            self.layer_list.append(Layer(self))
        for i in range(3000):
            new_goblin = Goblin(self.layer_list[0])
            new_goblin.position.x = random.randint(100, 900)
            new_goblin.position.y = random.randint(100, 900)
            new_goblin.update_speed = random.randint(20, 2000)
            self.entity_list.append(new_goblin)

            new_pumpkin = Pumpkin(self.layer_list[0])
            new_pumpkin.position.x = random.randint(100, 900)
            new_pumpkin.position.y = random.randint(100, 900)
            self.entity_list.append(new_pumpkin)

    def draw(self, surface):
        for entity in self.entity_list:
            entity.draw(surface)

    def tick(self):
        for entity in self.entity_list:
            entity.tick()

    def update(self):
        for entity in self.entity_list:
            entity.tick()