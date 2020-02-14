import math

class City:
    x = 0
    y = 0
    name = ""
    pop = 0
    country = None
    units = []
    factories = []

    def __init__(self, x, y, name, pop):
        self.x = x
        self.y = y
        self.name = name
        self.pop = pop
        self.country = None
        self.units = []
        self.factories = []

    def __str__(self):
        return str(self.name) + ": (" + str(self.x) + "," + str(self.y) + ") " + str(self.pop)

    def getPos(self):
        return [self.x, self.y]

    def getDist(self, city):
        a = city.getPos()
        return abs(math.sqrt(((self.x - a[0])**2) + ((self.y - a[1])**2)))

    def getPop(self):
        return self.pop

    def getName(self):
        return self.name

    def getCountry(self):
        return self.country

    def setCountry(self, c):
        self.country = c
