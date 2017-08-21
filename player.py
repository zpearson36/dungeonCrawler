from sprite import Sprite
import random
import threading

class Player:
    def __init__(self, sprite = Sprite(), pos = (300, 300)):
        self._sprite = sprite
        self._pos = pos
        self._vel = (0, 0)
        self._lock = threading.Lock()
        self._alive = True

    def isAlive(self):
        return self._alive

    def kill(self):
        self._alive = False

    def getLock(self):
        return self._lock

    def getSprite(self):
        return self._sprite

    def getPos(self):
        return self._pos

    def getSize(self):
        return self.getSprite().getSize()

    def setPos(self, pos = None):
        if pos == None:
            pos = self.getPos()
        self._pos = pos


    def setVel(self, vect = (0,0)):
        self._vel = vect

    def getVel(self):
        return self._vel

    def move(self, room):
        x = self.getPos()[0]+self.getVel()[0]
        y = self.getPos()[1]+self.getVel()[1]

        #Room Boundaries
        if x > room.getSize()[0] - self.getSprite().getWidth() - 32:
            x = room.getSize()[0] - self.getSprite().getWidth() - 32
        elif x < 32:
            x = 32

        if y > room.getSize()[1] - self.getSprite().getHeight() - 32:
            y = room.getSize()[1] - self.getSprite().getHeight() - 32
        elif y < 32:
            y = 32

        #object collision
        for obj in room.getObstacles()+room.getEnemies():
            #upperleft
            if y <= obj.getPos()[1]+obj.getSize()[1] and y >= obj.getPos()[1] and x <= obj.getPos()[0]+obj.getSize()[0] and x >= obj.getPos()[0]:
                if self.getVel()[0] != 0:
                    x = obj.getPos()[0]+obj.getSize()[0] + 1
                else:
                    y = obj.getPos()[1]+obj.getSize()[1] + 1
            #bottomleft
            elif y+self.getSprite().getHeight() <= obj.getPos()[1]+obj.getSize()[1] and y+self.getSprite().getHeight() >= obj.getPos()[1] and x <= obj.getPos()[0]+obj.getSize()[0] and x >= obj.getPos()[0]:
                if self.getVel()[0] != 0:
                    x = obj.getPos()[0]+obj.getSize()[0] + 1
                else:
                    y = obj.getPos()[1] - self.getSprite().getHeight() + 1
            #upperright
            elif y <= obj.getPos()[1]+obj.getSize()[1] and y >= obj.getPos()[1] and x+self.getSprite().getWidth() <= obj.getPos()[0]+obj.getSize()[0] and x+self.getSprite().getWidth() >= obj.getPos()[0]:
                if self.getVel()[0] != 0:
                    x = obj.getPos()[0] - self.getSprite().getWidth() + 1
                else:
                    y = obj.getPos()[1] + obj.getSize()[1] + 1
            #bottomeright
            elif y+self.getSprite().getHeight() <= obj.getPos()[1]+obj.getSize()[1] and y+self.getSprite().getHeight() >= obj.getPos()[1] and x+self.getSprite().getWidth() <= obj.getPos()[0]+obj.getSize()[0] and x+self.getSprite().getWidth() >= obj.getPos()[0]:
                if self.getVel()[0] != 0:
                    x = obj.getPos()[0] - self.getSprite().getWidth() + 1
                else:
                    y = obj.getPos()[1] - self.getSprite().getHeight() + 1
            #topedge
            elif y <= obj.getPos()[1]+obj.getSize()[1] and y >= obj.getPos()[1] and x+self.getSprite().getWidth() >= obj.getPos()[0]+obj.getSize()[0] and x <= obj.getPos()[0]:
                y = obj.getPos()[1] + obj.getSize()[1] + 1
            #bottomedge
            elif y+self.getSprite().getHeight() <= obj.getPos()[1]+obj.getSize()[1] and y+self.getSprite().getHeight() >= obj.getPos()[1] and x+self.getSprite().getWidth() >= obj.getPos()[0]+obj.getSize()[0] and x <= obj.getPos()[0]:
                y = obj.getPos()[1] - self.getSprite().getHeight() + 1
            #leftedge
            elif y+self.getSprite().getHeight() >= obj.getPos()[1]+obj.getSize()[1] and y <= obj.getPos()[1] and x <= obj.getPos()[0]+obj.getSize()[0] and x >= obj.getPos()[0]:
                x = obj.getPos()[0] + obj.getSize()[0] + 1
            #rightedge
            elif y <= obj.getPos()[1] and y+self.getSprite().getHeight() >= obj.getPos()[1]+obj.getSize()[1] and x+self.getSprite().getWidth() <= obj.getPos()[0]+obj.getSize()[0] and x+self.getSprite().getWidth() >= obj.getPos()[0]:
                x = obj.getPos()[0] - self.getSprite().getWidth() + 1

        self.setPos((x, y))
