class Clade:
    def __init__(self, child1, child2, distance):
        self.child1 = child1
        self.child2 = child2
        self.distance = distance
        return
    def getChild1Type():
        return type(self.child1)
    def getChild2Type():
        return type(self.child2)

class Leaf:
    def __init__(self, seqNum):
        self.seqNum = seqNum
        return
    