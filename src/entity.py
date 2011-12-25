import pygame, random, math
from pygame.locals import *
from resourcemanager import *

# Possible states that an entity can be in
jumpingState = "jumping"
climbingState = "climbing"
walkingState = "walking"
swimmingState = "swimming"

# Various moving creatures, as well as special map objects
class Entity():
    def __init__(self, x, y, image, physics=False, name = ""):
        self.x = x
        self.y = y
        self.name = ""
        self.tileMap = None
        self.setImage(image)
        
        # Physics variables:
        self.doPhysics = physics
        self.dx = 0
        self.dy = 0
        self.ax = 0
        self.ay = 0
        self.thrustX = 0
        self.thrustY = 0
        self.envDx = 0
        self.envDy = 0
        self.state = jumpingState # Can be one of the states above
        self.jumpSpeed  = 350 # Speed up when jumping
        self.flySpeed   = 120 # Sideways speed in air while falling
        self.walkSpeed  = 200
        self.climbSpeed = 170       
        self.swimSpeed = 100
        self.sinkSpeed = -1000 # Floating by default
        self.fallAcceleration = 15000
        self.airResistance = 0.3
        self.waterResistance = 2
        self.bounce = False
        self.area = pygame.Rect(0, 0, 1, 1)
        
        return

    def setImage(self, image):
        self.image = image 
        if not image == None:                
            self.xOffset = self.image.get_rect().centerx
            self.yOffset = self.image.get_rect().bottom
            self.area = image.get_rect().copy()
        else:
            self.xOffset = 0
            self.yOffset = 0
            self.area = pygame.Rect(0, 0, 1, 1)

        

    def getArea(self):
        self.area.x = self.x - self.xOffset
        self.area.y = self.y - self.yOffset
        self.area.h = self.image.get_rect().width
        self.area.w = self.image.get_rect().height
        return self.area
        
    def update(self, durationSeconds):
        if self.doPhysics and self.tileMap is not None:
            self.physicsUpdate(durationSeconds)
        return
        
    def draw(self, camera):
        if self.image is not None:
            camera.drawImage(self.image, 
                             self.x - self.xOffset, 
                             self.y - self.yOffset)

    # Called when the player tries to activate the entity
    def activate(self, player):
        return

    # Returns true if the entity intersects with the area
    def overlaps(self, area):
        return self.getArea().colliderect(area)         

    # Moves the entity in the specified direction
    def move(self, xDir, yDir, disengage = False):

        # The accelecration done by movement, used for flying or swimming (walking and climbing directly modifies the velocity)
        self.thrustX = 0
        self.thrustY = 0
        
        # Act differently depending on where the character is:
        
        # On ground
        if self.state == walkingState:

            # Move sideways with walking speed in the specified direction
            self.dx = xDir * self.walkSpeed

            # Check up/down movement
            if yDir < 0:
                # Up pressed, try to climb or jump
                if self.atClimbableTile():
                    # Climb up if the tile is climbable
                    self.dy -= self.climbSpeed
                    self.state = climbingState
                else:
                    # Jump if there is nothing to climb
                    self.dy -= self.jumpSpeed
                    self.state = jumpingState
            elif yDir > 0:
                # Down pressed, try to go down by climbing or swimming:
                if self.aboveClimbableTile():
                    # Climb down if the tile below is climbable
                    self.dy += self.climbSpeed
                    self.state = climbingState
                elif self.aboveSwimmableTile():    
                    # Swim down if the tile below is swimmable
                    self.dy += self.swimSpeed
                    self.state = swimmingState
                else:
                    # Otherwise don't move in y direction    
                    self.dy = 0
            else:
                # No movement in y direction        
                self.dy = 0
                
        
        # In air
        elif self.state == jumpingState:
            # Control air movement (e.g. with wings in case of main character)
            self.thrustX = xDir * self.flySpeed
            self.thrustY = yDir * self.flySpeed
        
            # If we are over a climbable object, and player pressed up, start climbing
            if yDir < 0 and self.atClimbableTile():
                self.state = climbingState
                
        # Climbing
        elif self.state == climbingState:
            # Climbing movement 
            self.dx = xDir * self.climbSpeed
            self.dy = yDir * self.climbSpeed
            
            # If we are above a blocking tile, and player pressed down, assume they want to walk
            if yDir > 0 and self.aboveBlockingTile():
                self.state = walkingState
                self.dy = 0

            # If disengage button was pressed, stop climbing and jump
            if disengage:
                self.state = jumpingState
                self.dx = xDir * self.jumpSpeed
                self.dy = yDir * self.jumpSpeed               
                    
        # Swimming
        elif self.state == swimmingState:
            # Swimming movement 
            self.thrustX = xDir * self.swimSpeed
            self.thrustY = yDir * self.swimSpeed
    
        
    def physicsUpdate(self, durationSeconds):
    
        # Sanity check our location
        if self.atBlockingTile():
            # We are inside a wall!
            # We should not really be inside a wall, but if we are, move the entity up and out
            print("Warning: Entity inside wall!  Moving up")
            self.y -= 1
            return # No need to do any other physics while we are in an invalid place
            

        # Add external forces based on state
        if self.state == jumpingState:
            # If we are jumping, update fall speed
            self.ay = self.fallAcceleration * durationSeconds    

            # Apply air resistance
            self.dx -= self.dx * self.airResistance * durationSeconds
            self.dy -= self.dy * self.airResistance * durationSeconds
        
        elif self.state == swimmingState:
            # If we are swimming, add wave forces (sine over time)
            timeSec = pygame.time.get_ticks() * 0.001
            self.ax = math.sin(timeSec*1.52) * 800 * durationSeconds
            self.ay = (math.sin(timeSec*1.62) * 500 + self.sinkSpeed) * durationSeconds 

            # Apply water resistance
            self.dx -= self.dx * self.waterResistance * durationSeconds
            self.dy -= self.dy * self.waterResistance * durationSeconds

        else:
            # No acceleration for climbing or walking states
            self.ax = 0
            self.ay = 0

        # Calculate velocity from acceleration
        self.dx += (self.ax + self.thrustX) * durationSeconds
        self.dy += (self.ay + self.thrustY) * durationSeconds
        
        # Calculate new pos
        newX = self.x + (self.dx) * durationSeconds
        newY = self.y + (self.dy) * durationSeconds
        
        # Check if we would go into a wall
        endX   = int(newX)
        endY   = int(newY)
        if self.blockingTileAt(endX, endY):
            # If we are bouncy, invert deltas
            if self.bounce:
                # Figure out if we bounced from a horizontal or vertical wall (or both?)
                # TODO: Better bounce
                startX = int(self.x)
                startY = int(self.y)
                if startX == endX:
                    # Probably horizontal
                    self.dx = -self.dx
                elif startY == endY:
                    # Probably vertical
                    self.dy = -self.dy
                else:
                    # Maybe both, or moving diagonally
                    self.dx = -self.dx
                    self.dy = -self.dy
            else:
                # We are not bouncy, just stop moving
                # TODO: Stop moving in direction of wall, not otherwise
                self.dx = 0
                self.dy = 0
        else:
            # No blocking tile at next position, ok to move there    
            self.x = newX
            self.y = newY

            if self.state == jumpingState:               
                # If we are falling, check if we landed            
                if self.atSwimmableTile():
                    # We fell into water
                    self.state = swimmingState               
                elif self.aboveBlockingTile():
                    # We landed on ground
                    self.state = walkingState
                    self.dy = 0
                    self.ax = 0
                    self.ay = 0
                elif self.aboveClimbableTile() and self.dy > 0:
                    # We were dropping down and landed on something climbable
                    self.state = walkingState
                    self.dy = 0
                    self.ax = 0
                    self.ay = 0
                                       
            elif self.state == walkingState:
                if not self.aboveWalkableTile():
                    # We are no longer walking over anything! fall down
                    self.state = jumpingState
            elif self.state == climbingState:
                if not self.atClimbableTile():
                    # We are no longer climbing on anything! fall down
                    self.state = jumpingState
            elif self.state == swimmingState:
                if not self.atSwimmableTile():
                    # We are no longer swimming in anything! fall down
                    self.state = jumpingState
                    

    def stop(self):
        self.dx = 0
        self.dy = 0
        self.ax = 0
        self.ay = 0
        
    def aboveWalkableTile(self):
        return self.aboveClimbableTile() or self.aboveBlockingTile()


    def atClimbableTile(self):
        return self.tileMap.climbableAt(int(self.x), int(self.y))

    def atBlockingTile(self):
        return self.tileMap.blockingAt(int(self.x), int(self.y))

    def atSwimmableTile(self):
        return self.tileMap.swimmableAt(int(self.x), int(self.y))

    def aboveClimbableTile(self):
        return self.tileMap.climbableAt(int(self.x), int(self.y) + 1)

    def aboveBlockingTile(self):
        return self.tileMap.blockingAt(int(self.x), int(self.y) + 1)

    def aboveSwimmableTile(self):
        return self.tileMap.swimmableAt(int(self.x), int(self.y) + 1)

    def blockingTileAt(self, x, y):
        return self.tileMap.blockingAt(int(x), int(y))





