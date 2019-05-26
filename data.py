import pymysql
import threading
import sys

class dataGenor:
    def __init__(self,place):
        self.conn = pymysql.connect(host = "", port = , user = "", passwd = "", db = "", charset="")
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        self.query = "select * from weather_"+place
        self.data = []
        self.run()
    
    def run(self):
        self.cur.execute(self.query)
        mainData = self.cur.fetchall()
        self.data = mainData[-1]
        self.conn.commit()
        threading.Timer(1,self.run).start()

    def recv(self):
        return [float(self.data["speed"])/100,float(self.data["direction"]),float(self.data["rain"])]
    
    def end(self):
        sys.exit(1)