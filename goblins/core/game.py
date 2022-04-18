import logging

import pygame
from pygame.locals import *

from goblins.core import WINDOW_WIDTH, WINDOW_HEIGHT
from goblins.interface.camera import Camera
from goblins.singletons import GlobalSingleton
from goblins.world import World
from goblins.entities import Goblin


class Game:
    def __init__(self):
        self.running = True
        self.camera = Camera()
        self.clock = None
        self.display_surface = None
        self.font = None
        self.global_singleton = None
        self.size = self.width, self.height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.world = None

    def on_init(self):
        try:
            logging.debug(f'Game: Starting')
            pygame.init()
            pygame.font.init()
            self.font = pygame.font.SysFont('Arial', 12)
            self.global_singleton = GlobalSingleton()
            self.clock = pygame.time.Clock()
            self.display_surface = pygame.display.set_mode(self.size, pygame.SCALED | pygame.RESIZABLE)
            self.world = World()
            logging.debug(f'Game: Loaded Successfully')
            return True
        except Exception as e:
            logging.error(f'Game: {e}')
            logging.error(f'Game: Failed to Load')
            return False


    def on_event(self, event):
        keys = pygame.key.get_pressed()

        if keys[K_w]:
            self.camera.scroll_north()
        if keys[K_s]:
            self.camera.scroll_south()
        if keys[K_a]:
            self.camera.scroll_west()
        if keys[K_d]:
            self.camera.scroll_east()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        self.global_singleton.delta_time = self.clock.tick(60)
        self.camera.update()
        self.world.update()

    def on_render(self):
        self.world.layer_list[0].draw(self.display_surface)
        self.world.draw(self.display_surface)
        self.display_surface.blit(self.font.render(f'{self.clock.get_fps():.2f}', False, (0, 0, 0)), (2, 2))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.running = self.on_init()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


