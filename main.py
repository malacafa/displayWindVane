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
X = 1920/1300
Y = 1080/700
WM = graphWM([0,0],data[0])
WD = graphWD(data[1])
RM = graphRM([0,50],data[2])
pygame.font.init() 
myfont = pygame.font.SysFont('Consolas', 38)
titlefont = pygame.font.SysFont('Consolas', 50)

window = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
fps = pygame.time.Clock()
dt = datetime.datetime.now()
pygame.display.set_caption(str(dt)[0:-1])
key = 'Now'
place = 'Convention Center'

try:
    while END!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0]>1425 and 1870>pos[0] and pos[1]<845 and 775<pos[1]:
                    if key == 'Now':
                        key = 'School'
                        place = 'GSA'
                    elif key == 'School':
                        key = 'Now'
                        place = 'Convention Center'
        dt = datetime.datetime.now()
        pygame.display.set_caption(str(dt)[0:-7]+" Mode:::"+place)

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
        pygame.draw.rect(window, pygame.Color(12,77,162),pygame.Rect(int(965*X),int(500*Y),int(300*X),int(50*Y)))
        cnt = 0
        for i in rectWM:
            cnt += 1
            pygame.draw.rect(window, pygame.Color(20*cnt,255,20*cnt),pygame.Rect((i*CONST.width*X),((40*CONST.height-180)*Y),(CONST.width*6*X)+3,(CONST.height*25)*Y))
            if cnt > 11:
                break
        cnt = 0

        for i in rectRM:
            cnt += 1
            pygame.draw.rect(window, pygame.Color(20*cnt,20*cnt,255),pygame.Rect((i*CONST.width*X),((40*CONST.height+200)*Y),(CONST.width*6*X)+3,(CONST.height*25)*Y))
            if cnt > 11:
                break

        cirWD[0][0] = int(cirWD[0][0]*X)
        cirWD[0][1] = int(cirWD[0][1]*Y)
        cirWD[1][0] = int(cirWD[1][0]*X)
        cirWD[1][1] = int(cirWD[1][1]*Y)
        pygame.draw.circle(window, pygame.Color(255, 255, 255),cirWD[0], 230)
        pygame.draw.line(window, pygame.Color(255,0,0),cirWD[0],cirWD[1], 5)
        pygame.draw.line(window, pygame.Color(0,0,0),[0,int(350*Y)],[int(930*X),int(350*Y)], 3)
        pygame.draw.line(window, pygame.Color(0,0,0),[int(930*X),0],[int(930*X),int(700*Y)], 3)
        pygame.draw.line(window, pygame.Color(0,0,0),[int(930*X),int(470*Y)],[int(1300*X),int(470*Y)], 3)
        placetext = titlefont.render(place,False,(0,0,0))
        textmain = titlefont.render("Wind Speed( km/h )",False,(0,0,0))
        textmain2 = titlefont.render("Wind Direction",False,(0,0,0))
        textmain3 = titlefont.render("Rain Fall( mm/h )",False,(0,0,0))
        
        N = titlefont.render("N",False,(0,0,0))
        window.blit(N,( int(1110*X),int(100*Y)))
        E = titlefont.render("E",False,(0,0,0))
        window.blit(E,(int(1250*X),int(240*Y)))
        W = titlefont.render("W",False,(0,0,0))
        window.blit(W,(int(970*X),int(240*Y)))
        S = titlefont.render("S",False,(0,0,0))
        window.blit(S,(int(1110*X),int(380*Y)-20))

        txt = titlefont.render("Change MOD",False,(255,255,255))
        window.blit(txt,(1030*X,510*Y))

        textState = myfont.render("%02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d~"%(0,2,4,6,8,10,12,14,16,18,20,22), False, (0, 0, 0))
        textState2 = myfont.render("%02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d   %02d~"%(0,10,20,30,40,50,60,70,80,90,100,110), False, (0, 0, 0))
        window.blit(textmain,(65*X,30*Y))
        window.blit(textmain3,(65*X,410*Y))
        window.blit(textmain2,(990*X,60*Y))
        window.blit(textState,(65*X,70*Y))
        window.blit(textState2,(65*X,450*Y))
        window.blit(placetext,(1430,900))
        pygame.display.flip()
        fps.tick()

except Exception as e:
    print(str(datetime.datetime.now())[0:-7],"Thank you for using.")
    print("End program by '",e,"'")
    print("Created by SungHoon Yoon.")
