class Clade:
    def __init__(self, child1, child2, distance):
        self.child1 = child1
        self.child2 = child2
        self.distance = distance
        self.stringRep = stringRep
        self.weight = child1.weight + child2.weight
    
    def getChild1Type(self):
        return type(self.child1)
    def getChild2Type(self):
        return type(self.child2)
    def generateStringRep():
        stringRep = "(" + child1.generateStringRep() + "," + child2.generateStringRep + ")"
        return stringRep
    

class Leaf:
    def __init__(self, seqNum):
        self.seqNum = seqNum
        self.weight = 1

    def getSeqNum(self):
        return self.seqNum

    def generateStringRep():
        return str(self.seqNum)
    

