import pygame, random, math
from pygame.locals import *
import textutils
from colorutils import *
from tilemap import *
from world import *
from camera import *
from player import *

# Some constants
gameName = "Vampire and Teddybears"
screenSize = [1024, 256*3]
tileSize = 64
cameraSpeed = 1000

# Input keys
keyUp        = [K_UP, K_w]
keyDown      = [K_DOWN, K_s]
keyLeft      = [K_LEFT, K_a]
keyRight     = [K_RIGHT, K_d]
keyActivate  = [K_SPACE, K_RETURN]
keyBack      = [K_ESCAPE]
toggleCamera = K_v

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
world = World(tileSize)
world.start()

# Player
player = Player(64*17, 64*24, imageManager.getTile("victor", 0, 1, 256, transparent=True))
player.yOffset -= 20 # Stand on ground
world.currentRoom.getLayer('player').add(player)


# TODO: Enter room
# TODO: Find entrance position (specified by the door that lead there, or by start pos)
# TODO: Put player on entrance position

# Keep track of our position
camera = Camera(screen, target=player)    

# True if any of the specified control keys are pressed
def pressed(pressedKeys, controlKeys):
    for key in controlKeys:
        if pressedKeys[key]: return True
    return False


def isFreeCamMode():
    return camera.target == None


# Main loop 
clock = pygame.time.Clock()
running  = True
while running:

    # Run at 40 frames per second
    frameDurationSeconds = clock.tick(40) * 0.001 # Returns milliseconds since last call, convert to seconds

    # Update camera
    camera.update(frameDurationSeconds)

    # Check if esc was pressed or window closed
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == toggleCamera:
            if isFreeCamMode():
                camera.target = player
            else:
                camera.target = None

    # Read pressed keys
    pressedKeys = pygame.key.get_pressed()
    xDir = 0
    yDir = 0
    if pressed(pressedKeys, keyLeft):
            xDir -= 1
    if pressed(pressedKeys, keyRight):
            xDir += 1
    if pressed(pressedKeys, keyUp):
            yDir -= 1
    if pressed(pressedKeys, keyDown):
            yDir += 1

    if isFreeCamMode():
        camera.x += xDir * cameraSpeed * frameDurationSeconds
        camera.y += yDir * cameraSpeed * frameDurationSeconds
    else:    
        player.move(xDir, yDir)
    
    # TODO: Handle activate key

    # Fill screen with black, so that earlier graphics dont show up 
    screen.fill(darkgreyblue)

    world.currentRoom.update(frameDurationSeconds)

    world.currentRoom.draw(camera)

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


