#Author:Haicheng Qin
import pygame,sys
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("pygame游戏之旅")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        pygame.display.update()