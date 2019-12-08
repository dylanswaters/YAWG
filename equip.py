class Equipment:
    name = ""
    accuracy = 0
    attack = 0
    armor = 0
    numSoldiers = 0
    numHits = 0
    numAttacks = 0
    cost = 0

    def __init__(self, name, acc, att, arm, numSo, numH, numA, cost):
        self.name = name
        self.accuracy = acc
        self.attack = att
        self.armor = arm
        self.numSoldiers = numSo
        self.numHits = numH
        self.numAttacks = numA
        self.cost = cost

    def getAcc(self):
        return self.accuracy

    def getAtt(self):
        return self.attack

    def getArmor(self):
        return self.armor

    def getName(self):
        return self.name

    def getSoldiers(self):
        return self.numSoldiers

    def getNumHits(self):
        return self.numHits

    def getNumAttacks(self):
        return self.numAttacks

    def getCost(self):
        return self.cost

    def setAcc(self, val):
        self.accuracy = val

    def setAtt(self, val):
        self.attack = val

    def setArmor(self, val):
        self.armor = val

    def setName(self, val):
        self.name = val

    def setSoldiers(self, val):
        self.numSoldiers = val

    def setNumHits(self, val):
        self.numHits = val

    def setNumAttacks(self, val):
        self.numAttacks = val

    def setCost(self, val):
        self.cost = val
