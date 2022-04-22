import random

import pygame

from goblins.entities.plants.plant import Plant


class Pumpkin(Plant):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img = pygame.image.load('goblins/assets/pumpkin.png').convert_alpha()
        self.surface = self.img

