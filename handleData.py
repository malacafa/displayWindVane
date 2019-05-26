from data import dataGenor

class Currdata:
    def __init__(self):
        self.windDir = 0
        self.windMag = 0
        self.rainMag = 0
    
    def added(self,a):
        a += 1
        return a

    def set(self, windDir = 0, windMag = 0, rainMag = 0):
        if self.added(windDir):
            self.windDir = windDir
        if self.added(windMag):
            self.windMag = windMag
        if self.added(rainMag):
            self.rainMag = rainMag

    def get(self):
        return [self.windDir,self.windMag,self.rainMag]

class updateData:
    def __init__(self,key):
        self.dataGenNow = dataGenor('near')
        self.dataGenSchool = dataGenor('far')
        self.data = []
        self.key = key

    def recvData(self):
        if self.key == 'School':
            self.data = self.dataGenSchool.recv()
        elif self.key == 'Now':
            self.data = self.dataGenNow.recv()

    def getData(self):
        self.recvData()
        return self.data

if __name__ == '__main__':
    gdSchool = updateData('School')
    for _ in range(10):
        gdSchool.recvData()
        print(gdSchool.getData())