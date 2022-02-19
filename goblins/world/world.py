from goblins.objects.goblin import Goblin
from goblins.core import WORLD_LAYERS
from goblins.world.layer import Layer

class World:
    def __init__(self):
        self.layer_list = list()
        self.object_list = list()
        self.generate()

    def generate(self):
        for i in range(WORLD_LAYERS):
            self.layer_list.append(Layer())
        self.object_list.append(Goblin())

    def draw(self, surface):
        for object in self.object_list:
            object.draw(surface)