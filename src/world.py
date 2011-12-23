# The map data for the whole game
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from tilemap import *
from maputils import *
from room01 import *

class World:
    def __init__(self, tileSize, tileSet):
        self.tileSize = tileSize
        self.tileSet = tileSet
                
    # Sets up world to start positions
    def start(self):
        self.currentRoom = createRoom01(self.tileSet)


