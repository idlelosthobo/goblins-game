import pygame
from pygame.locals import *

from goblins.core import WINDOW_WIDTH, WINDOW_HEIGHT
from goblins.interface.camera import Camera
from goblins.world import World


class Game:
    def __init__(self):
        self.running = True
        self.camera = Camera()
        self.clock = None
        self.display_surf = None
        self.size = self.width, self.height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.world = World()

    def on_init(self):
        try:
            pygame.init()
            self.clock = pygame.time.Clock()
            self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
            return True
        except:
            return False

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.camera.scroll_north()
            if event.key == K_s:
                self.camera.scroll_south()
            if event.key == K_a:
                self.camera.scroll_west()
            if event.key == K_d:
                self.camera.scroll_east()
            if event.key == K_ESCAPE:
                self.running = False
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        self.clock.tick(30)
        self.camera.scroll()

    def on_render(self):
        self.world.layer_list[0].draw(self.display_surf, self.camera.translate_world_x, self.camera.translate_world_y)
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


