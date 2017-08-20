import pygame

class Display:
    def __init__(self, dimensions = (800, 600), title="Game"):
        self._dimensions = dimensions
        self._title = title
        self._background = (255,255,255)

    def getWidth(self):
        return self._dimensions[0]

    def getHeight(self):
        return self._dimensions[1]

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

    def fill(self):
        self._display.fill(self.getBackground())

    def update(self):
        pygame.display.update()
