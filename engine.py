import random
import tkinter

from city import *
from unit import *
from country import *
from factory import *
from equip import *
from globals import *
from placeNames import *

def main():
    countryList = []
    for rcni in range(0,5):
        countryList.append(Country(getRevName(getName())))
    cityList = []
    PosCheckList = []

    while(len(cityList) < 50):
        rx = random.randint(0,100)
        ry = random.randint(0,100)
        rpop = 0
        if(len(cityList) < 10):
            rpop = random.randint(45000,99000)
        if(len(cityList) < 20 and len(cityList) > 9):
            rpop = random.randint(800,5000)
        if(len(cityList) < 30 and len(cityList) > 19):
            rpop = random.randint(3500,15000)
        if(len(cityList) < 40 and len(cityList) > 29):
            rpop = random.randint(10000,50000)
        if(len(cityList) < 50 and len(cityList) > 39):
            rpop = random.randint(100,1000)
        if([rx,ry] not in PosCheckList):
            PosCheckList.append([rx,ry])
            newCity = City(rx, ry, getName(), rpop)
            cityList.append(newCity)
            # print(newCity)

    # for country in countryList:
        # print(country)

    for coi in range(0,len(countryList)):
        curCountry = countryList[coi]
        curCity = cityList[0]
        curCountry.addCity(curCity)
        cityList.remove(curCity)
        for aci in range(0, 9):
            smallestDistI = 0
            smallestDist = curCity.getDist(cityList[0])
            for cii in range(1, len(cityList)):
                if(smallestDist < curCity.getDist(cityList[cii])):
                    smallestDistI = cii
            curCountry.addCity(cityList[smallestDistI])
            curCity = cityList[smallestDistI]
            cityList.remove(curCity)

    inputBuffer = " "
    playerCountry = None
    master = Tk()
    master.title("YAWG")

    
    countryNames = ""
    for cni in range(0, len(countryList)):
        countryNames += str(cni) + "- " + countryList[cni].getName() + " "
    print(countryNames)
    inputBuffer = input()
    try:
        int(inputBuffer)
    except:
        print("invalid input")
        return
    playerCountry = countryList[int(inputBuffer)]


    while(inputBuffer != "q"):
        # update ui
        master.update_idletasks()
        master.update()
        # show menu
        #
        for city in playerCountry.getCities():
            print(city)
        inputBuffer = input()


if __name__ == '__main__':
    main()
