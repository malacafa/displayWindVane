import pygame
from handleData import updateData
from pgLogic import graphRM, graphWD, graphWM
from pgConstant import Constants
import datetime

GDSchool = updateData('School')
GDNow = updateData('Now')

data = GDNow.getData()
CONST = Constants()
END = False

WM = graphWM([0,0],data[0])
WD = graphWD(data[1])
RM = graphRM([0,50],data[2])
pygame.font.init() 
myfont = pygame.font.SysFont('Consolas', 25)
titlefont = pygame.font.SysFont('Consolas', 30)

window = pygame.display.set_mode((1300,700))
fps = pygame.time.Clock()
dt = datetime.datetime.now()
pygame.display.set_caption(str(dt)[0:-1])
key = 'Now'

try:
    while END!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0]>965 and 1265>pos[0] and pos[1]>500 and 1265>pos[1]:
                    if key == 'Now':
                        key = 'School'
                    elif key == 'School':
                        key = 'Now'

        dt = datetime.datetime.now()
        pygame.display.set_caption(str(dt)[0:-7]+" Mode:::"+key)

        if key == 'Now':
            data = GDNow.getData()
        elif key == 'School':
            data = GDSchool.getData()
        
        WM.setData(data[0])
        WD.setData(data[1])
        RM.setData(data[2])

        window.fill(pygame.Color(237,223,185))
        rectWM = WM.rectInfo()
        rectRM = RM.rectInfo()
        cirWD = WD.cirInfo()
        pygame.draw.rect(window, pygame.Color(12,77,162),pygame.Rect(965,500,300,50))
        cnt = 0
        for i in rectWM:
            cnt += 1
            pygame.draw.rect(window, pygame.Color(20*cnt,255,20*cnt),pygame.Rect(i*CONST.width,40*CONST.height-180,CONST.width*6,CONST.height*25))
            if cnt > 11:
                break
        cnt = 0
        for i in rectRM:
            cnt += 1
            pygame.draw.rect(window, pygame.Color(20*cnt,20*cnt,255),pygame.Rect(i*CONST.width,40*CONST.height+200,CONST.width*6,CONST.height*25))
            if cnt > 11:
                break
        
        pygame.draw.circle(window, pygame.Color(255, 255, 255),cirWD[0], 150)
        pygame.draw.line(window, pygame.Color(255,0,0),cirWD[0],cirWD[1], 10)
        pygame.draw.line(window, pygame.Color(0,0,0),[0,350],[930,350], 3)
        pygame.draw.line(window, pygame.Color(0,0,0),[930,0],[930,700], 3)
        pygame.draw.line(window, pygame.Color(0,0,0),[930,470],[1300,470], 3)
        textmain = titlefont.render("Wind Speed( km/h )",False,(0,0,0))
        textmain2 = titlefont.render("Wind Direction",False,(0,0,0))
        textmain3 = titlefont.render("Rain Fall( mm/h )",False,(0,0,0))
        
        N = titlefont.render("N",False,(0,0,0))
        window.blit(N,(1120-10,250-140-10))
        E = titlefont.render("E",False,(0,0,0))
        window.blit(E,(1120+140-10,250-10))
        W = titlefont.render("W",False,(0,0,0))
        window.blit(W,(1120-140-10,250-10))
        S = titlefont.render("S",False,(0,0,0))
        window.blit(S,(1120-10,250+140-10))

        txt = titlefont.render("Change MOD",False,(255,255,255))
        window.blit(txt,(1030,510))

        textState = myfont.render("%02d   %02d   %02d   %02d   %02d    %02d   %02d   %02d   %02d   %02d   %02d   %02d~"%(0,2,4,6,8,10,12,14,16,18,20,22), False, (0, 0, 0))
        textState2 = myfont.render("%02d   %02d   %02d   %02d   %02d    %02d   %02d   %02d   %02d   %02d   %02d   %02d~"%(0,10,20,30,40,50,60,70,80,90,100,110), False, (0, 0, 0))
        window.blit(textmain,(65,30))
        window.blit(textmain3,(65,410))
        window.blit(textmain2,(990,60))
        window.blit(textState,(65,70))
        window.blit(textState2,(65,450))
        pygame.display.flip()
        fps.tick()

except Exception as e:
    print(str(datetime.datetime.now())[0:-7],"Thank you for using.")
    print("End program by '",e,"'")
    print("Created by SungHoon Yoon.")