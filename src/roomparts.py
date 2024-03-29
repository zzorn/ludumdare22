import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from tilemap import *
from maputils import *

# Floor
def makePlatform(tileSet, layer, startX, y, width, leftEndBlock=True, rightEndBlock=True):
        endX = 4 * width + startX
        for x in range(startX, endX, 4):  
            tileSet.putBlock(layer, "floor", x, y)
        if leftEndBlock: tileSet.putBlock(layer, "floorLeft",  (startX - 1), y)
        if rightEndBlock: tileSet.putBlock(layer, "floorRight", (endX      ), y)
  


# Kirjahylly!
def kirjahylly(tileSet, layer, x, y, w, h):
   for ty in range(y, y+h*4, 4):
      for tx in range(x+1, x+w*4+1, 4):  
            tileSet.putBlock(layer, "bookshelf", tx, ty)
      tileSet.putBlock(layer, "bookshelfEdgeLeft", x, ty)
      tileSet.putBlock(layer, "bookshelfEdgeRight", x+w*4+1, ty)


# Muta
# mud arvot (tileset, layer, alkux, alkuy, leveys aina 4 kertaa, korkeus aina 4 kertaa)
def mud(tileSet, layer, x, y, w, h):
   # Pinta
   for tx in range(x, x+w*4, 4):
      tileSet.putBlock(layer, "mudSurface", tx, y)

   # Deep Mud
   for ty in range(y+4, y+h*4, 4):  
      for tx in range(x, x+w*4, 4):
         tileSet.putBlock(layer, "mud", tx, ty) 


