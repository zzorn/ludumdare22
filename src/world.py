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
        self.rooms = {}
                
    # Sets up world to start positions
    def start(self):        
        startRoom = createRoom01(self.tileSet)
        self.addRoom("startRoom", startRoom)
        self.addRoom("chairRoom", createRoom01(self.tileSet))
        self.currentRoom = startRoom

    # get room with given name
    def getRoom(self, roomName):
        return self.rooms[roomName]

    def addRoom(self, roomName, room):
        room.world = self
        self.rooms[roomName] = room

    # Moves the specified (player) entity to the specified room and entry position
    def enterRoom(self, roomName, entryPosName, player):
        # Remove player from old room
        if not player.tileMap is None:
             player.tileMap.remove(player)

        # Add player to new room
        room = self.getRoom(roomName)
        room.getLayer('player').add(player)
        
        # Find entry position for player, and place player at it
        entryPosEntity = room.getEntityNamed(entryPosName)
        if not entryPosEntity is None:
            player.x = entryPosEntity.x
            player.y = entryPosEntity.y
        


    

