import pygame

class Sprite:
    def __init__(self, img ="assets\\sprites\\player.png", size=(140,180)):
        self._image = pygame.image.load(img)
        self._size = size

    def getImage(self):
        return self._image

    def getSize(self):
        return self._size
