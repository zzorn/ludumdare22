# A map consisting of tiled images, and entities in it.
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
import tmxloader
from camera import *
from entity import *


class TileType:
    def __init__(self, image, blocking = False, climbable = False, swimmable = False):
        self.image = image
        self.blocking = blocking
        self.climbable = climbable
        self.swimmable = swimmable

    def draw(self, camera, x, y):
        camera.drawImage(self.image, x, y)

class Layer:

    def draw(self, camera):
        return

    def update(self, durationSeconds):
        return
        
    def blockingAt(self, x, y):
        return False    
    
    def climbableAt(self, x, y):
        return False    

    def swimmableAt(self, x, y):
        return False    
        
    def getOverlappingEntity(self, area):
        return None
        
class EntityLayer(Layer):
    def __init__(self, tileMap):
        self.tileMap = tileMap
        self.entities = []

    def add(self, entity):
        self.entities.append(entity)
        entity.tileMap = self.tileMap

    def remove(self, entity):
        self.entities.remove(entity)
        entity.tileMap = None

    def update(self, durationSeconds):
        for entity in self.entities:
            entity.update(durationSeconds)
    
    def draw(self, camera):
        for entity in self.entities:
            entity.draw(camera)
    
    def getOverlappingEntity(self, area):
        for entity in self.entities:
            if entity.overlaps(area):
                return entity 
        return None        
                       

class TileLayer(Layer):
    def __init__(self, tileMap):
        self.tileMap = tileMap
        self.tiles = [None] * tileMap.tileCount()
        
    # Returns True if the specified tile coordinate is in the map area.    
    def tilePosOnMap(self, tileX, tileY):
        return (0 <= tileX < self.tileMap.sizeX and
                0 <= tileY < self.tileMap.sizeY)
    
        
    def setTile(self, tileX, tileY, tileType):
        if self.tilePosOnMap(tileX, tileY):
            self.tiles[self.tileMap.sizeX * tileY + tileX] = tileType
        
    def getTile(self, tileX, tileY):
        if self.tilePosOnMap(tileX, tileY):
            return self.tiles[self.tileMap.sizeX * tileY + tileX]
        else:
            return None

    def blockingAt(self, x, y):
        t = self.getTileAtPixel(x, y)
        if t is None:
            return False
        else:
            return t.blocking
    
    def climbableAt(self, x, y):
        t = self.getTileAtPixel(x, y)
        if t is None:
            return False
        else:
            return t.climbable    
            
    def swimmableAt(self, x, y):
        t = self.getTileAtPixel(x, y)
        if t is None:
            return False
        else:
            return t.swimmable
            

    def getTileAtPixel(self, x, y):
        # Round down to the tile coordinates that the point is in
        tileX = self._tileForPixel(x)
        tileY = self._tileForPixel(y)
        return self.getTile(tileX, tileY)

    def _tileForPixel(self, c):
        return int(math.floor(c / self.tileMap.tileSize))
        

    def draw(self, camera):
        # Get the range of tiles in the visible area
        tileStartX = self._tileForPixel(camera.visibleArea.left)
        tileStartY = self._tileForPixel(camera.visibleArea.top)
        tileEndX   = self._tileForPixel(camera.visibleArea.right) + 1
        tileEndY   = self._tileForPixel(camera.visibleArea.bottom) + 1

        # Draw each tile in the visible area
        tileSize = self.tileMap.tileSize
        for ty in range(tileStartY, tileEndY):
            for tx in range(tileStartX, tileEndX):
                tileType = self.getTile(tx, ty)
                if tileType is not None:
                    x = tx * tileSize
                    y = ty * tileSize
                    tileType.draw(camera, x, y)
                

class TileMap:

    def __init__(self, tileSize, sizeX, sizeY):
    
        self.tileSize = tileSize
        self.sizeX    = sizeX
        self.sizeY    = sizeY
        
        self.layers       = []
        self.namedLayers  = {}
    
        ## Load map
        #self.tiledMap = tmxloader.load_pygame("maps/" + name + ".tmx")
        #self.entities = EntityGroup()
        #for obj in self.tiledMap.getObjects():
        #    entity = createEntity(obj)
        #    if not entity == None:
        #        self.add(entity)

        ## Find the solid layers we can walk on                
        #self.solidLayers = []
        #for layer in self.tiledMap.layers:
        #    if hasattr(layer, 'layerType') and layer.layerType == "solid":
        #        self.solidLayers.append(layer)

    # Adds a layer for tiles with the specified name
    def addTileLayer(self, name):
        return self._addLayer(name, TileLayer(self))

    # Adds a layer for entities (moving game objects) with the specified name
    def addEntityLayer(self, name):
        return self._addLayer(name, EntityLayer(self))

    def _addLayer(self, name, layer):
        self.layers.append(layer)
        self.namedLayers[name] = layer      
        return layer

    # Return the layer with the specified name
    def getLayer(self, name):
        return self.namedLayers[name]

    def tileCount(self):
        return self.sizeX * self.sizeY

    def update(self, frameDurationSeconds):
        for layer in self.layers:
            layer.update(frameDurationSeconds)

    def draw(self, camera):
        for layer in self.layers:
            layer.draw(camera)

    # Test to see if there is solid wall at the specified pixel coordinates
    def blockingAt(self, x, y):
        for layer in self.layers:
            if layer.blockingAt(x, y):
                return True
        return False            

    def climbableAt(self, x, y):
        for layer in self.layers:
            if layer.climbableAt(x, y):
                return True
        return False            

    def swimmableAt(self, x, y):
        for layer in self.layers:
            if layer.swimmableAt(x, y):
                return True
        return False            


    # Returns first entity overlapping the specified entity, or None if none found.
    def getOverlappingEntity(self, target):
        area = target.area()
        for layer in self.layers:
            entity = layer.getOverlappingEntity(area)
            if not entity == None:
                return entity
        return None
                
    
    
    

