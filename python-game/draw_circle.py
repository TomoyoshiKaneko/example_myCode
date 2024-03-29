import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    """main routine"""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        # red：塗りつぶし
        pygame.draw.circle(SURFACE,(255,0,0),(50,50),20)
        # red：太さ10
        pygame.draw.circle(SURFACE,(255,0,0),(150,50),20,10)
        # green：r=10
        pygame.draw.circle(SURFACE,(0,255,0),(50,150),10)
        # green：r=20
        pygame.draw.circle(SURFACE,(0,255,0),(150,150),20)
        # green：r=30
        pygame.draw.circle(SURFACE,(0,255,0),(250,150),30)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
