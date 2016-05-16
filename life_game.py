import os
import time
class life():
    def __init__(self,size):
        map = open("map","r")
        read = map.readline()
        self.map = []
        self.minlive = 2
        self.maxlive = 3
        self.minb = 3
        self.maxb = 3
        self.sleep = 0.1
        while read:
            self.map.append(read.split())
            read = map.readline()
        print(self.map)
    def is_alive(self):
        while 1:
            for y in range(len(self.map)):
                for x in range(len(self.map[y])):
                    if self.map[y][x] == "1":
                        if not self.mnogo(self.minlive,self.maxlive,x,y):
                            self.map[y][x] = "0"
                    else:
                        if self.mnogo(self.minb,self.maxb,x,y):
                            self.map[y][x] = "1"
            for x in self.map:
                print(*x)
            time.sleep(self.sleep)
            os.system('clear')
    def mnogo(self,min,max,x,y):
        c = 0
        for j in range(y-1,y+2):
            for i in range(x-1,x+2):
                if self.map[j][i] == 1:
                    c += 1
        return ((c <= max) and (c >= min))
life = life(100)
