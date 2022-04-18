import random

import pygame

from goblins.entities.plants.plant import Plant


class Pumpkin(Plant):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('goblins/assets/pumpkin.png').convert_alpha()
        self.surface = self.img
