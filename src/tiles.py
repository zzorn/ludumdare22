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
    tiles.add("slime", "walls_solid", 0, 8, 4, 4, swimmable=True)
    tiles.add("slimeSurface1", "walls_transparent", 0, 2, 4, 4, swimmable=True)
    tiles.add("slimeSurface2", "walls_transparent", 4, 2, 4, 4, swimmable=True)
    tiles.addRandomAlternative("slimeSurface", "slimeSurface1", 1)
    tiles.addRandomAlternative("slimeSurface", "slimeSurface2", 1)

    # Floor
    tiles.add("floorLeft",  "walls_transparent", 0,  0, 1, 1, blocking=True)
    tiles.add("floorRight", "walls_transparent", 23, 0, 1, 1, blocking=True)
    tiles.add("floorShort", "walls_transparent", 1,  0, 2, 1, blocking=True)
    tiles.add("floor1",     "walls_transparent", 3,  0, 4, 1, blocking=True)
    tiles.add("floor2",     "walls_transparent", 7,  0, 4, 1, blocking=True)
    tiles.add("floor3",     "walls_transparent", 11, 0, 4, 1, blocking=True)
    tiles.add("floor4",     "walls_transparent", 15, 0, 4, 1, blocking=True)
    tiles.addRandomAlternative("floor", "floor1", 3)
    tiles.addRandomAlternative("floor", "floor2", 2)
    tiles.addRandomAlternative("floor", "floor3", 2)
    tiles.addRandomAlternative("floor", "floor4", 1)

    # Bookshelfts
    tiles.add("bookshelfEdgeLeft1",  "bookshelf", 4, 0, 1, 4, climbable=True)
    tiles.add("bookshelfEdgeLeft2",  "bookshelf", 4, 4, 1, 4, climbable=True)
    tiles.addRandomAlternative("bookshelfEdgeLeft", "bookshelfEdgeLeft1", 1)
    tiles.addRandomAlternative("bookshelfEdgeLeft", "bookshelfEdgeLeft2", 1)

    tiles.add("bookshelfEdgeRight1",  "bookshelf", 8, 0, 1, 4, climbable=True)
    tiles.add("bookshelfEdgeRight2",  "bookshelf", 8, 4, 1, 4, climbable=True)
    tiles.addRandomAlternative("bookshelfEdgeRight", "bookshelfEdgeRight1", 1)
    tiles.addRandomAlternative("bookshelfEdgeRight", "bookshelfEdgeRight2", 1)

    tiles.add("bookshelf1",  "bookshelf", 9, 0, 4, 4, climbable=True)
    tiles.add("bookshelf2",  "bookshelf", 9, 4, 4, 4, climbable=True)
    tiles.add("bookshelf3",  "bookshelf", 9, 8, 4, 4, climbable=True)
    tiles.add("bookshelf4",  "bookshelf", 9, 12, 4, 4, climbable=True)
    tiles.addRandomAlternative("bookshelf", "bookshelf1", 1)
    tiles.addRandomAlternative("bookshelf", "bookshelf2", 1)
    tiles.addRandomAlternative("bookshelf", "bookshelf3", 1)
    tiles.addRandomAlternative("bookshelf", "bookshelf4", 1)


    return tiles





