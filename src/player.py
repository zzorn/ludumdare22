
from entity import *

class Player(Entity):
    def __init__(self, x, y, image):
        Entity.__init__(self, x, y, image, physics=True)


