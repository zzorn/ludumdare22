# The map data for the whole game
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from tilemap import *
from maputils import *


class World:
    def __init__(self, tileSize):
        self.tileSize = tileSize
        self.mapBuilder = MapBuilder(tileSize)
                
    # Sets up world to start positions
    def start(self):
        self.currentRoom = self.createStartRoom()    

    def createStartRoom(self):
        startRoom = TileMap(self.tileSize, 40, 20)
        bg = startRoom.addTileLayer('background')
        startRoom.addEntityLayer('entities')
        startRoom.addEntityLayer('player')
        startRoom.addTileLayer('foreground')

        for i in range(0,10):
            self.mapBuilder.addBlock(bg, "stone", i * 4, 0*4)
            self.mapBuilder.addBlock(bg, "wall",  i * 4, 2*4)
            self.mapBuilder.addBlock(bg, "wall",  i * 4, 1*4)
            self.mapBuilder.addBlock(bg, "stone", i * 4, 3*4)

        return startRoom


