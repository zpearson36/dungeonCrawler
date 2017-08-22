import pygame
import random
import player
from furniture import Furniture

class Tile:
    def __init__(self, img, size = (32,32), pos = (0,0)):
        self._img = pygame.image.load(img)
        self._size = (32,32)
        self._pos = pos

    def getPos(self):
        return self._pos

    def getSize(self):
        return self._size

    def getImage(self):
        return self._img

class Room:
    def __init__(self, roomType = "defaultRoom", size = (800,512), enemies = 0):
        self._size = size
        self._type = roomType
        self._floor = Tile("assets/tiles/"+self._type+"/floor.png")
        self._wall = Tile("assets/tiles/"+self._type+"/wall.png")
        self._door = {}
        self.setDoors()
        self._doors = {'top': (365,385), 'bot': (365,35), 'left':(690, 208), 'right': (35, 211)}
        self._obstacles = []
        self.setObstacles(random.randrange(0, 5))
        self._enemies = []
        self.setEnemies(random.randrange(0, 4))

    def setEnemies(self, num):
        for x in range(num):
            thing_x = random.randrange(150, self._size[0]-100)
            thing_y = random.randrange(150, self._size[1]-100)
            self._enemies.append(player.Player(pos=(thing_x, thing_y)))

    def getEnemies(self):
        return self._enemies

    def getSize(self):
        return self._size

    def setObstacles(self, num):
        for x in range(num):
            thing_x = random.randrange(150, self._size[0]-100)
            thing_y = random.randrange(150, self._size[1]-100)
            self._obstacles.append(Furniture(roomType = self._type, pos=(thing_x, thing_y)))

    def getObstacles(self):
        return self._obstacles


    def setDoors(self):
        self._door['top'] = Tile("assets/tiles/"+self._type+"/door_top.png", (70, 32), (365,0))
        self._door['bot'] = Tile("assets/tiles/"+self._type+"/door_bot.png", (70, 32), (365,480))
        self._door['left'] = Tile("assets/tiles/"+self._type+"/door_left.png", (32, 90), (0, 211))
        self._door['right'] = Tile("assets/tiles/"+self._type+"/door_right.png", (32, 90), (768, 211))

    def getFloor(self):
        return self._floor

    def getWall(self):
        return self._wall

    def getDoor(self, orientation):
        return self._door[orientation]

    def getDoorList(self):
        return self._doors
