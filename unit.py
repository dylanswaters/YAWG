import random

class Unit:
    equipment = []
    name = ""
    numSoldiers = 0

    def __init__(self, name):
        self.equipment = []
        self.name = name
        self.numSoldiers = 0

    def takeDamage(self, damage):
        dam = damage[1] / damage[0]
        for i in range(0, damage[0]):
            randIndex = random.randint(0, len(self.equipment))
            if(equipment[randIndex].getArmor() < dam):
                numSoldiers -= equipment[randIndex].getSoldiers()
                equipment.remove(equipment[randIndex])

    def dealDamage(self):
        hitCount = 0
        damage = 0
        for i in equipment:
            hitRoll = random.randint(0,100)
            if(hitroll <= i.getAcc()):
                damage += i.getAtt()
                hitCount += 1
        return [hitcount, damage]

    def addEquipment(self, e):
        self.numSoldiers += e.getSoldiers()
        self.equipment.append(e)
