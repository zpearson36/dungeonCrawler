from sprite import Sprite

class Player:
    def __init__(self, sprite = Sprite(), pos = (300, 300)):
        self._sprite = sprite
        self._pos = pos

    def getSprite(self):
        return self._sprite

    def getPos(self):
        return self._pos

    def setPos(self, pos = None):
        if pos == None:
            pos = self.getPos()
        self._pos = pos
