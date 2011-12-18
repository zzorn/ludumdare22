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



class EntityGroup():
    def __init__(self):
        self.entities = []
        
    def add(self, entity):
        self.entities.append(entity) 

    def remove(self, entity):
        self.entities.remove(entity) 

    def update(self, durationSeconds):
        for entity in self.entities:
            entity.update(durationSeconds)

    def draw(self, surface, camera):
        for entity in self.entities:
            entity.draw(surface, camera)


class Entity():
    def __init__(self, x, y, image, physics=False):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.room = None
        self.image = image
        self.doPhysics = physics
        self.onGround = False
        self.jumpSpeed = 10
        self.fallAcceleration = 50
        return
        
    def update(self, durationSeconds):
        if self.doPhysics and not self.room == None:
            self.physicsUpdate(durationSeconds)
        return
        
    def draw(self, surface, camera):
        if not self.image == None:
            xOffset = self.image.get_rect().centerx
            yOffset = self.image.get_rect().bottom
            surface.blit(self.image, (self.x - camera.pixelX() - xOffset, 
                                      self.y - camera.pixelY() - yOffset))


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
        if self.room.solidAt(self.x + self.dx * durationSeconds, self.y):
            self.dx = 0
    
        # Calculate new position
        self.x += self.dx * durationSeconds
        self.y += self.dy * durationSeconds

        # Check if we are on the ground        
        if self.room.solidAt(self.x, self.y + 1):
            self.onGround = True
            self.dy = 0
        else:
            self.onGround = False
    
        



