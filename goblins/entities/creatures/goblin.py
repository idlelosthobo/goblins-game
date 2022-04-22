import pygame

import random
from goblins.entities.creatures.creature import Creature
from goblins.core import Position


class Goblin(Creature):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img = pygame.image.load('goblins/assets/goblin_basic.png').convert_alpha()
        if random.randint(1, 2) == 1:
            self.flower_img = pygame.image.load('goblins/assets/dandelion_flower.png').convert_alpha()
            self.img.blit(self.flower_img, (0, 8))
        self.surface = self.img

    def update(self):
        self.think()
        new_position = Position(random.randint(-1, 1), random.randint(-1, 1))
        if new_position.x < 0:
            self.surface = pygame.transform.flip(self.img, True, False)
        else:
            self.surface = self.img
        self.position.move_to(self.position + new_position)
        self.draw_has_changed = True

    def think(self, count=0):
        if count == 1000:
            print(f'{self = } Maximum Count')
        if random.randint(1, 50) != 1 and count < 1000:
            count += 1
            self.think(count)

