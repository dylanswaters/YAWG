class Country:
    name = ""
    popTotal = 0
    popCivilian = 0
    popMilitary = 0
    equipment = []
    cities = []

    def __init__(self, name):
        self.name = name
        self.popTotal = 0
        self.popCivilian = 0
        self.popMilitary = 0
        self.equipment = []
        self.cities = []

    def __str__(self):
        retstr = self.name + ": " + str(len(self.cities)) + " cities, " + str(self.popTotal/1000) + "k pop\n\tcities: "
        for city in self.cities:
           retstr += str(city.getName()) + ", "
        return retstr

    def getPopTotal(self):
        return self.popTotal

    def getName(self):
        return self.name

    def getCities(self):
        return self.cities

    def addCity(self, city):
        city.setCountry(self)
        self.cities.append(city)
        self.popTotal += city.getPop()

    def delCityByIndex(self, index):
        self.cities[index].setCountry(None)
        self.popTotal -= self.cities[index]
        self.cities.remove(index)

    def delCityByCity(self, city):
        city.setCountry(None)
        self.popTotal -= city.getPop()
        self.cities.remove(city)
