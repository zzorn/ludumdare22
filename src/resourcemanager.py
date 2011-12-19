# Code based on http://www.pygame.org/wiki/LazyImageLoading?parent=CookBook

import pygame
import weakref
 
class ResourceManager(object):
    def __init__(self):
#        self.cache = {}
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
    def getImage(self, imageName, transparent = False):
        fileName = self.baseDir + imageName + ".png"
        img = self.cache.get(fileName)
        print ("Getting image "+imageName)
        if img == None:
            print ("   loading it")
            img = pygame.image.load(fileName)
            
            if (transparent):
                img = img.convert_alpha()
            else:
                img = img.convert()
                
            self.cache.store(fileName, img)
        else:
            print ("   already loaded")

        return img
 
    # Get a part of an image (specified by a rect)   
    def get(self, imageName, subArea = None, transparent = False):
        if subArea == None:
            return self.getImage(imageName)
        else:    
            print ("Getting area "+str(subArea)+" of image "+imageName)
            key = imageName + str(subArea)
            img = self.cache.get(key)
            if img == None:
                print ("  generating it")
                img = self.getImage(imageName, transparent)
                if transparent:                
                    imagePart = img.subsurface(subArea)
                    #imagePart = pygame.Surface(subArea.size, flags=pygame.SRCALPHA)
                else:
                    imagePart = img.subsurface(subArea)
                    #imagePart = pygame.Surface(subArea.size)
                #imagePart.blit(img, (-subArea.left, -subArea.top))
                img = imagePart
                self.cache.store(key, img)
                print ("  generated")
            else:
                print ("  already generated")

            return img
         
    def getTile(self, imageName, x, y, tileSize, transparent = False):
        return self.get(imageName, pygame.Rect(x * tileSize, y * tileSize, tileSize, tileSize), transparent)

         
imageManager = ImageManager("images/")
        
