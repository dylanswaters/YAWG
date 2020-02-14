import random
from tkinter import *
from tkinter import ttk

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
    root = Tk()
    root.title("YAWG")
    rootFrame = ttk.Frame(root, padding="10")
    rootFrame.grid(column=0, row=0)
    playerCountry = None

    countryNames = ""
    for cni in range(0, len(countryList)):
        countryNames += "\"" + countryList[cni].getName() + " | Pop: " + str(countryList[cni].getPopTotal()) + "\" "
        # print(countryNames)
    countryNames = StringVar(value=countryNames)
    countryListBox = Listbox(rootFrame, listvariable=countryNames, width=40, height=10)
    countryListBox.grid(column=1,row=1)
    # countryListBox.selection_set(0)

    def play(*args):
        # set player country
        playerCountry = countryList[countryListBox.curselection()[0]]
        # delete the current widgets
        list = rootFrame.grid_slaves()
        for l in list:
            l.grid_forget()
        # create new screen
        playerCountryName = playerCountry.getName()
        countryNameLabel = ttk.Label(rootFrame, textvariable=playerCountryName, width=40, height=10)
        countryNameLabel.grid(column=1, row=1)

    playButton = Button(rootFrame, text='Play', command=play).grid(column=1, row=2)


    root.mainloop()
    # inputBuffer = input()
    # try:
    #     int(inputBuffer)
    # except:
    #     print("invalid input")
    #     return
    # playerCountry = countryList[int(inputBuffer)]
    # while(inputBuffer != "q"):
    #     # update ui
    #     root.update_idletasks()
    #     root.update()
    #     root.mainloop()
    #     # show menu
    #     #
    #     for city in playerCountry.getCities():
    #         print(city)
    #     inputBuffer = input()


if __name__ == '__main__':
    main()
