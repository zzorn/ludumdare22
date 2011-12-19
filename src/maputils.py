import random
import tilemap
import resourcemanager

class TileBlock:
    def __init__(self, imageName, tileSize, tx, ty, blockSize, blocking = False):
        self.blockSize = blockSize
        self.tiles = []
        
        for y in range(tx * blockSize, (tx + 1) * blockSize):
            for x in range(ty * blockSize, (ty + 1) * blockSize):
                self.tiles.append(tilemap.TileType(resourcemanager.imageManager.getTile(imageName, x, y, tileSize), blocking))
                
    def add(self, tileLayer, tileX, tileY):
        i = 0
        for y in range(0, self.blockSize):
            for x in range(0, self.blockSize):
                tileLayer.setTile(tileX + x, tileY + y, self.tiles[i])
                i += 1
        

class RandomBlock:
    def __init__(self, alternatives):
        self.alternatives = alternatives
        
    def add(self, tileLayer, tileX, tileY):
        random.choice(self.alternatives).add(tileLayer, tileX, tileY)
        

class MapBuilder:
    def __init__(self, tileSize):
        self.tileSize = tileSize
        
        blocks = {}
        self.blocks = blocks

        blocks["stone_1"] = TileBlock("wall", tileSize, 0, 0, 4, blocking = True)
#        blocks["stone_2"] = TileBlock("wall", tileSize, 1, 0, 4, blocking = True)
#        blocks["stone_3"] = TileBlock("wall", tileSize, 2, 0, 4, blocking = True)
#        blocks["stone_4"] = TileBlock("wall", tileSize, 3, 0, 4, blocking = True)
#        blocks["stone"]   = RandomBlock([blocks["stone_1"], blocks["stone_2"], blocks["stone_3"], blocks["stone_4"]])


    def addBlock(self, tileLayer, blockName, tileX, tileY):
        self.blocks[blockName].add(tileLayer, tileX, tileY)


