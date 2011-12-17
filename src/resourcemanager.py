# Code based on http://www.pygame.org/wiki/LazyImageLoading?parent=CookBook

import pygame
import weakref
 
class ResourceManager(object):
    def __init__(self):
        self.__dict__.update(dict(
            cache = weakref.WeakValueDictionary(),
        ))
       
    def get(self, key):
        try:
            resource = self.cache[key]
        except KeyError:
            return None
        return resource
        
    def store(self, key, resource):
        self.cache[key] = resource 
        
    
class ImageManager:
    def __init__(self, baseDir):
        self.cache = ResourceManager()
        self.baseDir = baseDir

    # Get an image with the specified name        
    def getImage(self, imageName):
        fileName = self.baseDir + imageName + ".png"
        img = self.cache.get(fileName)
        if img == None:
            img = pygame.image.load(fileName)
            self.baseDir + imageName
            self.cache.store(imageName, img)
        return img
 
    # Get a part of an image (specified by a rect)   
    def get(self, imageName, subArea = None):
        if subArea == None:
            return self.getImage(imageName)
        else:    
            key = imageName + str(subArea)
            img = self.cache.get(key)
            if img == None:
                img = self.getImage(imageName)
                imagePart = pygame.Surface(subArea.size)
                imagePart.blit(img, (-subArea.left, -subArea.top))
                img = imagePart
                self.cache.store(key, img)
            return img
         
imageManager = ImageManager("images/")
        
