import pygame, random, math
from pygame.locals import *
import textutils
from colorutils import *
from room import *
from world import *
from camera import *

# Some constants
gameName = "Vampire and Teddybears"
screenSize = [1024, 256*3]

# Setup screen
pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption(gameName)

# Tell players we are getting things up and running
screen.fill(darkgreyblue)
textutils.drawTextCentered(screen, "Starting Game...")
pygame.display.flip()

# Load the world
world = World()
world.start()

# Keep track of our position
camera = Camera(4, 4)    

# Main loop 
clock = pygame.time.Clock()
running  = True
while running:

    # Run at 40 frames per second
    frameDurationSeconds = clock.tick(40) * 0.001 # Returns milliseconds since last call, convert to seconds

    # Read input  sammuttaa pelin   
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False
    # TODO: Read inputs

    # Fill screen with black, so that earlier graphics dont show up 
    screen.fill(darkgreyblue)

    world.currentRoom.update(frameDurationSeconds)

    world.currentRoom.draw(screen, camera)

    textutils.drawTextCentered(screen, "Insert Game Here! :)")

    # TODO: Draw map
    # TODO: Draw figures
    # TODO: Draw HUD with score, life, etc.

    # Show the screen we just painted, and hide and start painting on the screen that was just visible
    pygame.display.flip()

 
# Tell player that game is closing normally, as it can take a few seconds
screen.fill(darkgreyblue)
textutils.drawTextCentered(screen, "Thanks for playing!")
pygame.display.flip()

# Release loaded resources, shut down pygame
pygame.quit ()


