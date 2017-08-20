from display import Display
from sprite import Sprite
import pygame

class Game:
    def __init__(self):
        self._display = Display()
        self._stop = False
        self._clock = pygame.time.Clock()
        self._player = Sprite()

    def start(self):
        pygame.init()
        self._display.initWindow()
        self.run()

    def run(self):
        while not self._stop:
            self.getEvent()
            self._display.fill()
            self._display.draw(self._player)
            self._display.update()
            self._clock.tick(60)

        self.close()

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._stop = True
            if event.type == pygame.KEYDOWN:
                pass

    def close(self):
        pygame.quit()
        quit()
