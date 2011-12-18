
class Camera:
    def __init__(self, x, y, tileSize):
        self.tileX = x
        self.tileY = y
        self.tileSize = tileSize
        
    def pixelX(self):
        return self.tileX * self.tileSize

    def pixelY(self):
        return self.tileY * self.tileSize

