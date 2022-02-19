import pygame
from pygame.locals import *

from goblins.core import WINDOW_WIDTH, WINDOW_HEIGHT
from goblins.world import World


class Game:
    def __init__(self):
        self._running = True
        self._clock = None
        self._display_surf = None
        self.size = self.width, self.height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.world = World()

    def on_init(self):
        try:
            pygame.init()
            self._clock = pygame.time.Clock()
            self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
            return True
        except:
            return False

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self._clock.tick(30)

    def on_render(self):
        self.world.layer_list[0].draw(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self._running = self.on_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


