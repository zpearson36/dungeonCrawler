import pygame
from display import Display

if __name__ == "__main__":
    dsply = Display()
    dsply.initWindow()
    close = False
    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
        dsply.update()
    dsply.close()
