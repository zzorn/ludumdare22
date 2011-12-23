import random
import tilemap
import resourcemanager

# Several tiles used together
class TileBlock:
    # Create a new TileBlock, using the specified image, containing tiles of tileSize, using a block of tiles starting 
    # from tileX,tileY, which is blockW number of tiles wide, and blockH tiles high.
    # If blocking is true the tiles are not walkable, if water is true they are water / mud tiles,
    # if climbable is true they can be climbed on.
    def __init__(self, imageName, tileSize, tileX, tileY, blockW, blockH, blocking = False, swimmable = False, climbable=False):
        self.blockW = blockW
        self.blockH = blockH
        self.tiles = []
        
        for y in range(tileY, tileY + blockH):
            for x in range(tileX, tileX + blockW):
                image = resourcemanager.imageManager.getTile(imageName, x, y, tileSize)
                tileType = tilemap.TileType(image, blocking, climbable, swimmable)
                self.tiles.append(tileType)
        
                
    def putBlock(self, tileLayer, tileX, tileY):
        i = 0
        for y in range(0, self.blockH):
            for x in range(0, self.blockW):
                tileLayer.setTile(tileX + x, tileY + y, self.tiles[i])
                i += 1
        

class RandomBlock:
    def __init__(self, alternativeWeights):
        self.alternatives = []
        for alternative, weight in alternativeWeights.iteritems():
            self.addAlternative(alternative, weight)

    def addAlternative(self, alternativeBlock, weight):
        for i in range(0, weight):
            self.alternatives.append(alternativeBlock)
        
    def add(self, tileLayer, tileX, tileY):
        random.choice(self.alternatives).add(tileLayer, tileX, tileY)
        

# Contains set of named tiles and tile blocks loaded from image files.
class TileSet:
    def __init__(self, tileSize):
        self.tileSize = tileSize
        
        blocks = {}
        self.blocks = blocks

    def add(self, blockName, imageName, tileX, tileY, blockW, blockH, blocking=False, swimmable=False, climbable=False):
        blocks[blockName] = TileBlock(imageName, tileSize, tileX, tileY, blockW, blockH, blocking, swimmable, climbable)

    def addRandomAlternative(self, blockName, otherBlock, weight=1):
        randomBlock = blocks[blockName]
        if randomBlock is None:
            randomBlock = new RandomBlock({})
        elif randomBlock is not RandomBlock:
            raise ("Can not add random alternative to "+blockName+", it's not a random block!")

        randomBlock.addAlternative(otherBlock, weight)


    def putBlock(self, tileLayer, blockName, tileX, tileY):
        self.blocks[blockName].putBlock(tileLayer, tileX, tileY)


