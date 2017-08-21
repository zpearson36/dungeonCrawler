import pygame
import random
from player import Player
from furniture import Furniture

class Tile:
    def __init__(self, img, size = (32,32)):
        self._img = pygame.image.load(img)
        self._size = (32,32)

    def getSize(self):
        return self._size

    def getImage(self):
        return self._img

class Room:
    def __init__(self, roomType = "defaultRoom", size = (800,512), enemies = 2):
        self._size = size
        self._type = roomType
        self._floor = Tile("assets/tiles/"+self._type+"/floor.png")
        self._wall = Tile("assets/tiles/"+self._type+"/wall.png")
        self._door = {}
        self.setDoors()
        self._doors = {'top': (365,0), 'bot': (365,480), 'left':(0, 211), 'right': (768, 211)}
        self._obstacles = []
        self.setObstacles(0)
        self._enemies = []
        self.setEnemies(enemies)

    def setEnemies(self, num):
        for x in range(num):
            thing_x = random.randrange(150, self._size[0]-100)
            thing_y = random.randrange(150, self._size[1]-100)
            self._enemies.append(Player(pos=(thing_x, thing_y)))

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
        self._door['top'] = Tile("assets/tiles/"+self._type+"/door_top.png", (70, 32))
        self._door['bot'] = Tile("assets/tiles/"+self._type+"/door_bot.png", (70, 32))
        self._door['left'] = Tile("assets/tiles/"+self._type+"/door_left.png", (32, 90))
        self._door['right'] = Tile("assets/tiles/"+self._type+"/door_right.png", (32, 90))

    def getFloor(self):
        return self._floor

    def getWall(self):
        return self._wall

    def getDoor(self, orientation):
        return self._door[orientation]

    def getDoorList(self):
        return self._doors
