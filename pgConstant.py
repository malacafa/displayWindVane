import ctypes

class Constants:
    def __init__(self):
        #user32 = ctypes.windll.user32
        #self.screenWid = user32.GetSystemMetrics(0)
        #self.screenHei = user32.GetSystemMetrics(1)
        self.screenWid = 1200
        self.screenHei = 700
        self.width = self.screenWid//100
        self.height = self.screenHei//100
        self.rectWidIndex = 5
        self.rectHeiIndex = 30
        self.radius = 150