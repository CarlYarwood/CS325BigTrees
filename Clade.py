class Clade:
    def __init__(self, child1, child2, distance, stringRep):
        self.child1 = child1
        self.child2 = child2
        self.distance = distance
        self.stringRep = stringRep
    
    def getChild1Type(self):
        return type(self.child1)
    def getChild2Type(self):
        return type(self.child2)
    

class Leaf:
    def __init__(self, seqNum):
        self.seqNum = seqNum

    def getSeqNum(self):
        return self.seqNum

