import pygame

import random
from goblins.entities.creatures.creature import Creature
from goblins.core import Position


class Goblin(Creature):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('goblins/assets/goblin_basic.png').convert_alpha()
        if random.randint(1, 2) == 1:
            self.flower_img = pygame.image.load('goblins/assets/dandelion_flower.png').convert_alpha()
            self.img.blit(self.flower_img, (0, 8))
        self.surface = self.img

    def update(self):
        new_position = Position(random.randint(-1, 1), random.randint(-1, 1))
        if new_position.x < 0:
            self.surface = pygame.transform.flip(self.img, True, False)
        else:
            self.surface = self.img
        self.position.move_to(self.position + new_position)

