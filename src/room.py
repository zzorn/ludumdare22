# Utilities for map
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
import tmxloader
from camera import *
from entity import *

def nop():
    return

tileSize = 64

# An area
class Room:

    def __init__(self, name):
        # Load map
        self.tiledMap = tmxloader.load_pygame("maps/" + name + ".tmx")
        self.entities = EntityGroup()
        for obj in self.tiledMap.getObjects():
            entity = createEntity(obj)
            if not entity == None:
                self.add(entity)

        # Find the solid layers we can walk on                
        self.solidLayers = []
        for layer in self.tiledMap.layers:
            if hasattr(layer, 'layerType') and layer.layerType == "solid":
                self.solidLayers.append(layer)

    def add(self, entity):
        self.entities.add(entity)
        entity.room = self

    def remove(self, entity):
        self.entities.remove(entity)
        entity.room = None


    def update(self, frameDurationSeconds):
        self.entities.update(frameDurationSeconds)

    # Test to see if there is solid wall at the specified pixel coordinates
    def solidAt(self, x, y):
        tileX = int(math.floor(x / tileSize))
        tileY = int(math.floor(y / tileSize))
        for solidLayer in self.solidLayers:
            for testTileY in range(tileY - 4, tileY + 4):
                for testTileX in range(tileX - 4, tileX + 4):
                    tileImage = self.tiledMap.getTileImageForLayer(testTileX, testTileY, solidLayer)
                    if not tileImage == 0 and not tileImage == None:
                        w, h = tileImage.get_rect().size
                        inImageX = int(testTileX * tileSize - x)
                        inImageY = int(testTileY * tileSize - y)
                        if 0 <= inImageX < w and 0 <= inImageY < h:
                            pixel = tileImage.get_at((inImageX, inImageY))
                            return pixel[3] > 128 # If alpha is more than half transparent, it's solid
        
        return False

    def draw(self, surface, camera):
        # Loop through all visible tiles in this room, and draw them at their positions
        tileSize = 64
        w = surface.get_rect().width / tileSize
        h = surface.get_rect().height / tileSize
        layerNum = 0
        for layer in self.tiledMap.layers:
            for ty in range(0, h + 4):
                for tx in range(-4, w):
                    tileImage = self.tiledMap.getTileImage(tx + camera.tileX, ty + camera.tileY, layerNum)
                    if (not tileImage == None) and (not tileImage == 0):
                        iw = tileImage.get_rect().width
                        ih = tileImage.get_rect().height
                        pos = (tx * tileSize, ty * tileSize - ih + tileSize)
                        surface.blit(tileImage, pos)
            layerNum += 1
        
        # Draw all entities (characters, powerups, enemies, doors, etc)
        self.entities.draw(surface, camera)


