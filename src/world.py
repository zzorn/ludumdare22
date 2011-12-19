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
        mapSizex = 100
        mapSizey = 100
        startRoom = TileMap(self.tileSize ,mapSizex ,mapSizey)
        backWall = startRoom.addTileLayer('backWall')
        bg = startRoom.addTileLayer('solid')
        ground = startRoom.addTileLayer('ground')
        startRoom.addEntityLayer('entities')
        startRoom.addEntityLayer('player')
        startRoom.addTileLayer('foreground')

        
        def makePlatform(startX, y, width):
            endX = 4 * width + startX
            for x in range(startX, endX, 4):  
                self.mapBuilder.addBlock(bg, "stone", x, y)
                self.mapBuilder.addBlock(ground, "ground", x, y)
            self.mapBuilder.addBlock(ground, "ground_left",  (startX - 4), y)
            self.mapBuilder.addBlock(ground, "ground_right", (endX      ), y)

        # Walkable platforms
        makePlatform(16, 14, 2)
        makePlatform(30, 16, 4)

        # Mud at bottom
        for x in range(0,20*4, 4):
            self.mapBuilder.addBlock(bg, "mud", x, 24)     


        for i in range(0,3):
            self.mapBuilder.addBlock(bg, "stone", i * 4, 12)
            
        #reunat
        for x in range(0,mapSizex ):
            for y in range(0,2):
                self.mapBuilder.addBlock(bg, "stone", x * 4, y * 4)

        

       
        for i in range(4,6):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)-1, 16)
        for i in range(7,9):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)+3, 21)
        for i in range(10,13):
            self.mapBuilder.addBlock(bg, "stone", (i * 4), 20)
        for i in range(13,15):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)+1, 19)
        for i in range(15,19):
            self.mapBuilder.addBlock(bg, "stone", (i * 4)+1, 21)     

        for x in range(0, mapSizex):
            for y in range(0,mapSizey):
                self.mapBuilder.addBlock(backWall, "wall", x * 4, y * 4)     

        return startRoom


