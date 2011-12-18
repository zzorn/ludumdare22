import pygame, random, math
from pygame.locals import *
import textutils
from colorutils import *
from room import *
from world import *
from camera import *
from player import *

# Some constants
gameName = "Vampire and Teddybears"
screenSize = [1024, 256*3]
tileSize = 64

# Input keys
keyUp       = [K_UP, K_w]
keyDown     = [K_DOWN, K_s]
keyLeft     = [K_LEFT, K_a]
keyRight    = [K_RIGHT, K_d]
keyActivate = [K_SPACE, K_RETURN]
keyBack     = [K_ESCAPE]

# Setup screen
pygame.init()
screen = pygame.display.set_mode(screenSize)
#screen = pygame.display.set_mode(screenSize, FULLSCREEN)
pygame.display.set_caption(gameName)

# Hide mouse
pygame.mouse.set_visible(False)

# Tell players we are getting things up and running
screen.fill(darkgreyblue)
textutils.drawTextCentered(screen, "Starting Game...")
pygame.display.flip()

# Load the world
world = World()
world.start()

# Keep track of our position
camera = Camera(8, 4, tileSize)    

# Player
player = Player(700, 700, imageManager.getTile("victor", 0, 1, 256, transparent=True))
world.currentRoom.add(player)

# TODO: Enter room
# TODO: Find entrance position (specified by the door that lead there, or by start pos)
# TODO: Put player on entrance position

# True if any of the specified control keys are pressed
def pressed(pressedKeys, controlKeys):
    for key in controlKeys:
        if pressedKeys[key]: return True
    return False


# Main loop 
clock = pygame.time.Clock()
running  = True
while running:

    # Run at 40 frames per second
    frameDurationSeconds = clock.tick(40) * 0.001 # Returns milliseconds since last call, convert to seconds

    # Check if esc was pressed or window closed
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False

    # Read pressed keys
    movementSpeed = 64
    pressedKeys = pygame.key.get_pressed()
    if pressed(pressedKeys, keyLeft):
            camera.tileX -= 1
            player.move(-movementSpeed)
    if pressed(pressedKeys, keyRight):
            camera.tileX += 1
            player.move(movementSpeed)
    if pressed(pressedKeys, keyUp):
            camera.tileY -= 1
            player.jump()
    if pressed(pressedKeys, keyDown):
            camera.tileY += 1

    # Fill screen with black, so that earlier graphics dont show up 
    screen.fill(darkgreyblue)

    world.currentRoom.update(frameDurationSeconds)

    world.currentRoom.draw(screen, camera)

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


