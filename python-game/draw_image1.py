import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    logo = pygame.image.load("pythonlogo.jpg")




#　プログラム変更済み
    SURFACE.fill((225,225,225))

        # 左上が(20,50)の位置にロゴを描画
    SURFACE.blit(logo,(20,50))

    pygame.display.update()
    FPSCLOCK.tick(30000)



if __name__ == '__main__':
    main()
