from sprite import Sprite

class Furniture:
    def __init__(self, roomType = "defaultRoon", img = "altar.png", size = (50,50), pos = (32,32)):
        self._sprite = Sprite("assets\\tiles\\"+roomType+"\\"+img, size)
        self._pos = pos

    def getPos(self):
        return self._pos

    def getSprite(self):
        return self._sprite

    def getSize(self):
        return self.getSprite().getSize()
