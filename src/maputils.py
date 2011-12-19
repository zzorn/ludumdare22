import random
import tilemap
import resourcemanager

class TileBlock:
    def __init__(self, imageName, tileSize, tx, ty, blockSize, blocking = False, transparent = False, water = False):
        self.blockSize = blockSize
        self.tiles = []
        
        for y in range(ty * blockSize, (ty + 1) * blockSize):
            for x in range(tx * blockSize, (tx + 1) * blockSize):
                image = resourcemanager.imageManager.getTile(imageName, x, y, tileSize, transparent)
                tileType = tilemap.TileType(image, blocking, swimmable = water)
                self.tiles.append(tileType)
                
    def add(self, tileLayer, tileX, tileY):
        i = 0
        for y in range(0, self.blockSize):
            for x in range(0, self.blockSize):
                tileLayer.setTile(tileX + x, tileY + y, self.tiles[i])
                i += 1
        

class RandomBlock:
    def __init__(self, alternativeWeights):
        self.alternatives = []
        for alternative, weight in alternativeWeights.iteritems():
            for i in range(0, weight):
                self.alternatives.append(alternative)
        
    def add(self, tileLayer, tileX, tileY):
        random.choice(self.alternatives).add(tileLayer, tileX, tileY)
        

class MapBuilder:
    def __init__(self, tileSize):
        self.tileSize = tileSize
        
        blocks = {}
        self.blocks = blocks

        print("start preparing blocks")
        blockSize = 4
        blocks["wall_1"] = TileBlock("wall", tileSize, 0, 0, blockSize, blocking = False, transparent = True) # TODO: Keep transparent things together
        blocks["wall_2"] = TileBlock("wall", tileSize, 1, 0, blockSize, blocking = False)
        blocks["wall_3"] = TileBlock("wall", tileSize, 2, 0, blockSize, blocking = False)
        blocks["wall_4"] = TileBlock("wall", tileSize, 3, 0, blockSize, blocking = False)
        blocks["wall"]   = RandomBlock({blocks["wall_1"]: 3, 
                                        blocks["wall_2"]: 2, 
                                        blocks["wall_3"]: 1, 
                                        blocks["wall_4"]: 2})

        blocks["stone_1"] = TileBlock("wall", tileSize, 0, 1, blockSize, blocking = True)
        blocks["stone_2"] = TileBlock("wall", tileSize, 1, 1, blockSize, blocking = True)
        blocks["stone_3"] = TileBlock("wall", tileSize, 2, 1, blockSize, blocking = True)
        blocks["stone_4"] = TileBlock("wall", tileSize, 3, 1, blockSize, blocking = True)
        blocks["stone"]   = RandomBlock({blocks["stone_1"]: 2, 
                                         blocks["stone_2"]: 2, 
                                         blocks["stone_3"]: 2, 
                                         blocks["stone_4"]: 2})

        blocks["ground_1"] = TileBlock("wall", tileSize, 1, 2, blockSize, blocking = True, transparent = True)
        blocks["ground_2"] = TileBlock("wall", tileSize, 2, 2, blockSize, blocking = True, transparent = True)
        blocks["ground_3"] = TileBlock("wall", tileSize, 0, 3, blockSize, blocking = True, transparent = True)
        blocks["ground_4"] = TileBlock("wall", tileSize, 1, 3, blockSize, blocking = True, transparent = True)
        blocks["ground"]   = RandomBlock({blocks["ground_1"]: 1, 
                                          blocks["ground_2"]: 3, 
                                          blocks["ground_3"]: 2, 
                                          blocks["ground_4"]: 2})

        blocks["ground_left"] = TileBlock("wall", tileSize, 0, 2, blockSize, blocking = False, transparent = True)
        blocks["ground_right"] = TileBlock("wall", tileSize, 2, 3, blockSize, blocking = False, transparent = True)

        blocks["mud_1"] = TileBlock("wall", tileSize, 3, 2, blockSize, blocking = False, transparent = True, water = True)
        blocks["mud_2"] = TileBlock("wall", tileSize, 3, 3, blockSize, blocking = False, transparent = True, water = True)
        blocks["mud"]   = RandomBlock({blocks["mud_1"]: 1, 
                                       blocks["mud_2"]: 1})

        print("end preparing blocks")


    def addBlock(self, tileLayer, blockName, tileX, tileY):
        self.blocks[blockName].add(tileLayer, tileX, tileY)


