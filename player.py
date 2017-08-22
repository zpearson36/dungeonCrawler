from sprite import Sprite
import room
import random
import threading
from utils import UID
import utils
import time

class Player:
    def __init__(self, pos = (300, 300)):
        self._UID = UID.uid()
        self._sprite = Sprite()
        self._pos = pos
        self._vel = (0, 0)
        self._lock = threading.Lock()
        self._alive = True
        self._direction = "down"
        self._walkCycle = 1

    def attack(self, display):
        size = {"down":(88,52), "up":(88,52), "left":(52,88), "right":(52,88)}
        direction = {"down":(-15, self.getSize()[1]), "up":(-15,-1*size[self.getDirection()][1]), "left":(-1*size[self.getDirection()][0],-15), "right":(self.getSize()[0],-15)}
        slash = Sprite(img = "slash_"+self.getDirection()+".png", imgLoc = "assets/effects/", size = size[self.getDirection()])
        start = time.time()
        while time.time() - start < .1:
            display.draw(slash, (self.getPos()[0]+direction[self.getDirection()][0],self.getPos()[1]+direction[self.getDirection()][1]))

    def getCycle(self):
        self._walkCycle += 1
        if self._walkCycle >= 30:
            self._walkCycle = 0
        return self._walkCycle//10

    def setDirection(self, direction):
        self._direction = direction

    def getDirection(self):
        return self._direction

    def getUID(self):
        return self._UID

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

    def move(self, dungeon):

        x = self.getPos()[0]+self.getVel()[0]
        y = self.getPos()[1]+self.getVel()[1]

        img = {(0,1): "down",(0,-1): "up",(1,0): "right",(-1,0): "left"}
        if self.getVel() != (0,0):
            self.setDirection(img[utils.reduceTuple(self.getVel())])

        if self.getVel() == (0,0):
            cycle = "1"
        else:
            cycle = str(self.getCycle())

        self.getSprite().setImgName("player_"+self.getDirection()+"_"+cycle+".png")
        self.getSprite().loadImg()

        for door, portal in dungeon.getDoorList().items():
            #upperleft
            if y <= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and y >= dungeon.getDoor(door).getPos()[1] and x <= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x >= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()
            #bottomleft
            elif y+self.getSprite().getHeight() <= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and y+self.getSprite().getHeight() >= dungeon.getDoor(door).getPos()[1] and x <= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x >= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()
            #upperright
            elif y <= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and y >= dungeon.getDoor(door).getPos()[1] and x+self.getSprite().getWidth() <= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x+self.getSprite().getWidth() >= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()
            #bottomeright
            elif y+self.getSprite().getHeight() <= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and y+self.getSprite().getHeight() >= dungeon.getDoor(door).getPos()[1] and x+self.getSprite().getWidth() <= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x+self.getSprite().getWidth() >= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()
            #topedge
            elif y <= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and y >= dungeon.getDoor(door).getPos()[1] and x+self.getSprite().getWidth() >= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x <= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()
            #bottomedge
            elif y+self.getSprite().getHeight() <= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and y+self.getSprite().getHeight() >= dungeon.getDoor(door).getPos()[1] and x+self.getSprite().getWidth() >= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x <= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()
            #leftedge
            elif y+self.getSprite().getHeight() >= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and y <= dungeon.getDoor(door).getPos()[1] and x <= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x >= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()
            #rightedge
            elif y <= dungeon.getDoor(door).getPos()[1] and y+self.getSprite().getHeight() >= dungeon.getDoor(door).getPos()[1]+dungeon.getDoor(door).getSize()[1] and x+self.getSprite().getWidth() <= dungeon.getDoor(door).getPos()[0]+dungeon.getDoor(door).getSize()[0] and x+self.getSprite().getWidth() >= dungeon.getDoor(door).getPos()[0]:
                self.setPos(portal)
                return room.Room()

        #Room Boundaries
        if x > dungeon.getSize()[0] - self.getSprite().getWidth() - 32:
            x = dungeon.getSize()[0] - self.getSprite().getWidth() - 32
        elif x < 32:
            x = 32

        if y > dungeon.getSize()[1] - self.getSprite().getHeight() - 32:
            y = dungeon.getSize()[1] - self.getSprite().getHeight() - 32
        elif y < 32:
            y = 32

        #object collision
        for obj in dungeon.getObstacles()+dungeon.getEnemies():
            if obj.getUID() == self.getUID():
                continue
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
        return None
