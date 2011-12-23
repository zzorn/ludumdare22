# Map data for a room
import pygame, random, math
from pygame.locals import *
from resourcemanager import *
from tilemap import *
from maputils import *


def createRoom01(tileSet):
    mapSizex = 100
    mapSizey = 48
    startRoom = TileMap(tileSet.tileSize ,mapSizex ,mapSizey)
    backWall = startRoom.addTileLayer('backWall')
    bg = startRoom.addTileLayer('solid')
    ground = startRoom.addTileLayer('ground')
    startRoom.addEntityLayer('entities')
    startRoom.addEntityLayer('player')
    startRoom.addTileLayer('foreground')

    
    def makePlatform(startX, y, width, leftEndBlock=True, rightEndBlock=True):
        endX = 4 * width + startX
        for x in range(startX, endX, 4):  
            tileSet.putBlock(ground, "floor", x, y)
        if leftEndBlock: tileSet.putBlock(ground, "floorLeft",  (startX - 1), y)
        if rightEndBlock: tileSet.putBlock(ground, "floorRight", (endX      ), y)
  



        
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


    

   #    etukivet eli lattia mutaa ei se paalle tuleva vaa se nelio ... in range(alkuruutu, loppuruutu, hyppays)
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



  

    # mud at bottom ...range(alku, loppu, hyppy)   ...."mud", x, annetaan alkukorkeus)
    for x in range(24, 32, 4):
        tileSet.putBlock(bg, "mudSurface", x, 26)  
        tileSet.putBlock(bg, "mud", x, 26+4)  
    for x in range(40, 48, 4):
        tileSet.putBlock(bg, "mudSurface", x, 26)  
        tileSet.putBlock(bg, "mud", x, 26+4)  
    for x in range(60, 68, 4):
        tileSet.putBlock(bg, "mudSurface", x, 26)
        tileSet.putBlock(bg, "mud", x, 26+4)  
    for x in range(72, 76, 4):
        tileSet.putBlock(bg, "mudSurface", x, 26)
        tileSet.putBlock(bg, "mud", x, 26+4)  


   # lattiat eli ne josta kasvaa esim ruohoa kaytta def    makePlatformia  ...form(alkux, alkuy, monta 4x4 tilea)
    makePlatform(16, 24, 2, False)
    makePlatform(32, 24, 2)
    makePlatform(48, 24, 3)
    makePlatform(68, 24, 1)
    makePlatform(76, 24, 2, rightEndBlock=False)


    




  

  

    # takaseina, ala koske
    for x in range(0, mapSizex):
        for y in range(0,mapSizey):
            tileSet.putBlock(backWall, "wall", x * 4, y * 4)     

    

    return startRoom

