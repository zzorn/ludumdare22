# Map data for a room
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from tilemap import *
from maputils import *
from roomparts import *
from entities import *


def createRoom01(tileSet):
    tileSize = 64
    mapSizex = 100
    mapSizey = 48
    startRoom = TileMap(tileSet.tileSize ,mapSizex ,mapSizey)
    
    backWall   = startRoom.addTileLayer('backWall')
    bg         = startRoom.addTileLayer('solid')
    ground     = startRoom.addTileLayer('ground')
    furniture  = startRoom.addTileLayer('furniture')
    entities   = startRoom.addEntityLayer('entities')
    player     = startRoom.addEntityLayer('player')
    foreground = startRoom.addTileLayer('foreground')
    
    # Add doors
    entities.add(Door("door1", tileSize * 20, tileSize * 24, "chairRoom", "door2", doorClosed))
    entities.add(Door("door2", tileSize * 40, tileSize * 24, "startRoom", "door1", doorClosed))
   
        
    #reunat ala koske
    for x in range(0,mapSizex, 4 ):
        for y in range(0,9,4):
            tileSet.putBlock(bg, "stone", x , y )
    for x in range(0,13,4 ):
        for y in range(0,mapSizey, 4):
            tileSet.putBlock(bg, "stone", x , y )
    for x in range(mapSizex-16,mapSizex, 4 ):
        for y in range(0,mapSizey, 4):
            tileSet.putBlock(bg, "stone", x , y )
    for x in range(0,mapSizex, 4 ):
        for y in range(mapSizey-12,mapSizey, 4):
            tileSet.putBlock(bg, "stone", x , y )


    

    # etukivet eli lattia mutta ei se paalle tuleva vaa se nelio ... in range(alkuruutu, loppuruutu, hyppays)
    for x in range(16, 24, 4):
        for y in range( 24, 40, 4): 
            tileSet.putBlock(bg, "stone", x , y)
    for x in range(32, 39, 4):
        for y in range( 24, 40, 4): 
            tileSet.putBlock(bg, "stone", x , y)
    for x in range(48, 60, 4):
        for y in range( 24, 40, 4): 
            tileSet.putBlock(bg, "stone", x , y)
    for x in range(68, 72, 4):
        for y in range( 24, 40, 4): 
            tileSet.putBlock(bg, "stone", x , y)
    for x in range(76, 84, 4):
        for y in range( 24, 40, 4): 
            tileSet.putBlock(bg, "stone", x , y)


    # mud arvot (tileset, bg, alkux, alkuy, leveys aina 4 kertaa, korkeus aina 4 kertaa)
    mud(tileSet, bg, 24, 26, 2, 3)
    mud(tileSet, bg, 40, 26, 2, 3)
    mud(tileSet, bg, 60, 26, 2, 3)
    mud(tileSet, bg, 72, 26, 1, 3)
    

    # kirjahylly parametrit, furniture, alkux, alkuy, isojen kirjahyllypalojen maara leveys, sama korkeus
    kirjahylly(tileSet, furniture, 33, 20, 1, 1)


    # lattiat eli ne josta kasvaa esim ruohoa kaytta def    makePlatformia  ...form(alkux, alkuy, monta 4x4 tilea)
    makePlatform(tileSet, ground, 16, 24, 2, False)
    makePlatform(tileSet, ground, 32, 24, 2)
    makePlatform(tileSet, ground, 48, 24, 3)
    makePlatform(tileSet, ground, 68, 24, 1)
    makePlatform(tileSet, ground, 76, 24, 2, rightEndBlock=False)


    




  

  

    # takaseina, ala koske
    for x in range(0, mapSizex):
        for y in range(0,mapSizey):
            tileSet.putBlock(backWall, "wall", x * 4, y * 4)     

    

    return startRoom

