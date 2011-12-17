# Utilities for map
import pygame, random, math
from pygame.locals import *
from resourcemanager import *

# Some type of block
class Tile:
    def __init__(self, imageName):
        self.image = imageManager.get(imageName)
    
    def draw(self, surface, x, y):
        surface.blit(self.image, pos)


# An area
class Room:

    def __init__(self):
        # tilePositions stores what tiles are at specific positions
        tilePositions = {}

    # Set tile at specific location
    def setTile(self, pos, tile):
        tilePositions[pos] = tile
        
    def draw(self, surface, x, y):
        # Loop through all tiles in this room, and draw them at their positions
        for pos, tile in tilePositions:
            # TODO: Only draw the tile if it is visible on the surface
            tile.draw(surface, x + pos[0], y + pos[1])
        
    


