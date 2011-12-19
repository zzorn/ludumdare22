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
        startRoom = TileMap(self.tileSize, 100, 20)
        backWall = startRoom.addTileLayer('backWall')
        bg = startRoom.addTileLayer('background')
        startRoom.addEntityLayer('entities')
        startRoom.addEntityLayer('player')
        startRoom.addTileLayer('foreground')

        for i in range(0,3):
            self.mapBuilder.addBlock(bg, "stone", i * 4, 12)
        for i in range(4,6):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)-1, 11)
        for i in range(7,9):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)+3, 16)
        for i in range(10,13):
            self.mapBuilder.addBlock(bg, "stone", (i * 4), 15)
        for i in range(13,15):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)+1, 14)
        for i in range(15,19):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)+1, 16)     

        for x in range(0, 20):
            for y in range(0,20):
                self.mapBuilder.addBlock(backWall, "wall", x * 4, y * 4)     

        return startRoom


