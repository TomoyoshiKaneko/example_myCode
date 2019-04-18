import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,200))
FPSCLOCK = pygame.time.Clock()

def main():
    """main routine """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        # red 横線
        pygame.draw.line(SURFACE,(255,0,0),(10,80),(200,80))

        # red horizonal line(thickness 15)
        pygame.draw.line(SURFACE,(255,0,0),(10,150),(200,150),15)

        # green vertical line(thickness 10)
        start_pos = (300,30)
        end_pos = (380,200)
        pygame.draw.line(SURFACE,(0,0,255),start_pos,end_pos)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
