from goblins.core import Position


class GlobalSingleton(object):
    _shared_dict = {}

    def __init__(self):
        self._shared_dict['delta_time'] = int()
        self._shared_dict['world_translate'] = Position()

    def get_delta_time(self): return self._shared_dict['delta_time']
    def set_delta_time(self, delta_time): self._shared_dict['delta_time'] = delta_time

    delta_time = property(get_delta_time, set_delta_time)

    def get_world_translate(self): return self._shared_dict['world_translate']
    def set_world_translate(self, position): self._shared_dict['world_translate'] = position

    world_translate = property(get_world_translate, set_world_translate)

