
from mathutils import *
from entity import *


class Camera:
    def __init__(self, surface, target = None):
        self.x = 0
        self.y = 0
        if target is not None:
            self.x = target.x
            self.y = target.y
        self.dx = 0
        self.dy = 0
        self.followSpeed = 0.12
        self.foreShadowing = 1.5
        self.surface = surface
        self.target = target
        self.visibleArea = surface.get_rect().copy()
        self._updateVisibleArea()

    # Set an entity that the camera centers on (typically the player)
    # Set to None to stop the camera from moving
    def follow(self, entity):
        self.target = entity
        
    # Return true if an area in the world with a top at x,y and specified width and height is visible on the camera now
    def isVisible(self, x, y, w, h):
        return (self.visibleArea.left - w <= x < self.visibleArea.right and 
                self.visibleArea.top - h <= y < self.visibleArea.bottom)
                  
        
    
    # Draw an image at a specific world coordinate to the camera surface
    def drawImage(self, image, worldX, worldY):
        # First check if the image would be visible at all before drawing
        if self.isVisible(worldX, 
                          worldY, 
                          image.get_rect().width, 
                          image.get_rect().height):
            self.surface.blit(image, 
                              (worldX - self.visibleArea.left, 
                               worldY - self.visibleArea.top))

    # Update camera position
    def update(self, durationSeconds):
        if self.target is not None:
            # Calculate the amount we would need to move the camera to get it to the target entity
            tdx = self.target.x - self.x + self.target.dx * self.foreShadowing
            tdy = self.target.y - self.y + self.target.dy * self.foreShadowing

            # Take into account target movement speed, so move camera in front of where the target is moving
            tdx = self.target.x - self.x + self.target.dx * self.foreShadowing
            tdy = self.target.y - self.y + self.target.dy * self.foreShadowing
            
            # Mix the ideal target movement with the current camera movement, so that the camera moves smoothly
            self.dx = interpolate(self.dx, tdx, self.followSpeed)
            self.dy = interpolate(self.dy, tdy, self.followSpeed)
            
            # Update camera position
            self.x += self.dx * durationSeconds
            self.y += self.dy * durationSeconds
            
        self._updateVisibleArea()
            
    # Update the area that the camera shows of the world (in pixel coordinates)
    def _updateVisibleArea(self):
        self.visibleArea.centerx = self.x
        self.visibleArea.centery = self.y
        
        

