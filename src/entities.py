import pygame
from entity import *
from resourcemanager import *

tileSize = 64
doorLocked = "doorLocked"
doorClosed = "doorClosed"
doorOpen   = "doorOpen"

class Door(Entity):
    def __init__(self, x, y, destination, state = doorClosed):
        Entity.__init__(self, x, y, None)
        self.destination = destination
        self.setState(doorClosed)

    # Change state and image
    def setState(self, state):
        print("Setting door state to " + state)
        if state == doorLocked:
            self.state = doorLocked
            self.setImage(imageManager.get("door_window_pillar", pygame.Rect(0, 0 * tileSize*4, tileSize * 3, tileSize*4)))
        elif state == doorOpen:    
            self.state = doorOpen
            self.setImage(imageManager.get("door_window_pillar", pygame.Rect(0, 2 * tileSize*4, tileSize * 3, tileSize*4)))
        else:    
            self.state = doorClosed
            self.setImage(imageManager.get("door_window_pillar", pygame.Rect(0, 1 * tileSize*4, tileSize * 3, tileSize*4)))


    # Called when the player activates the door
    def activate(self, player):
        print("Activating door, current state " + self.state)
        if self.state == doorLocked:
            # If door is locked, take key from player inventory and open door
            # TODO
            return
        elif self.state == doorClosed:    
            # If door is closed, open it
            self.setState(doorOpen)
        else:    
            # if door is open, step through
            self.setState(doorClosed)
        


