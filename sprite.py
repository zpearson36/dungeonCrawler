import pygame

class Sprite:
    def __init__(self, img ="player_down_1.png", size=(53,68), imgLoc = "assets/sprites/"):
        self._imgLoc = imgLoc
        self._imgName = img
        self.loadImg()
        self._size = size

    def getImage(self):
        return self._image

    def getWidth(self):
        return self._size[0]

    def getHeight(self):
        return self._size[1]

    def setImgName(self, img):
        self._imgName = img

    def loadImg(self):
        self._image = pygame.image.load(self._imgLoc+self._imgName)

    def getSize(self):
        return self._size
