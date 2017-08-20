import pygame

class Tile:
    def __init__(self, img):
        self._img = pygame.image.load(img)

    def getImage(self):
        return self._img

class Room:
    def __init__(self, type = "defaultRoom"):
        self._floor = Tile("assets\\tiles\\"+type+"\\floor.png")
        self._wall = Tile("assets\\tiles\\"+type+"\\wall.png")
        self._door = Tile("assets\\tiles\\"+type+"\\door.png")

    def getFloor(self):
        return self._floor

    def getWall(self):
        return self._wall

    def getDoor(self):
        return self._door
