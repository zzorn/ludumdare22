# The map data for the whole game
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from room import *

class World:
    def __init__(self):
        return
                
    # Sets up world to start positions
    def start(self):
        self.currentRoom = self.createStartRoom()

    

    def createStartRoom(self):
        startRoom = Room("startroom")

        return startRoom


