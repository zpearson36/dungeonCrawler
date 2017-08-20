from display import Display
from sprite import Sprite
from player import Player
from room import Room
import pygame

class Game:
    def __init__(self):
        self._display = Display()
        self._stop = False
        self._clock = pygame.time.Clock()
        self._player = Player()
        self._room = Room()

    def start(self):
        pygame.init()
        self.getDisplay().initWindow()
        self.run()

    def run(self):
        while not self._stop:
            self.getEvent()
            self.getDisplay().fill()
            self.getDisplay().renderRoom(self.getRoom())
            self._player.move(self.getDisplay().getDimensions())
            self.getDisplay().draw(self._player.getSprite(), self._player.getPos())
            self.getDisplay().update()
            self._clock.tick(60)

        self.close()

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._stop = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        self._player.setVel((-5, 0))
                elif event.key == pygame.K_RIGHT:
                        self._player.setVel((5, 0))
                elif event.key == pygame.K_UP:
                        self._player.setVel((0, -5))
                elif event.key == pygame.K_DOWN:
                        self._player.setVel((0, 5))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self._player.setVel((0, 0))
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self._player.setVel((0, 0))

    def getDisplay(self):
        return self._display

    def getRoom(self):
        return self._room

    def close(self):
        pygame.quit()
        quit()
