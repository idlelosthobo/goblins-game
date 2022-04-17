from goblins.entities.goblin import Goblin
from goblins.core import WORLD_LAYERS
from goblins.singletons import GlobalSingleton
from goblins.world.layer import Layer


class World:
    def __init__(self):
        self.layer_list = list()
        self.object_list = list()
        self.generate()
        self.global_singleton = GlobalSingleton()

    def generate(self):
        for i in range(WORLD_LAYERS):
            self.layer_list.append(Layer())
        new_goblin = Goblin()
        new_goblin.position.x = 10
        new_goblin.position.y = 12
        self.object_list.append(new_goblin)

    def draw(self, surface):
        for object in self.object_list:
            object.draw(surface)

    def tick(self):
        for object in self.object_list:
            object.tick()

    def update(self):
        for object in self.object_list:
            object.tick()