class Clade:
    def __init__(self, child1, child2, distance):
        self.child1 = child1
        self.child2 = child2
        self.distance = distance
        self.weight = child1.weight + child2.weight
    
    def getChild1Type(self):
        return type(self.child1)
    def getChild2Type(self):
        return type(self.child2)
    def generateStringRep(self):
        stringRep = "(" + self.child1.generateStringRep() + "," + \
         str(self.distance) + "," + self.child2.generateStringRep() + ")"
        return stringRep
    
class Conf_Clade():
    def __init__(self, clade, conf_val):
        self.clade = clade
        self.conf_val = conf_val


class Leaf:
    def __init__(self, seqNum):
        self.seqNum = seqNum
        self.weight = 1

    def getSeqNum(self):
        return self.seqNum

    def generateStringRep(self):
        return str(self.seqNum)
    

