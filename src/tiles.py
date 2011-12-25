import random
import tilemap
import resourcemanager
from tileset import *


def setupTiles(tileSize):
    tiles = TileSet(tileSize)

    # Background wall
    tiles.add("wall1", "walls_solid", 0,  0, 4, 4)
    tiles.add("wall2", "walls_solid", 4,  0, 4, 4)
    tiles.add("wall3", "walls_solid", 8,  0, 4, 4)
    tiles.add("wall4", "walls_solid", 12, 0, 4, 4)
    tiles.addRandomAlternative("wall", "wall1", 3)
    tiles.addRandomAlternative("wall", "wall2", 2)
    tiles.addRandomAlternative("wall", "wall3", 1)
    tiles.addRandomAlternative("wall", "wall4", 2)

    # Walkable stone
    tiles.add("stone1", "walls_solid", 0,  4, 4, 4, blocking=True)
    tiles.add("stone2", "walls_solid", 4,  4, 4, 4, blocking=True)
    tiles.add("stone3", "walls_solid", 8,  4, 4, 4, blocking=True)
    tiles.add("stone4", "walls_solid", 12, 4, 4, 4, blocking=True)
    tiles.addRandomAlternative("stone", "stone1", 3)
    tiles.addRandomAlternative("stone", "stone2", 2)
    tiles.addRandomAlternative("stone", "stone3", 1)
    tiles.addRandomAlternative("stone", "stone4", 2)

    # Slime 
    tiles.add("mud", "walls_solid", 0, 8, 4, 4, swimmable=True)
    tiles.add("mudSurface1", "walls_transparent", 0, 2, 4, 4, swimmable=True)
    tiles.add("mudSurface2", "walls_transparent", 4, 2, 4, 4, swimmable=True)
    tiles.addRandomAlternative("mudSurface", "mudSurface1", 1)
    tiles.addRandomAlternative("mudSurface", "mudSurface2", 1)

    # Floor
    tiles.add("floorLeftTop",  "walls_transparent", 0,  0, 1, 1, blocking=True)
    tiles.add("floorRightTop", "walls_transparent", 19, 0, 1, 1, blocking=True)
    tiles.add("floorShortTop", "walls_transparent", 1,  0, 2, 1, blocking=True)
    tiles.add("floor1Top",     "walls_transparent", 3,  0, 4, 1, blocking=True)
    tiles.add("floor2Top",     "walls_transparent", 7,  0, 4, 1, blocking=True)
    tiles.add("floor3Top",     "walls_transparent", 11, 0, 4, 1, blocking=True)
    tiles.add("floor4Top",     "walls_transparent", 15, 0, 4, 1, blocking=True)

    tiles.add("floorLeftBottom",  "walls_transparent", 0,  1, 1, 1, blocking=False)
    tiles.add("floorRightBottom", "walls_transparent", 19, 1, 1, 1, blocking=False)
    tiles.add("floorShortBottom", "walls_transparent", 1,  1, 2, 1, blocking=False)
    tiles.add("floor1Bottom",     "walls_transparent", 3,  1, 4, 1, blocking=False)
    tiles.add("floor2Bottom",     "walls_transparent", 7,  1, 4, 1, blocking=False)
    tiles.add("floor3Bottom",     "walls_transparent", 11, 1, 4, 1, blocking=False)
    tiles.add("floor4Bottom",     "walls_transparent", 15, 1, 4, 1, blocking=False)

    tiles.addCombinedBlock("floorLeft",  "floorLeftTop",     0, 0)
    tiles.addCombinedBlock("floorLeft",  "floorLeftBottom",  0, 1)
    tiles.addCombinedBlock("floorRight", "floorRightTop",    0, 0)
    tiles.addCombinedBlock("floorRight", "floorRightBottom", 0, 1)
    tiles.addCombinedBlock("floorShort", "floorShortTop",    0, 0)
    tiles.addCombinedBlock("floorShort", "floorShortBottom", 0, 1)
    tiles.addCombinedBlock("floor1", "floor1Top",    0, 0)
    tiles.addCombinedBlock("floor1", "floor1Bottom", 0, 1)
    tiles.addCombinedBlock("floor2", "floor2Top",    0, 0)
    tiles.addCombinedBlock("floor2", "floor2Bottom", 0, 1)
    tiles.addCombinedBlock("floor3", "floor3Top",    0, 0)
    tiles.addCombinedBlock("floor3", "floor3Bottom", 0, 1)
    tiles.addCombinedBlock("floor4", "floor4Top",    0, 0)
    tiles.addCombinedBlock("floor4", "floor4Bottom", 0, 1)

    tiles.addRandomAlternative("floor", "floor1", 3)
    tiles.addRandomAlternative("floor", "floor2", 2)
    tiles.addRandomAlternative("floor", "floor3", 2)
    tiles.addRandomAlternative("floor", "floor4", 1)

    # Bookshelfts front
    tiles.add("bookshelfEdgeLeft1",  "bookshelf", 4, 0, 1, 4, climbable=True)
    tiles.add("bookshelfEdgeLeft2",  "bookshelf", 4, 4, 1, 4, climbable=True)
    tiles.addRandomAlternative("bookshelfEdgeLeft", "bookshelfEdgeLeft1", 1)
    tiles.addRandomAlternative("bookshelfEdgeLeft", "bookshelfEdgeLeft2", 1)

    tiles.add("bookshelfEdgeRight1",  "bookshelf", 9, 0, 1, 4, climbable=True)
    tiles.add("bookshelfEdgeRight2",  "bookshelf", 9, 4, 1, 4, climbable=True)
    tiles.addRandomAlternative("bookshelfEdgeRight", "bookshelfEdgeRight1", 1)
    tiles.addRandomAlternative("bookshelfEdgeRight", "bookshelfEdgeRight2", 1)

    tiles.add("bookshelf1",  "bookshelf", 5, 0, 4, 4, climbable=True)
    tiles.add("bookshelf2",  "bookshelf", 5, 4, 4, 4, climbable=True)
    tiles.add("bookshelf3",  "bookshelf", 5, 8, 4, 4, climbable=True)
    tiles.add("bookshelf4",  "bookshelf", 5, 12, 4, 4, climbable=True)
    tiles.addRandomAlternative("bookshelf", "bookshelf1", 1)
    tiles.addRandomAlternative("bookshelf", "bookshelf2", 1)
    tiles.addRandomAlternative("bookshelf", "bookshelf3", 1)
    tiles.addRandomAlternative("bookshelf", "bookshelf4", 1)


    return tiles






