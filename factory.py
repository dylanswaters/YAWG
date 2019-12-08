from equip import *

class Factory:
    equipment = None
    manufacturingSpeed = 0
    currentProg = 0

    def __init__(self):
        self.equipment = None
        self.manufacturingSpeed = 0
        self.currentProg = 0

    def setEquipment(self, e):
        self.equipment = e

    def tickProgress(self):
        self.currentProg += self.manufacturingSpeed
        if(self.currentProg > self.equipment.getCost()):
            self.currentProg -= self.equipment.getCost()
            return 1
        return 0
