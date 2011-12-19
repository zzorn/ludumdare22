import pygame, random, math
from pygame.locals import *
from resourcemanager import *

def createEntity(obj):
    x = obj.x + obj.width / 2
    y = obj.y + obj.height
    entity = None
    kind = obj.type
    print ("Creating entity " + kind + " at " + str(x) + ", " + str(y))
    if kind == "Item":
        if obj.Type == "TeddyBear":
            print("Making teddybear")    
            img = imageManager.getTile("creepers", random.randrange(0,5), 2, 128, transparent=True)
            print ("image is ", img)
            entity = Entity(x, y, img)
        else: 
            print("Could not create item of type ", obj.Type)
    else:
        print("Could not create object of type ", kind)    
    return entity    



class Entity():
    def __init__(self, x, y, image, physics=False):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.tileMap = None
        self.image = image
        self.doPhysics = physics
        self.onGround = False
        self.jumpSpeed = 100
        self.fallAcceleration = 50
        self.xOffset = self.image.get_rect().centerx
        self.yOffset = self.image.get_rect().bottom
        return
        
    def update(self, durationSeconds):
        if self.doPhysics and self.tileMap is not None:
            self.physicsUpdate(durationSeconds)
        return
        
    def draw(self, camera):
        if self.image is not None:
            camera.drawImage(self.image, 
                             self.x - self.xOffset, 
                             self.y - self.yOffset)


    def move(self, dx):
        self.dx = dx
        
    def jump(self):
        if self.onGround:
            self.dy = -self.jumpSpeed

    def physicsUpdate(self, durationSeconds):

        # Fall speed
        if not self.onGround:
            self.dy += self.fallAcceleration * durationSeconds

        # Don't move through solid walls
        if self.tileMap.blockingAt(self.x + self.dx * durationSeconds, self.y):
            self.dx = 0
    
        # Calculate new position
        self.x += self.dx * durationSeconds
        self.y += self.dy * durationSeconds

        # Check if we are on the ground        
        if self.tileMap.blockingAt(self.x, self.y + 1):
            self.onGround = True
            self.dy = 0
        else:
            self.onGround = False
    
        



