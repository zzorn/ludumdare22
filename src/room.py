# Utilities for map
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
import tmxloader
from camera import *

def nop():
    return

# An area
class Room:

    def __init__(self, name):
        # Load map
        self.tiledMap = tmxloader.load_pygame("maps/" + name + ".tmx")

    def update(self, frameDurationSeconds):
        


    def draw(self, surface, camera):
        # Loop through all visible tiles in this room, and draw them at their positions
        tileSize = 64
        w = surface.get_rect().width / tileSize
        h = surface.get_rect().height / tileSize
        layerNum = 0
        for layer in self.tiledMap.layers:
            for ty in range(0, h + 4):
                for tx in range(-4, w):
                    tileImage = self.tiledMap.getTileImage(tx + camera.x, ty + camera.y, layerNum)
                    if (not tileImage == None) and (not tileImage == 0):
                        iw = tileImage.get_rect().width
                        ih = tileImage.get_rect().height
                        pos = (tx * tileSize, ty * tileSize - ih + tileSize)
                        surface.blit(tileImage, pos)
            layerNum += 1
    


