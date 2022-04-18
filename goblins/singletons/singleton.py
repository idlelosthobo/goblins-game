from goblins.core import Position


class Singleton(object):
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    
class GlobalSingleton(Singleton):
    delta_time = int()
    world_translate = Position()

