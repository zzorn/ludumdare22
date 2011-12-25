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
        
    def putBlock(self, tileLayer, tileX, tileY):
        random.choice(self.alternatives).putBlock(tileLayer, tileX, tileY)
        


class CombinedBlock:
    def __init__(self):
        self.blocks = {}

    def addBlock(self, componentBlock, x, y):
        self.blocks[(x, y)] = componentBlock
        
    def putBlock(self, tileLayer, tileX, tileY):
        for pos in self.blocks:
            self.blocks[pos].putBlock(tileLayer, tileX + pos[0], tileY + pos[1]) 
        

# Contains set of named tiles and tile blocks loaded from image files.
class TileSet:
    def __init__(self, tileSize):
        self.tileSize = tileSize
        
        self.blocks = {}

    def add(self, blockName, imageName, tileX, tileY, blockW, blockH, blocking=False, swimmable=False, climbable=False):
        self.blocks[blockName] = TileBlock(imageName, self.tileSize, tileX, tileY, blockW, blockH, blocking, swimmable, climbable)

    def addRandomAlternative(self, blockName, otherBlock, weight=1):
        if blockName in self.blocks:
            randomBlock = self.blocks[blockName]
            if randomBlock is not RandomBlock:
                print("ERROR: Can not add random alternative to "+blockName+", it's not a random block!")
                # TODO: Throw exception
        else:
            randomBlock =  RandomBlock({})
            self.blocks[blockName] = randomBlock
            

        randomBlock.addAlternative(self.blocks[otherBlock], weight)


    def addCombinedBlock(self, blockName, otherBlock, x, y):
        if blockName in self.blocks:
            combinedBlock = self.blocks[blockName]
            if combinedBlock is not CombinedBlock:
                print("ERROR: Can not add component to "+blockName+", it's not a combined block!")
                # TODO: Throw exception
        else:
            combinedBlock = CombinedBlock()
            self.blocks[blockName] = combinedBlock
            

        combinedBlock.addBlock(self.blocks[otherBlock], x, y)


    def putBlock(self, tileLayer, blockName, tileX, tileY):
        self.blocks[blockName].putBlock(tileLayer, tileX, tileY)


