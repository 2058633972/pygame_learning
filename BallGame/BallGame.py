#Author:Haicheng Qin
import pygame,sys
pygame.init()
#vinfo=pygame.display.Info()
#size = width, height = vinfo.current_w,vinfo.current_h #sized的width，height为整个窗口的宽和高
size=width,height=600,400
speed = [1, 1]
black = 0, 0, 0
screen = pygame.display.set_mode(size,pygame.RESIZABLE)#窗口大小可调
#screen = pygame.display.set_mode(size,pygame.NOFRAME)#无边框显示
#screen = pygame.display.set_mode(size,pygame.FULLSCREEN)#全屏显示
icon=pygame.image.load("balls.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("色彩型")
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()
still=False #用于控制小球运动或静止
bgcolor=pygame.Color("black")
def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0]=speed[0] if speed[0] == 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0]+1 if speed[0] > 0 else speed[0]-1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))
            elif event.key == pygame.K_UP:
                speed[1] = speed[1]+1 if speed[1] > 0 else speed[1]-1
            elif event.key==pygame.K_ESCAPE:
                sys.exit()
        elif event.type==pygame.VIDEORESIZE:
            size=width,height=event.size[0],event.size[1]
            screen=pygame.display.set_mode(size,pygame.RESIZABLE)#感知窗口的变化并刷新
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:  #数字1为鼠标左键的编号
                still=True   #still为True代表停止移动即鼠标左键按下时停止移动
        elif event.type==pygame.MOUSEBUTTONUP:
            still=False
            if event.button==1:
                ballrect=ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)
        elif event.type==pygame.MOUSEMOTION:
            if event.buttons[0]==1:
                ballrect=ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)

    if pygame.display.get_active() and not still:#窗口没有最小化时小球运动，否则暂停
        ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        if ballrect.right>width and ballrect.right+speed[0]>ballrect.right:
            speed[0]=-speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if ballrect.bottom>height and ballrect.bottom+speed[1]>ballrect.bottom:
            speed[1]=-speed[1]
    bgcolor.r=RGBChannel(ballrect.left*255/width)
    bgcolor.g=RGBChannel(ballrect.top*255/height)
    bgcolor.b=RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))
    screen.fill(bgcolor)
    screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)
