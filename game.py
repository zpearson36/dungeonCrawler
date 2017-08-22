from display import Display
from sprite import Sprite
from player import Player
from room import Room
import pygame
import threading
import time
import random
class Game:
    def __init__(self):
        self._display = Display()
        self._stop = False
        self._clock = pygame.time.Clock()
        self._player = Player()
        self._room = Room(size = self._display.getDimensions())
        self._threads = []

    def start(self):
        pygame.init()
        self.getDisplay().initWindow()
        self.loadRoom()
        self.run()

    def loadRoom(self):
        for enemy in self.getRoom().getEnemies():
            thisThread = threading.Thread(target=self.npcThreads, args=(enemy, ))
            thisThread.start()
            self._threads.append(thisThread)
            time.sleep(.3)

    def unloadRoom(self):
        for enemy in self.getRoom().getEnemies():
            enemy.kill()

    def npcThreads(self, npc):
        while(npc.isAlive()):
            npc.getLock().acquire()
            xVel = random.randrange(-1,2)*npc.getSize()[0]/2
            yVel = random.randrange(-1,2)*npc.getSize()[1]/2
            npc.setVel((xVel, yVel))
            npc.move(self.getRoom())
            npc.getLock().release()
            #self.getDisplay().draw(npc.getSprite(), npc.getPos())
            time.sleep(.5)

    def run(self):
        while not self._stop:
            self.getEvent()
            self.getDisplay().fill()
            self.getDisplay().renderRoom(self.getRoom())
            nextRoom = self._player.move(self.getRoom())
            if nextRoom != None:
                self.unloadRoom()
                self.setRoom(nextRoom)
                self.loadRoom()
            self.getDisplay().draw(self._player.getSprite(), self._player.getPos())
            for enemy in self.getRoom().getEnemies():
                enemy.getLock().acquire()
                self.getDisplay().draw(enemy.getSprite(), enemy.getPos())
                enemy.getLock().release()
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

    def setRoom(self, room):
        self._room = room

    def close(self):
        self.unloadRoom()
        pygame.quit()
        quit()
