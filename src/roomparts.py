import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from tilemap import *
from maputils import *

def makePlatform(startX, y, width, leftEndBlock=True, rightEndBlock=True):
        endX = 4 * width + startX
        for x in range(startX, endX, 4):  
            tileSet.putBlock(ground, "floor", x, y)
        if leftEndBlock: tileSet.putBlock(ground, "floorLeft",  (startX - 1), y)
        if rightEndBlock: tileSet.putBlock(ground, "floorRight", (endX      ), y)
  


    # Kirjahylly!
def kirjahylly(tileSet, furniture, x, y, w, h):
   for ty in range(y, y+h*4, 4):
      for tx in range(x+1, x+w*4+1, 4):  
            tileSet.putBlock(furniture, "bookshelf", tx, ty)
      tileSet.putBlock(furniture, "bookshelfEdgeLeft", x, ty)
      tileSet.putBlock(furniture, "bookshelfEdgeRight", x+w*4+1, ty)
