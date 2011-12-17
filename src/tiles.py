# A set of tiles used in the game
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from room import *

# Some type of block
class Tile:
    def __init__(self, imageName, area = None):
        self.image = imageManager.get(imageName, area)
    
    def draw(self, surface, x, y):
        surface.blit(self.image, (x, y))


wallSize = 256

def tileSheetPos(x, y, size):
    return Rect(x * size, y* size, size, size)
    
wall1 = Tile("wall", tileSheetPos(0, 0, wallSize))
wall2 = Tile("wall", tileSheetPos(1, 0, wallSize))
wall3 = Tile("wall", tileSheetPos(2, 0, wallSize))
wall4 = Tile("wall", tileSheetPos(3, 0, wallSize))
wallTiles = [wall1, wall2, wall3, wall4]










