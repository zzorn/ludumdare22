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
        mapSizey = 50
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

        # lattiat eli ne josta kasvaa esim ruohoa kaytta def makePlatformia
 #       makePlatform(16, 14, 2)
 #       makePlatform(30, 16, 4)

        # Mud at bottom
 #       for x in range(0,20*4, 4):
 #           self.mapBuilder.addBlock(bg, "mud", x, 24)     



            
        #reunat ala koske
        for x in range(0,mapSizex, 4 ):
            for y in range(0,9,4):
                self.mapBuilder.addBlock(bg, "stone", x , y )
        for x in range(0,13,4 ):
            for y in range(0,mapSizey, 4):
                self.mapBuilder.addBlock(bg, "stone", x , y )
        for x in range(mapSizex-16,mapSizex, 4 ):
            for y in range(0,mapSizey, 4):
                self.mapBuilder.addBlock(bg, "stone", x , y )
        for x in range(0,mapSizex, 4 ):
            for y in range(mapSizey-12,mapSizey, 4):
                self.mapBuilder.addBlock(bg, "stone", x , y )







        

       # etukivet eli lattia mutaa ei se paalle tuleva vaa se nelio
        for i in range(16, 21, 4):
            self.mapBuilder.addBlock(bg, "stone", i , 24)

        for x in range(0, mapSizex):
            for y in range(0,mapSizey):
                self.mapBuilder.addBlock(backWall, "wall", x * 4, y * 4)     

        return startRoom


