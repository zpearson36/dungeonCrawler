import pygame

class Sprite:
    def __init__(self, img ="assets/sprites/player2.png", size=(53,68)):
        self._image = pygame.image.load(img)
        self._size = size

    def getImage(self):
        return self._image

    def getWidth(self):
        return self._size[0]

    def getHeight(self):
        return self._size[1]

    def getSize(self):
        return self._size
