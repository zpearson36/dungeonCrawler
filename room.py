import pygame

class Tile:
    def __init__(self, img):
        self._img = pygame.image.load(img)

    def getImage(self):
        return self._img

class Room:
    def __init__(self, roomType = "defaultRoom"):
        self._type = roomType
        self._floor = Tile("assets\\tiles\\"+self._type+"\\floor.png")
        self._wall = Tile("assets\\tiles\\"+self._type+"\\wall.png")
        self._door = {}
        self.setDoors()
        self._doors = {'top': (365,0), 'bot': (365,480), 'left':(0, 211), 'right': (768, 211)}

    def setDoors(self):
        self._door['top'] = Tile("assets\\tiles\\"+self._type+"\\door_top.png")
        self._door['bot'] = Tile("assets\\tiles\\"+self._type+"\\door_bot.png")
        self._door['left'] = Tile("assets\\tiles\\"+self._type+"\\door_left.png")
        self._door['right'] = Tile("assets\\tiles\\"+self._type+"\\door_right.png")

    def getFloor(self):
        return self._floor

    def getWall(self):
        return self._wall

    def getDoor(self, orientation):
        return self._door[orientation]

    def getDoorList(self):
        return self._doors
