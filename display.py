import pygame

class Display:
    def __init__(self, dimensions = (800, 600), title="Game"):
        self._dimensions = dimensions
        self._title = title
        self._background = (255,255,255)
        self._clock = pygame.time.Clock()

    def initWindow(self):
        pygame.init()
        self._display = pygame.display.set_mode((self._dimensions[0],self._dimensions[1]))
        pygame.display.set_caption(self._title)

    def update(self):
        pygame.display.update()
        self._clock.tick(60)

    def close(self):
        pygame.quit()
        quit()
