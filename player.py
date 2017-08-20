from sprite import Sprite

class Player:
    def __init__(self, sprite = Sprite(), pos = (300, 300)):
        self._sprite = sprite
        self._pos = pos
        self._vel = (0, 0)

    def getSprite(self):
        return self._sprite

    def getPos(self):
        return self._pos

    def setPos(self, pos = None):
        if pos == None:
            pos = self.getPos()
        self._pos = pos


    def setVel(self, vect = (0,0)):
        self._vel = vect

    def getVel(self):
        return self._vel

    def move(self, displaySize):
        newX = self.getPos()[0]+self.getVel()[0]
        newY = self.getPos()[1]+self.getVel()[1]

        if newX > displaySize[0] - self.getSprite().getWidth() - 32:
            newX = displaySize[0] - self.getSprite().getWidth() - 32
        elif newX < 32:
            newX = 32

        if newY > displaySize[1] - self.getSprite().getHeight() - 32:
            newY = displaySize[1] - self.getSprite().getHeight() - 32
        elif newY < 32:
            newY = 32

        self.setPos((newX, newY))
