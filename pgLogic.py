from math import sin,cos,pi
from pgConstant import Constants

class graphWM:
    def __init__(self, startP, data):
        self.startP = startP
        self.const = Constants()
        self.data = data
        self.xPos = 0
        self.yPos = 0
    
    def setData(self,data):
        self.data = data

    def rectInfo(self):
        rectList = []
        self.xPos = self.startP[0]+5
        self.yPos = self.startP[1]+40
        rectList.append(self.xPos)
        i = self.data
        while i>0: # 0~20
            i -= 2
            self.xPos += self.const.rectWidIndex+1
            rectList.append(self.xPos)
        return rectList

class graphRM:
    def __init__(self, startP, data):
        self.startP = startP
        self.const = Constants()
        self.data = data
        self.xPos = 0
        self.yPos = 0

    def setData(self,data):
        self.data = data
    
    def rectInfo(self):
        rectList = []
        self.xPos = self.startP[0]+5
        self.yPos = self.startP[1]+40
        rectList.append(self.xPos)
        i = self.data
        while i>0: # 0~40
            i -= 10
            self.xPos += self.const.rectWidIndex+1
            rectList.append(self.xPos)
        return rectList

class graphWD:
    def __init__(self, data):
        self.const = Constants()
        self.data = data
        self.cirC = [0,0]
        self.cirEnd = [0,0]
    
    def setData(self,data):
        self.data = data
    
    def cirInfo(self):
        self.cirC = [1120,250]
        theta = self.data*2*pi/16-pi/2
        x = self.cirC[0] + self.const.radius*cos(theta)
        x /= 1
        y = self.cirC[1] + self.const.radius*sin(theta)
        y /= 1
        self.cirEnd = [x,y]
        return [self.cirC,self.cirEnd]
        