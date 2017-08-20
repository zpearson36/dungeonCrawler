import pygame

class Display:
    def __init__(self, dimensions = (800, 512), title="Game"):
        self._dimensions = dimensions
        self._title = title
        self._background = (255,255,255)

    def getWidth(self):
        return self._dimensions[0]

    def getHeight(self):
        return self._dimensions[1]

    def getDimensions(self):
        return self._dimensions

    def setDimensions(self, width = None, height = None):
        if width == None:
            width = self.getWidth()
        if height == None:
            height = self.getHeight()
        self._dimensions = (width, height)

    def getBackground(self):
        return self._background

    def setBackground(self, newBackground = (255,255,255)):
        self._background = newBackground

    def initWindow(self):
        self._display = pygame.display.set_mode((self.getWidth(),self.getHeight()))
        pygame.display.set_caption(self._title)

    def draw(self, sprite, pos = (300, 300)):
        self._display.blit(sprite.getImage(), pos)

    def renderRoom(self, room):
        #draw floor
        for x in range(self._dimensions[0]//32):
            for y in range(self._dimensions[1]//32):
                self.draw(room.getFloor(), (x*32, y*32))

        #draw wall
        for x in range(self._dimensions[0]//32):
            self.draw(room.getWall(), (x*32, 0))
            self.draw(room.getWall(), (x*32, self._dimensions[1]-32))
        for y in range(self._dimensions[0]//32):
            self.draw(room.getWall(), (0, y*32))
            self.draw(room.getWall(), (self._dimensions[0]-32, y*32))

        #draw doors
        for door, pos in room.getDoorList().items():
            self.draw(room.getDoor(door), pos)

        #draw Furniture
        for obj in room.getObstacles():
            self.draw(obj.getSprite(), obj.getPos())

    def fill(self):
        self._display.fill(self.getBackground())

    def update(self):
        pygame.display.update()
