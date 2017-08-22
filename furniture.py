from sprite import Sprite
from utils import UID

class Furniture:
    def __init__(self, roomType = "defaultRoon", img = "altar.png", size = (50,50), pos = (32,32)):
        self._UID = UID.uid()
        self._sprite = Sprite(imgLoc ="assets/tiles/"+roomType+"/", img = img, size = size)
        self._pos = pos

    def getUID(self):
        return self._UID

    def getPos(self):
        return self._pos

    def getSprite(self):
        return self._sprite

    def getSize(self):
        return self.getSprite().getSize()
