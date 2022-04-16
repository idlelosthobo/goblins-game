import logging

from goblins.core.game import Game
from goblins.core.config import DEBUG

FORMAT = '%(levelname)s [%(asctime)-15s] %(message)s'

if DEBUG:
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
else:
    logging.basicConfig(format=FORMAT, level=logging.ERROR)
